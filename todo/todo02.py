import readxls
import schedule
import time
import webbrowser
from win10toast_click import ToastNotifier
import threading


page_url = 'http://example.com/'

def open_url():
    try:
        webbrowser.open_new(page_url)
        print('Opening URL...')
    except:
        print('Failed to open URL. Unsupported variable type.')

# initialize
toaster = ToastNotifier()

def td(title,message):
    toaster.show_toast(
        title, # title
        message, # message
        icon_path=None, # 'icon_path'
        duration= None, # for how many seconds toast should be visible; None = leave notification in Notification Center
        threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears
        #callback_on_click=open_url # click notification to run function
        )

def run_threaded(job_func,i,a,b):
    job_thread = threading.Thread(target=job_func,args=(i,a,b))
    job_thread.start()
    print('start')

def todo(title,message,time1):
    schedule.every().day.at(time1).do(td,title,message)

if __name__ == '__main__':
    title = '123'
    message = '封装系统'
    time1 = '13:00'
    run_threaded(todo,title,message,time1)
    title = '123'
    message = '去看医生'
    time1 = '10:30'
    run_threaded(todo, title, message,time1)
    title = '抢东西'
    message = '抢贝儿'
    time2 = '09:55'
    run_threaded(todo, title, message, time2)
    # schedule.every().day.at("22:13").do(td,title,message)
    while True:
        schedule.run_pending()
        time.sleep(1)

