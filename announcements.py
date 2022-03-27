import requests
from bs4 import BeautifulSoup


# Get the soup object of the given url
def get_url_soup(url):
    try :
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.ConnectionError:
        print('[X] Connection Refused; Please check Internet connection')
    return None

# Get list of rows form the announcements table 
def get_rows(soup):
    table = soup.find('table', {"class": "ktu-news"})
    rows = table.find_all('tr')
    return rows

# Get a specific announcement
def get_announcement(rows_soup, announcement_no : str):
    announcement = rows_soup[announcement_no].find_all('td')[1]

    # Get the title of the announcement
    title = announcement.find('b').text

    # Get the url of the announcement if 'a' tag exists
    if announcement.find('a'):
        url = announcement.find('a').get('href')
        # Remove tabs and spaces in the url and add the url prefix
        url = 'https://ktu.edu.in' + url.replace('\t','').replace('\r','').replace(' ', '')

        # Text inside the 'a' tag
        url_text = announcement.find('a').text
    else :
        print('[X] There is no url for the announcement')
        url = ''
        url_text = ''

    # Get the description text
    description = announcement.find('li').text
    # Remove the title string and the url text string to get the description
    description = description.replace(title, '').replace(url_text, '').strip()
    
    return title, description, url


if __name__ == "__main__":
    url = 'https://ktu.edu.in/eu/core/announcements.htm'
    
    rows = get_rows(get_url_soup(url))