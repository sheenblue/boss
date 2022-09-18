# -*- coding: utf-8 -*-
# @Author : sheen
# @Time   : 2022-09-05
# @FILE   : win.py

# from win10toast import ToastNotifier
# toast = ToastNotifier()
# toast.show_toast(title="This is a title", msg="This is a message",
#                  icon_path=r"C:\Program Files\Internet Explorer\images\bing.ico", duration=10)

# modules
import schedule
import time
import webbrowser
from win10toast_click import ToastNotifier
import threading

# function
page_url = 'http://example.com/'

def open_url():
    try:
        webbrowser.open_new(page_url)
        print('Opening URL...')
    except:
        print('Failed to open URL. Unsupported variable type.')

# initialize
toaster = ToastNotifier()

# # showcase
# toaster.show_toast(
#     "Example two", # title
#     "Click to open URL! >>", # message
#     icon_path=None, # 'icon_path'
#     duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
#     threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears
#     callback_on_click=open_url # click notification to run function
#     )

# showcase
def tt():
    toaster.show_toast(
        "Example two", # title
        "抢儿儿~~~", # message
        icon_path=None, # 'icon_path'
        duration=100, # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears
        callback_on_click=open_url # click notification to run function
        )

def tt1():
    toaster.show_toast(
        "Example two", # title
        "起来运动~~", # message
        icon_path=None, # 'icon_path'
        duration=100, # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears
        callback_on_click=open_url # click notification to run function
        )
def tt1():
    toaster.show_toast(
        "Example two", # title
        "吃药", # message
        icon_path=None, # 'icon_path'
        duration=100, # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears
        callback_on_click=open_url # click notification to run function
        )


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


#schedule.every().day.at("17:10").do(run_threaded,tt)
schedule.every().day.at("09:30").do(run_threaded,tt)
#schedule.every(40).minutes.do(run_threaded, tt1)
schedule.every().day.at("09:55").do(run_threaded,tt)

while True:
    schedule.run_pending()
    time.sleep(1)

