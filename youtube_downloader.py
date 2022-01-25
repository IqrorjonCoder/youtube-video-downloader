import time
from tkinter import *
from pytube import YouTube

main = Tk()
main.title("youtube downloader")
main.geometry("400x300")
main.resizable(False, False)
main.configure(bg="#fff")



def download_function():

    link = entry.get()
    yt = YouTube(link)
    time.sleep(3)

    ys = yt.streams.get_highest_resolution()
    ys.download("/home/iqrorjon/Videos/")

    time.sleep(3)

    text_label.config(text="Success !!!")


entry = Entry(main, width=40, bg="#dddddd", highlightcolor="#000")
entry.place(x=50, y=30)


dwn_button = Button(main, width=20, text="Download", command=download_function)
dwn_button.pack(pady=100)


text_label = Label(main, text=f"", width=40, highlightcolor="#000", bg="#fff")
text_label.pack(pady=10)


main.mainloop()