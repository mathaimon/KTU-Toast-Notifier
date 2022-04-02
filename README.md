# KTU Toast Notifier

An app to display **Windows Toast Notification** for new [APJAKTU](https://ktu.edu.in/home.htm) announcements . The data is scraped from the official KTU webpage.


## Features
- [x] Toast Notification in Windows
- [x] Clikable notification that takes you to the specified notification
- [ ] Running program in background
- [ ] Running the program periodically using **Windows Task Scheduler**

## Flow of the Program
- KTU publishes a new notification
- Program scans the landing page to check wheather a new notification is published.
    - For some reason ktu announcements page takes 15-20 seconds to load so checking the landing page is necessary to reduce the resource usage.
- If a new notification is found it then opens the notifications tab to find the link to the notification
- Shows the clickable notifications in reverse chronological order


## Running the program
### Prerequisites
- **Python interpreter** added to path
- **Pipenv** package installed
    - If not install using `pip install pipenv`

Now run the program using the following command :

```
git clone https://github.com/cyberdog-m/KTU-Toast-Notifier.git
cd KTU-Toast-Notifier
pipenv run main.py
```