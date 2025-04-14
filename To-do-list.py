import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry("400x600")

task_list=[]

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)




def deleteTask():

    global task_list

    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)


def openTaskFile():

    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END, task)


    except:
        file=open("tasklist.txt","w")
        file.close()



heading=Label(root, text="All TASKS", font=("Arial bold", 20,)).pack()


frame= Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=140)

task=StringVar()
task_entry=Entry(frame, width=18, font="Arial 20",bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

button=Button(frame,text="ADD", font="arial 20 bold", width=6, bg="darkblue", fg="white", bd=0, command=addTask)
button.place(x=300, y=0)


frame1=Frame(root, bd=3, width=700, height=280, bg="black")
frame1.pack(pady=(160,0))

listbox =  Listbox(frame1,font=('arial', 12), width=40, height=16, bg="darkblue" ,fg="white",cursor="hand2", selectbackground="skyblue")
listbox.pack(side=LEFT, fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)


openTaskFile()

frame2=Frame(root, width=400, height=50, bg="white", bd=0)
frame2.place(x=140, y=520)
Button(frame2, text="Delete", font="arial 20 bold", width=6, bg="darkblue", fg="white", command=deleteTask).pack()




root.mainloop()