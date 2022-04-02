import sys

import scraper
import database
from scraper import landing, announcements
import toast


def check_new_announcement() -> bool:
    """Get the last notification from the KTU landing page and compare it with the last announcement in the database"""

    landing_url = "https://ktu.edu.in/home.htm"

    landing_soup = landing.get_announcement_section(scraper.get_url_soup(landing_url))
    print("[+] Landing page scraped")

    # Get the last announcement title from the announcement list
    last_announcement = landing.get_announcement(landing_soup, 0)

    return database.check_exists(last_announcement)


def get_new_announcement():
    """Get the last 5 announcements and if the notification is not shown show toast notification and add to database"""

    announcements_url = "https://ktu.edu.in/eu/core/announcements.htm"
    
    announcement_soup = announcements.get_annoucement_rows(scraper.get_url_soup(announcements_url))
    print("[+] Announcements page scraped")

    for i in range(5):
        title, description, url = announcements.get_announcement(announcement_soup, i)

        # Check if announcement exist in the database
        if not database.check_exists(title):
            # add announcement to the database
            database.add_announcement(
                title= title,
                description= description,
                url = url
            )
            print("[+] Added new  announcement to database")



def show_toast_notifications():
    """Show toast notifications for un-notified announcements in the database"""
    un_notified_announcements = database.unnotified_announcements()
    for announcement in un_notified_announcements:
        # show toast notification
        try:
            # Printing debug info and first 40 characters of announcement
            print(f"[+] Showing Toast Notification \n \t {announcement['title'][:40]} .....")

            toast.show_toast(
                title= announcement['title'],
                description= announcement['description'],
                url = announcement['url']
            )

            # update the database on the notification showed status
            database.update_notified(database.get_query(announcement["title"]))
            print("[+] Updating database on notified status")
        except:
            print("[+] Failed to show Toast Notification")
    


if __name__ == "__main__":
    ## Exit program if no updates are found
    if check_new_announcement() == True:
        print("[+] No new announcements found")
        show_toast_notifications()

        sys.exit()

    print("[+] New announcements found")
    
    get_new_announcement()
    show_toast_notifications()