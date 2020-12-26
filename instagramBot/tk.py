from tkinter import *
from tkinter import messagebox
from time import sleep
from selenium import webdriver
# from PIL import Image, ImageTk
import os
import instagram
from instagram import Bot
 



screen = Tk()
screen.title("INSTAGRAM BOT")
screen.geometry("550x400+300+150")
screen.resizable('false','false')


canvas = Canvas(screen,width = 550, height=300)
canvas.pack()
img= PhotoImage(file="tenor.gif")
canvas.create_image(35,30, anchor =NW, image=img)
start_button = Button(screen,text="Start",width=50,bg="green",command=Bot.InstagramBot)
close_button = Button(screen,text="Close",width=50,bg="red",command=Bot.close)
block_button = Button(screen,text="Block",width=50,bg="brown",command=Bot.Block)

# label.pack()
start_button.pack()
close_button.pack()
block_button.pack()








screen.mainloop()

# sudo apt-get install python3-pil.imagetk