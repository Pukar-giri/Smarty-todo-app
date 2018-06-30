
from list import *
#===============================================================================
#commands for file menu implemented
def NList(root,wspace):
    dilog=Toplevel(root)
    dilog.title("New List")
    dilog.transient(root)
    dilog.geometry("400x150+"+str(int(root.winfo_x())+100)+"+"+str(int(root.winfo_y())+225))
    dilog.grab_set()
    dilog.resizable(0,0)
    namelabel=Label(dilog,text="Name:")
    name=Entry(dilog,width="50")
    reln=["General","Programming","Study","College Syllabus","Grocery","Important"]
    master=Pmw.ComboBox(dilog,label_text="Related to:",labelpos="wn",listbox_width=24,dropdown=1,scrolledlist_items=reln)
    master.selectitem(reln[0])
    imp=IntVar()
    important=Checkbutton(dilog,text="Important",variable=imp)
    tmd=IntVar()
    timed=Checkbutton(dilog,text="Timed",variable=tmd)
    addbtn=Button(dilog,text="Add",command=lambda : newlist(wspace,dilog,name.get(),master.get(0,None),imp.get(),tmd.get()))
    namelabel.grid(padx=5,pady=5,ipadx=2,row=0,column=0)
    name.grid(row=0,column=1,padx=5,pady=5,ipadx=2)
    master.grid(row=1,column=0,padx=5,pady=5,columnspan=5)
    important.grid(row=2,column=0,padx=5,pady=5,sticky="w",columnspan=2)
    timed.grid(row=2,column=1,padx=5,pady=5,sticky="e",columnspan=2)
    addbtn.grid(row=3,column=1,sticky="e",padx=5,pady=5,ipadx=3,ipady=3)
    name.focus()
    return 0
def Close():
    return 0

def Check():
    return 0

def Import():
    return 0

def Export():
    return 0

def Exit ():
    return 0

#===============================================================================
#commands for the edit menus
def CpyTask():
    return 0

def Details():
    return 0

def Addfile():
    return 0

def Pref():
    return 0

#===============================================================================
#commands for About menu
def Smarty():
    return 0

def Me():
    return 0
#===============================================================================
