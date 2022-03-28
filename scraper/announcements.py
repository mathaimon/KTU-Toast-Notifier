# Scraping script for announcements page of KTU
from bs4 import BeautifulSoup

def get_annoucement_rows(soup: BeautifulSoup):
    """Get list of rows from the announcements table"""
    table = soup.find('table', {"class": "ktu-news"})
    rows = table.find_all('tr')
    return rows

def get_announcement(rows_soup: BeautifulSoup, announcement_no : str):
    """"Get a specific announcement"""
    announcement = rows_soup[announcement_no].find_all('td')[1]

    # Get the title of the announcement
    title = announcement.find('b').text

    # Get the url of the announcement if 'a' tag exists
    if announcement.find('a'):
        url = announcement.find('a').get('href')
        # Remove tabs and spaces in the url and add the url prefix
        url = 'https://ktu.edu.in' + url.replace('\t','').replace('\r','').replace('\n','').replace(' ', '')

        # Text inside the 'a' tag
        url_text = announcement.find('a').text
    else :
        print('[X] There is no url for this announcement')
        url = ''
        url_text = ''

    # Get the description text
    description = announcement.find('li').text.replace('\n', ' ')
    # Remove the title string and the url text string to get the description
    description = description.replace(title, '').replace(url_text, '').strip()
    
    return title, description, url