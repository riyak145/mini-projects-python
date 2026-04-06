#import tkinter for creating GUI apps
import tkinter as tk
#sub modules: 
from tkinter import filedialog, messagebox

#main window
root = tk.Tk()
root.title("My Text Editor")
root.geometry("800x600") #size of editor

#create text area
text = tk.Text(
    root,
    wrap = tk.WORD, #the whole word will be together , not break in half if line ends 
    font=("Helvetica",12)

)
text.pack(expand= True, fill=tk.BOTH)

#logic :
#function : to create a new file 
def new_file():
    text.delete(1.0,tk.END)

#function 2 : to open a new file 
def open_file():
    #open file dialog 
    file_path=filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        #open selected file , "r" ; read
        with open(file_path, "r") as file:
            #clear old text
            text.delete(1.0,tk.END)
            text.insert(tk.END, file.read())
#funcrion 3 : save the file
def save_file():
    #open save file dialog to save file 
    file_path=filedialog.asksaveasfilename(
         defaultextension=".txt",
         filetypes=[("Text Files", "*.txt")]
    )

    if file_path: #only if user save the file with name then pop up this msg as its inside if and if its not saved and cancled "" then msg will not pop up 
        with open(file_path,"w") as file:
            file.write(text.get(1.0,tk.END))
        messagebox.showinfo("Info","File saved Successfully")

#here createb menu bar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)

#new open, save , exist

#add file menu bar 
menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# starts and keeps the window open 
root.mainloop()


