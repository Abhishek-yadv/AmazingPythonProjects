# Import necessary modules
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from plyer import notification

# URL to fetch live cricket scores
URL = 'http://www.cricbuzz.com/cricket-match/live-scores'

# Function to display notification
def notify(title, score):
    # Set maximum length for title and message
    max_title_length = 64
    max_message_length = 128

    # Truncate title and message if they exceed the maximum length
    truncated_title = title[:max_title_length]
    truncated_message = score[:max_message_length]

    # Display notification with truncated title and message
    notification.notify(
        title=truncated_title,
        message=truncated_message,
        app_name="Cricket Live Scores",  # Optional app name
        timeout=30,  # Duration in seconds
    )


while True:
    try:
        # Create a request object with custom user agent
        request = Request(URL, headers={'User-Agent': 'XYZ/3.0'})

        # Fetch the content from the URL
        response = urlopen(request, timeout=20).read()
        data_content = response

        # Parse the HTML content
        soup = BeautifulSoup(data_content, 'html.parser')

        # Find all the score elements
        for score in soup.find_all('div', attrs={'class': 'cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main'}):
            # Extract the header (match details)
            header = score.find(
                'div', attrs={'class': 'cb-col-100 cb-col cb-schdl'})
            header = header.text.strip()
            # Extract the score
            status = score.find(
                'div', attrs={'class': 'cb-scr-wll-chvrn cb-lv-scrs-col'})
            s = status.text.strip()
            # Display the notification with header and score
            notify(header, s)

    except Exception as e:
        # Print the error message if an exception occurs
        print("An error occurred:", e)

    # Wait for 10 seconds before fetching the scores again
    time.sleep(10)
