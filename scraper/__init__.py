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