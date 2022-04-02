import webbrowser

from win10toast_click import ToastNotifier


toaster = ToastNotifier()

def show_toast(title: str, description: str, url: str):
    """Show toast notification with the given title and description and also take to webpage when clicked on the notification"""

    toaster.show_toast(
        # The parameters should be non empty else the function holds indefinitely
        title= title if len(title)>0 else " ",
        msg= description if len(description)>0 else " ",
        icon_path= "ktulogo.ico",
        duration=2,
        callback_on_click= lambda: open_browser(url if len(url)>0 else " ")
    )


def open_browser(url: str):
    """Open default browser with the given url"""
    try:
        webbrowser.open_new(url)
        print("[+] Opening url in webbrowser")
    except:
        print("[X] Failed to open webbrowser")