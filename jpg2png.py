from tkinter import *
from PIL import Image, ImageTk

# from tkinter import *

img = Image.open("/Users/kevin/Desktop/Tower73-p14.jpg")
img.save("/Users/kevin/Desktop/testing.png")

root = Tk()
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()

#
# https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python
#

tkimg = ImageTk.PhotoImage(Image.open("/Users/kevin/Desktop/testing.png"))
canvas.create_image(20, 20, anchor=NW, image=tkimg)

root.mainloop()
