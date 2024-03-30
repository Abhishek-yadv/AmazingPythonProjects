import selenium
import email_validator
from selenium import webdriver
from email_validator import validate_email, EmailNotValidError
import csv


def LinkedIn_Email_Scraper(userEmail, userPassword):
    emailList = {}
    browser = webdriver.Chrome()
    # example => 'https://www.linkedin.com/feed/update/urn:li:activity:7176894692121350144/'
    url = 'https://www.linkedin.com/feed/update/urn:li:activity:7176894692121350144/'
    # visits page of the desired post
    browser.get(url)
    browser.implicitly_wait(5)
    # finds comments buttons
    commentDiv = browser.find_element(
        'xpath', '/html/body/main/section[1]/section[1]/div/div[3]/a[2]')
    loginLink = commentDiv.get_attribute('href')
    browser.get(loginLink)
    email = browser.find_element('xpath', '//*[@id="username"]')
    password = browser.find_element('xpath', '//*[@id="password"]')
    # inputs email in email field
    email.send_keys(userEmail)
    # inputs password in password field
    password.send_keys(userPassword)
    submit = browser.find_element(
        'xpath', '//*[@id="app__container"]/main/div[3]/form/div[3]/button')
    submit.submit()  # submits form
    browser.implicitly_wait(5)
    # finds the comments section
    commentSection = browser.find_element(
        'css_selector', '.comments-comments-list')
    for _ in range(3):  # this can also be set to any number or "while True" if you want it to search through the whole comment section of the post
        try:
            moreCommentsButton = commentSection.find_element('class_name', 'comments-comments-list__show-previous-container').find_element('tag_name', 'button')
            moreCommentsButton.click()
            browser.implicitly_wait(5)
        except:
            print('End of checking comments')
            break
    browser.implicitly_wait(20)
    # finds all individual comments
    comments = commentSection.find_elements('tag_name', 'article')
    for comment in comments:
        try:
            # finds name of commenter
            commenterName = comment.find_element(
                'class_name', 'hoverable-link-text')
            commentText = comment.find_element('tag_name', 'p')
            # finds email of commenter
            commenterEmail = commentText.find_element(
                'tag_name', 'a').get_attribute('innerHTML')
            # validates email address
            validEmail = validate_email(commenterEmail)
            commenterEmail = validEmail.email
        except:
            continue
        emailList[commenterName.get_attribute('innerHTML')] = commenterEmail
    browser.quit()
    return emailList


def DictToCSV(input_dict):
    # Converts dictionary into csv
    with open('./LinkedIn Email Scraper/emails.csv', 'w') as f:
        f.write('name,email\n')
        for key in input_dict:
            f.write('%s,%s\n' % (key, input_dict[key]))
    f.close()


if __name__ == '__main__':
    # Put your user Email and Password
    userEmail = 'youremail@gmail.com.com'
    userPassword = 'Your Password'
    emailList = LinkedIn_Email_Scraper(userEmail, userPassword)
    DictToCSV(emailList)
