import webbrowser

from win10toast_click import ToastNotifier


toaster = ToastNotifier()

def show_toast(title: str, description: str, url: str):
    """Show toast notification with the given title and description and also take to webpage when clicked on the notification"""

    toaster.show_toast(
        title= title,
        msg= description,
        icon_path= "ktulogo.ico",
        duration=2,
        callback_on_click= lambda: open_browser(url)
    )


def open_browser(url: str):
    """Open default browser with the given url"""
    try:
        webbrowser.open_new(url)
        print("[+] Opening url in webbrowser")
    except:
        print("[X] Failed to open webbrowser")