# KTU Toast Notifier

An app to display **Windows Toast Notification** for new [APJAKTU](https://ktu.edu.in/home.htm) announcements . The data is scraped from the official KTU webpage.


## Features
- Toast Notification in Windows
- Clikable notification that takes you to the specified notification

## Flow of the Program
- KTU publishes a new notification
- Program scans the landing page to check wheather a new notification is published.
    - For some reason ktu announcements page takes 15-20 seconds to load so checking the landing page is necessary to reduce the resource usage.
- If a new notification is found it then opens the notifications tab to find the link to the notification
- Shows the clickable notifications in reverse chronological order