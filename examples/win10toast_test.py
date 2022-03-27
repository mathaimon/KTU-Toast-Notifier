from win10toast_click import ToastNotifier

def callback_fn(data: str):
    print('callback recieved')
    print(data)

test_message = 'It is hereby informed that the course/exam registration for MCA S6 (R,S) Exam May 2022 and MCA INT S10 (R,S) Exam May 2022 are opened in the KTU portal. Registration submission by students through student login and payment of fee at College office on or before 30.03.2022, Wednesday . Request submission by Colleges to Un'
    
toaster = ToastNotifier()
toaster.show_toast("Hello World!!!",
                   test_message,
                   icon_path="ktulogo.ico",
                   duration=2,
                   callback_on_click=lambda: callback_fn('somedata')
                )
