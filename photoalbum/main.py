#install lib : pillow //lib for img processing 
import tkinter as tk #built-in library for creating Graphical User Interfaces (GUIs)
import time
from PIL import Image, ImageTk

#Main application Window
root = tk.Tk()
root.title("Photo slideshow album")
root.geometry("900x900")

# List of Image Paths
image_paths=[
    r"C:\Users\Downloads\dog.png",  #raw string , for path declare it will trated as path using r 
   r"C:\Users\Downloads\cat.jpeg",
    r"C:\Users\Downloads\rabbit.jpeg"
]

image_size=(500,500)
images=[]  #list for img 
for path in image_paths:
    img=Image.open(path)
    img=img.resize(image_size)
    images.append(img) #here adding rach img in the list

#convert img into Tkiter compatible img 
final_images=[] 
for img in images:
    photo= ImageTk.PhotoImage(img) #converting img to 
    final_images.append(photo)

#label widget to keep photo
image_label= tk.Label(root)
image_label.pack(pady=30)   #pacls a;; widget one after other in window

#slideshow for img
def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2) #2sec 
    
#button
play_button= tk.Button(
    root,
    text="play the slideshow",
    font=("Arial",17),
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()  #to keep the window open 
