from task import *
from tkinter import messagebox

import math
pad=18

def showlist(wspace):
    global listspace
    listspace=Frame(wspace,background="cyan")
    data=readfile()
    tiles=[]
    i=0
    for key,value in data.items():
        tile=Tile(wspace,listspace,data[key],key)
        tiles.append(tile)
    for x,tile in enumerate(tiles):
        row=math.floor(x/4)
        column=math.floor(x%4)
        tile.grid(row=row,column=column,padx=pad,pady=pad)
    listspace.pack(expand="yes",side="right",fill="both")
    return listspace


def newlist(wspace,dilog,name,relatedTo,important,timed):
    dilog.destroy()
    if name=="":
        messagebox.showerror("Error on adding task","The name field cannot be empty please complete it and try again")
        return 0
    data=readfile()
    ndata={str(len(data)):{"name":name,"related":relatedTo,"important":important,"timed":timed,"details":{},"tasks":{}}}
    data.update(ndata)
    with open("data.clx","w") as outfile:
        json.dump(data,outfile)
    tile=Tile(wspace,listspace,data[str(len(data)-1)],str(len(data)-1))
    x=len(data)-1
    row=math.floor(x/4)
    column=math.floor(x%4)
    tile.grid(row=row,column=column,padx=pad,pady=pad)
        # listspace.pack(expand="yes",side="right",fill="both")
    return 0

def Tile(wspace,listspace,data,key):
    canvas=Canvas(listspace,height=100,width=100,background="red",relief="raised",bd=5)
    canvas.create_text(50,50,text=data["name"])
    canvas.bind('<Button-1>',lambda event : showtask(wspace,listspace,data["tasks"],key))
    return canvas
