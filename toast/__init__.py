from win10toast_click import ToastNotifier

toaster = ToastNotifier()

def show_toast(title: str, description: str):
    toaster.show_toast(
        title= title,
        msg= description,
        duration=3
    )
