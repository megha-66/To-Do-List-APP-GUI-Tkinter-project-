
import tkinter
from tkinter import * 
from pathlib import Path 
import sys 

if getattr(sys, 'frozen', False): 
    base_dir = Path(sys._MEIPASS)  
else:
    base_dir = Path(r"<path-to-your-main-directory>")  #Follow the directory structure as mentioned in README.md.
    

path1 = base_dir/'images'/'topicon.png'
path2 = base_dir / 'images' / 'toptitlebar.png'
path3 = base_dir/'images'/'deletebutton.png'

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_list = []

def addProgress():
    task = task_entry.get()
    task_entry.delete(0,END)
    
    if task :
        with open("items.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
        
def deleteProgress():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
       task_list.remove(task)
       with open("items.txt", "w") as taskfile:
           for task in task_list:
               taskfile.write(task+"\n")
               
       listbox.delete(ANCHOR)        
    


def openTaskfile():
    
    try : 
        global task_list 
        with open("items.txt", "r") as taskfile:
            tasks= taskfile.readlines()
        
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
                
    except :
       file = open('items.txt','w')
       file.close()            

#icon
Image_icon = PhotoImage(file = str(path1))
root.iconphoto(False, Image_icon)



#top bar
TopImage = PhotoImage(file = str(path2))
Label(root, image = TopImage).pack()

#heading_bar
heading = Label(root, text = "List all the items/works", font = "arial 16 bold", fg = "white", bg = "#32405b")
heading.place(x=130, y=20)

#main
frame = Frame(root, width = 400, height = 50, bg = 'white')
frame.place(x=0,y=180)

task = StringVar()
task_entry = Entry(frame, width = 18, font = 'arial 15 ', bd = 0)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text = 'ADD', font = 'arial 14 bold', width = 6, bg = '#5a95ff', fg = '#fff', bd = 0, command=addProgress)
button.place(x=320,y=0)

#listbox
frame1 = Frame(root, bd = 3, width = 700, height = 280, bg = "#32405b")
frame1.pack(pady = (160,0))

listbox = Listbox(frame1, font = ('arial', 12), width = 40, height = 16, bg = "#32405b", fg = "white", cursor = "hand2", selectbackground="#5a95ff")
listbox.pack(side = LEFT, fill = BOTH, padx = 2)
sbar = Scrollbar(frame1)
sbar.pack(side = RIGHT, fill = BOTH)

listbox.config(yscrollcommand=sbar.set)
sbar.config(command = listbox.yview)

#delete
delete_icon = PhotoImage(file = str(path3))
Button(root,image = delete_icon, bd = 0, command=deleteProgress).pack(side = BOTTOM, pady = 1)


root.mainloop()

