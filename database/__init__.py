from tinydb import TinyDB, Query
import datetime

db = TinyDB('announcements_db.json')

"""
Sample database
{
    1:{
        title: "Announcement Title",
        description: " Description of the Annoncement",
        url : "https://ktu.edu.in/eu/......",
        isNotified : True,
        added_time: ''
        last_updated: ''
        notified_time : ''
    }
}
"""
def check_exists(announcement_title: str)-> bool:
    """Checks if the announcement with the given title is present in the database"""
    for announcement in db.all(): 
        return True if announcement['title'] == announcement_title else False

def add_announcement(title: str, description: str, url: str):
    """Add a new announcement to the database"""
    announcement = {
        "title": title,
        "description": description,
        "url": url,
        "is_notified": False,
        "added_time": str(datetime.datetime.now()),
        "last_updated": str(datetime.datetime.now()),
        "notified_time" : ''
    }
    db.insert(announcement)

def update_notified(announcement_query : Query):
    """Update the notified status and notified time of announcement_query"""
    update_data ={
        "is_notified" : True,
        "notified_time": str(datetime.datetime.now()),
        "last_updated": str(datetime.datetime.now())
    }
    db.update(update_data, announcement_query)

def get_notified_status(announcement_index: int) -> bool:
    """Get the 'is_notified' status of the announcement with the given announcement index"""
    return db.all()[announcement_index]["is_notified"]

