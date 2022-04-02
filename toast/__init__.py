import webbrowser

from win10toast_click import ToastNotifier


toaster = ToastNotifier()

def show_toast(title: str, description: str, url: str):
    toaster.show_toast(
        title= title,
        msg= description,
        duration=3,
        callback_on_click= lambda: open_browser(url)
    )


def open_browser(url: str):
    try:
        webbrowser.open_new(url)
        print("[+] Opening url in webbrowser")
    except:
        print("[X] Failed to open webbrowser")