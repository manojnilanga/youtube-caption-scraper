# from youtube_transcript_api import YouTubeTranscriptApi
#
#
# api_key =  "AIzaSyACfmxx7vCPk2wy4BNT07L6IJ5oGsAIc9g"
# video_id = "jO6qQDNa2UY"
#
#
# url = "https://www.youtube.com/watch?v=jO6qQDNa2UY&t=195s"
# video_id = url[32:43]
# print(video_id)
#
#
#
# responses = YouTubeTranscriptApi.get_transcript(
#             video_id, languages=['en'])
#
# file = open(video_id+".txt","w",encoding="utf-8")
#
# for i in range(0, len(responses)):
#     file.write(responses[i]["text"]+"\n")
# file.close()

from threading import Thread
from tkinter import font
from youtube_transcript_api import YouTubeTranscriptApi
import tkinter as tk

api_key =  "AIzaSyACfmxx7vCPk2wy4BNT07L6IJ5oGsAIc9g"
video_id = "jO6qQDNa2UY"

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
            if("watch" in urls[i]):
                video_id = urls[i][32:43]
            else:
                video_id = urls[i].split("/")[3][:11]
            print(video_id)
            responses = YouTubeTranscriptApi.get_transcript(
                        video_id, languages=['en'])
            file = open(video_id+".txt","w",encoding="utf-8")
            print("writing file for: "+urls[i])
            for i in range(0, len(responses)):
                file.write(responses[i]["text"]+" ")
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