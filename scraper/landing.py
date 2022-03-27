# Scraping script for landing page of KTU
from bs4 import BeautifulSoup


# Get list of announcements form announcements section
def get_announcement_section(soup: BeautifulSoup):
    table = soup.find('ul', {"class": "annuncement"})
    announcements = table.find_all('li')
    return announcements

def get_announcement(soup : BeautifulSoup, announcement_no: int):
    announcement = soup[announcement_no].find('a').text
    return announcement