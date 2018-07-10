from tkinter import *
import sys          
import random
import tkinter.messagebox as msg
from tkinter import Text ,Tk

root=Tk()
root.title("To-Do")
root.config(bg="green")
task_list=[]

def update_list():
    delete_task()
    for task in task_list:
        mylist.insert("end",task)

def delete_task():
    mylist.delete(0,END)

def add_task():
    task=entry.get("1.0",END)
    task_list.append(task)
    update_mylist()

def clear_task():
    sure=msg.askyesno("Are you really want to delete the all tasks ?")
    if sure==True:
        global task_list      
        task_list=[]
        update_mylist()

def remove():
    task = mylist.get("active")
    
    if task in task_list:
            task_list.remove(task)
            update_mylist()
    else:
        error = "There is no task in task_list(ListBox)."
        msg.showerror("Error", error)

def asc_order():
    task_list.sort()
    update_mylist()

def desc_order():
    task_list.sort()
    task_list.reverse()
    update_mylist()

def choose_random():
    task=mylist.get("active")
    if task in task_list:
       random.shuffle(task_list)
       random_task=task_list[0]
       msg.showinfo("Randomly chosen task is",random_task)
    else:
        error="There is no task in task_list(ListBox).Please add some task"
        msg.showerror("Error",error)

def num_of_task():
  
    j=0
    for i in task_list:
        j=j+1
    msg.showinfo("Number of tasks", j)

def exit():
    sys.exit()

label=Label(root,text="To-Do ",font="bold 20",width="10")
label.place(x=420,y=50)

entry=Text(root,width=37,height="2")

entry.place(x=350,y=100)

mylist=Listbox(root,width=50,height=18,bg="grey")
mylist.place(x=360,y=180)

add_item_button=Button(root,text="Add item",command=add_task,bg="lightgreen",width=15,font="5")
add_item_button.place(x=435,y=142)

clr_task_button=Button(root,text="Clear all tasks",width=15,font="5",command=clear_task,bg="red")
clr_task_button.place(x=680,y=300)

remove_button=Button(root,text="Remove",command=remove,width=15,font="5",bg="yellow")
remove_button.place(x=200,y=180)

asc_sort_button=Button(root,text="Ascending sort",command=asc_order,width=15,font="5",bg="yellow")
asc_sort_button.place(x=200,y=240)

sort_desc_button=Button(root,text="Descending sort",command=desc_order,width=15,font="5",bg="yellow")
sort_desc_button.place(x=200,y=300)

choose_random_button=Button(root,text="Choose Random",command=choose_random,width=15,font="5",bg="yellow")
choose_random_button.place(x=200,y=360)

number_of_tasks_button=Button(root,text="Number of Tasks",command=num_of_task,width=15,font="5",bg="yellow")
number_of_tasks_button.place(x=200,y=420)

exit_button=Button(root,text="Exit",font=5,command=exit,width=8,bg="red") 
exit_button.place(x=460,y=520)

root.minsize(900,600)
root.maxsize(1500,850)
root.mainloop()
