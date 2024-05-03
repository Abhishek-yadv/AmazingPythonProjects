import requests
from bs4 import BeautifulSoup
import time
import random

# List of user-agent
user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',]

# put your proxy servers
proxy_list = [
    'http://proxy1:port',
    'http://proxy2:port',]

def get_movie_info(movie_name):
    # Replace spaces with '+' for the URL
    movie_name = movie_name.replace(' ', '+')

    # Construct the IMDB search URL
    url = f'https://www.imdb.com/find?q={movie_name}&ref_=nv_sr_sm'
    print(f"Searching for movie: {url}")

    try:
        # Select a random user-agent
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}

        # Select a proxy server
        proxy = random.choice(proxy_list)
        proxies = {'http': proxy, 'https': proxy}

        # GET request
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the first movie result
        movie_result = soup.find('td', class_='result_text')

        if movie_result:
            # Extract the movie URL from the result
            movie_url = 'https://www.imdb.com' + movie_result.a['href']

            # Send a GET request to the movie URL
            movie_response = requests.get(
                movie_url, headers=headers, proxies=proxies)
            movie_response.raise_for_status()  # Raise an exception for non-2xx status codes
            movie_soup = BeautifulSoup(movie_response.content, 'html.parser')

            # Extract movie information from the page
            title = movie_soup.find(
                'div', class_='title_wrapper').h1.text.strip()
            rating = movie_soup.find('span', itemprop='ratingValue').text
            description = movie_soup.find(
                'span', class_='summary_text').text.strip()

            return {
                'title': title,
                'rating': rating,
                'description': description}
        else:
            print(f"No movie results found for '{movie_name}'")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching movie information: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


if __name__ == '__main__':
    movie_name = input('Enter a movie name: ')
    movie_info = get_movie_info(movie_name)

    if movie_info:
        print(f"Title: {movie_info['title']}")
        print(f"Rating: {movie_info['rating']}")
        print(f"Description: {movie_info['description']}")
    else:
        print('Movie not found.')
