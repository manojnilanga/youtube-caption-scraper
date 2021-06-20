from threading import Thread
from tkinter import font

import requests
from bs4 import BeautifulSoup
import tkinter as tk


is_run = True
def start():
    print("Starting ...")
    global is_run
    is_run = True

    t = Thread(target=start_checking)
    t.start()

def stop():
    print("Stopping ...")
    global is_run
    is_run = False

def start_checking():
    urls = text_urls.get("1.0", "end").split("\n")
    for i in range(0,len(urls)):
        try:
            if is_run == False:
                break
            if("http" not in urls[i]):
                continue
            response = requests.get(urls[i])
            soup = BeautifulSoup(response.text, 'html.parser')
            caption= soup.title.string[:-10]
            print(caption)
            file = open("output.txt","a", encoding="utf-8")
            file.write(caption+"\n")
            file.close()
        except:
            print("Error here : "+urls[i])
            continue
    print("Finished !")

window = tk.Tk()
window.geometry("700x700")
window.title("Youtube Caption Scraper")
text_urls = tk.Text(width=84, height=38)
text_urls.place(x=10, y=10)

myFont = font.Font(size=12)

btn_start= tk.Button(text="Stop", width=20,height=2,command=stop)
btn_start.place(x=300,y=640)
btn_start['font'] = myFont
btn_stop= tk.Button(text="Start", width=20,height=2,command=start)
btn_stop.place(x=500,y=640)
btn_stop['font'] = myFont
window.mainloop()