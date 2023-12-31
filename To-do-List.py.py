from tkinter import *
root = Tk()
root.title('To-Do List')
root.geometry('320x403')
root.resizable(0, 0)
root.config(bg="pink")

Label(root, text='MY To Do List', bg='Pink', font=("Comic Sans MS", 15), wraplength=300).place(x=35, y=0)
tasks = Listbox(root, selectbackground='Gold', bg='light blue', font=('Helvetica', 13), height=14, width=27)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=262, y=52, height=233)
tasks.place(x=35, y=50)
with open('mytasks.txt', 'r+') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()

 
new_item_entry = Entry(root, width=36)
new_item_entry.place(x=34, y=311)

add_btn = Button(root, text='Add Item', bg='light blue', width=11, font=('Arial', 13),
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=44, y=351)

delete_btn = Button(root, text='Delete Item', bg='light blue', width=11, font=('Arial', 13),
                 command=lambda: delete_item(tasks))
delete_btn.place(x=151, y=351)

root.update()
root.mainloop() 
