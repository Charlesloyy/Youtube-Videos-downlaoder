from tkinter import *
from pytube import YouTube



root = Tk()
root.geometry("300x250")


label = Label(root, text ="Enter your link below",anchor=CENTER, font = ("arial", 20), bd = 4)
label.grid(row=0, column=0, columnspan=5)


link_entry = Entry(root, width = 32, bd = 4)
link_entry.grid(row=1, column=1, columnspan=5, sticky = E + W)

def search():
    link = link_entry.get()
    yt = YouTube(link)
    label = Label(root, text =yt.title,anchor=CENTER, font = ("arial", 12), bd = 4)
    label.grid(row=2, column=0, columnspan=5)
##    label = Label(root, text =yt.description,anchor=CENTER, font = ("arial", 10), bd = 4)
##    label.grid(row=3, column=0, columnspan=5)
    
def download():
    link = link_entry.get()

    yt = YouTube(link)

    yd = yt.streams.get_highest_resolution()
    yd.download('/Users/Oloye/Desktop')

    
enter = Button(root, text = "Search", font = ("arial", 13), bd = 4, command = search)
enter.grid(row=1, column=0, sticky = E + W, padx = 10)

enter2 = Button(root, text = "Download", font = ("arial", 13), bd = 4, command = download)
enter2.grid(row=4, column=1, sticky = E + W, padx = 10)


root.mainloop()
