import sys

import scraper
import database
from scraper import landing, announcements


def check_new_announcement() -> bool:
    """Get the last notification from the KTU landing page and compare it with the last announcement in the database"""

    landing_url = "https://ktu.edu.in/home.htm"

    landing_soup = landing.get_announcement_section(scraper.get_url_soup(landing_url))

    # Get the last announcement title from the announcement list
    last_announcement = landing.get_announcement(landing_soup,0)

    return database.check_exists(last_announcement)


def get_new_announcement():
    """Get the last 5 announcements and if the notification is not shown show toast notification and add to database"""

    announcements_url = "https://ktu.edu.in/eu/core/announcements.htm"
    
    announcement_soup = announcements.get_annoucement_rows(scraper.get_url_soup(announcements_url))

    for i in range(5):
        title, description, url = announcements.get_announcement(announcement_soup, i)

        if not database.check_exists(title):
            database.add_announcement(
                title= title,
                description= description,
                url = url
            )


if __name__ == "__main__":
    ## Exit program if no updates are found
    if not check_new_announcement():
        print("[+] No new announcements found")
        sys.exit()