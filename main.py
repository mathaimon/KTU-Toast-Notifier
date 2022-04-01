import sys

import scraper
import database
from scraper import landing, announcements


def check_new_announcement() -> bool:
    """Get the last notification from the KTU landing page and compare it with the last announcement in the database"""

    landing_url = "https://ktu.edu.in/home.htm"

    landing_soup = landing.get_announcement_section(scraper.get_url_soup(landing_url))

    # Get the last announcement from the announcement list
    last_announcement = landing.get_announcement(landing_soup,0)

    return database.check_exists(last_announcement)


if __name__ == "__main__":
    if not check_new_announcement():
        print("[+] No new announcements found")
        sys.exit()