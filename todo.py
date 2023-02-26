import tkinter
from tkcalendar import Calendar
from tkinter import messagebox
import json

raiz = tkinter.Tk()
raiz.geometry('800x800')
raiz.title('ToDo App')

def GetData():
    with open(r'ToDoApp\tasks.txt', 'r') as saveFile:
        data = saveFile.readlines()
        for i in data:
            i = i[1:-2]
            if i != '':
                i = i.split(',')
                i = [x.replace('\'', "") for x in i]
                i = [x.replace('  ', " ") for x in i]
                Tasks.insert(0,"\n".join(i))

Title = tkinter.Label(text='ToDo', font=('Calibri', 50))
Title.pack()


class Task:
    def __init__(self, title, desc, date):
        self.title = title
        self.desc = desc
        self.date = date
    def GetText(self):
        return f'Title: {self.title}\n Desc: {self.desc}\n Due: {self.date}'


calendar = Calendar(raiz, selectmode="day", year=2022, month=1, date=1)
calendar.pack()


def fetchDate():
    selected_date = calendar.get_date()
    return selected_date

label = tkinter.Label(raiz, text  ='Title: ')
Title = tkinter.Entry(raiz)
label.pack()
Title.pack()

label = tkinter.Label(raiz, text  ='Description: ')
Description = tkinter.Entry(raiz,  width=50)
label.pack()
Description.pack()


def createTask():
    titulo = Title.get()
    desc = Description.get()
    Date = calendar.get_date()
    if all([titulo, desc, Date]):
        NewTask = Task(title=titulo, desc =desc, date = Date)
        Tasks.insert(0, NewTask.GetText())
    else: messagebox.showinfo('Alert', 'Task Data cannot be empty')


submit = tkinter.Button(raiz, text  = 'create Task', command = createTask)
submit.pack()

Tasks = tkinter.Listbox(raiz, width=100, height=20)
GetData()

scrollbar = tkinter.Scrollbar(raiz, orient=tkinter.VERTICAL, command = Tasks.yview)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
Tasks.config(yscrollcommand=scrollbar.set)


Tasks.pack()
def DeleteTask():
    current = Tasks.curselection()
    try:
        Tasks.delete(current)
    except: pass
    with open(r'ToDoApp\tasks.txt', 'r+') as saveFile:
        saveFile.truncate(0)
        SaveTaks()

Delete =tkinter.Button(text = 'DeleteTask', command = DeleteTask)
Delete.pack()

def SaveTaks():
    with open(r'ToDoApp\tasks.txt', 'r+') as saveFile:
        for item in Tasks.get(0, tkinter.END):
            item =  item.split('\n')
            saveFile.write(str(item) + "\n")

SaveButton = tkinter.Button(text = 'Save all', command = SaveTaks)
SaveButton.pack()

raiz.mainloop()