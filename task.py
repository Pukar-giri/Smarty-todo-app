from tkinter import *
import json
import Pmw
global n
def readfile():
    try:
        with open("data.clx","r") as infile:
            data= json.load(infile)
        if data : return data
        else : return {}
    except:
        print("error on reading file")
        return {}


def Check(mkey,tkey):
    data=readfile()
    data[mkey]["tasks"][tkey]["done"]= not data[mkey]["tasks"][tkey]["done"]
    with open("data.clx","w") as outfile:
        json.dump(data,outfile)
    return 0

def showtask(wspace,listspace,tasks,key):
    global taskspace
    # scrolledspace=Pmw.ScrolledFrame(wspace)
    # taskspace=scrolledspace.interior()
    # taskspace.config(background="orange")
    taskspace=Frame(wspace,background="orange")
    taskspace.pack(expand="yes",side="right",fill="both")
    #===========================================================================
    #context menu for task pane:
    taskmenu=Menu(taskspace,tearoff=0)
    taskmenu.add_command(label="Add Task",accelerator="Ctrl+Shift+N",underline=0,command=lambda : NTask(key))
    #taskmenu.add_command(label="Import List",accelerator="Ctrl+Shift+I",underline=0,command=Import)
    taskmenu.add_separator()
    #taskmenu.add_command(label="Prefrences",accelerator="Ctrl+.",underline=0,command=Pref)
    taskspace.bind('<Button-3>',lambda event :taskmenu.tk_popup(event.x_root,event.y_root))
    global chkbuttons
    chkbuttons=[]
    for tkey,value in tasks.items():
        chkbutton=chkbtn(tasks,tkey,key)
        chkbutton.pack()
        chkbuttons.append(chkbutton)
    listspace.destroy()

def NTask(key):
    dilog=Toplevel()
    dilog.title("New task")
    # dilog.transient(root)
    #dilog.geometry("400x150+"+str(int(root.winfo_x())+100)+"+"+str(int(root.winfo_y())+225))
    dilog.grab_set()
    dilog.resizable(0,0)
    namelabel=Label(dilog,text="Task:")
    name=Entry(dilog,width="50")
    imp=IntVar()
    important=Checkbutton(dilog,text="Important",variable=imp)
    tmd=IntVar()
    timed=Checkbutton(dilog,text="Timed",variable=tmd)
    addbtn=Button(dilog,text="Add",command=lambda : newtask(dilog,name.get(),imp.get(),tmd.get(),key))
    namelabel.grid(padx=5,pady=5,ipadx=2,row=0,column=0)
    name.grid(row=0,column=1,padx=5,pady=5,ipadx=2)
    important.grid(row=2,column=0,padx=5,pady=5,sticky="w",columnspan=2)
    timed.grid(row=2,column=1,padx=5,pady=5,sticky="e",columnspan=2)
    addbtn.grid(row=3,column=1,sticky="e",padx=5,pady=5,ipadx=3,ipady=3)
    name.focus()
    return 0

def newtask(dilog,name,important,timed,key):
        dilog.destroy()
        whole=readfile()
        data=whole[key]["tasks"]
        if name == "" :
            messagebox.showerror("Error on adding task","The Task field cannot be empty please complete it and try again")
            return 0
        ndata={str(len(data)):{"name":name,"done": False ,"important":important,"timed":timed,"details":{}}}
        data.update(ndata)
        whole[key]["tasks"]=data
        with open("data.clx","w") as outfile:
            json.dump(whole,outfile)
        chk=IntVar()
        chkbutton=chkbtn(data,str(len(data)-1),key)
        chkbutton.pack()
        return 0
def chkbtn(tasks,tkey,mkey):
    chk=Checkbutton(taskspace,text=tasks[tkey]["name"],background="orange",width=75,anchor="nw",relief="raised")
    if tasks[tkey]["done"]: chk.toggle()
    chk.bind('<Button-1>',lambda events :Check(mkey,tkey))
    return chk
def movedown():
    chkbuttons[n].pack_forget()
    n+=1
