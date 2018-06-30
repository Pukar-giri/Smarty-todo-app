from core import *
wspace=None
#===============================================================================
#creating the main window
root=Tk()
root.title("Smarty")
root.geometry("600x600+400+0")
root.resizable(0,0)
#===============================================================================
#creating the menubar and adding the main menubuttons to it
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
aboutmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="About",menu=aboutmenu)
root.config(menu=menubar)
#===============================================================================
#lets focus on the file menu and add items to it
filemenu.add_command(label="New List",accelerator="Ctrl+Shift+N",underline=0,command= lambda : NList(root,wspace))
filemenu.add_command(label="Close List",accelerator="Ctrl+W",underline=0,command=Close)
filemenu.add_command(label="Kill task",accelerator="Alt+Shift+X",underline=0,command=Check)
filemenu.add_separator()
filemenu.add_command(label="Import List",accelerator="Ctrl+Shift+I",underline=0,command=Import)
filemenu.add_command(label="Export List",accelerator="ctrl+Shift+E",underline=0,command=Export)
filemenu.add_separator()
filemenu.add_command(label="Exit",accelerator="Alt+F4",underline=0,command=Exit)
#===============================================================================
#its edit menus turn
editmenu.add_command(label="Copy Task",accelerator="Ctrl+C",underline=0,command=CpyTask)
editmenu.add_command(label="Add detail",accelerator="'+'+'D'",underline=0,command=Details)
editmenu.add_command(label="Add files",accelerator="'+'+'F'",underline=0,command=Addfile)
editmenu.add_separator()
editmenu.add_command(label="Prefrences",accelerator="Ctrl+.",underline=0,command=Pref)
#===============================================================================
#adding About menu items
aboutmenu.add_command(label="About Smarty",underline=0,command="Smarty")
aboutmenu.add_command(label="About Author",underline=0,command="Me")
#===============================================================================
#adding frame to the whole body
wspace=Frame(root,background="sky blue")
wspace.pack(expand="yes",side="right",fill="both")
#===============================================================================
#showing list in the Frame
lstspace=showlist(wspace)
#===============================================================================
#making right click context menu for body
spacemenu=Menu(lstspace,tearoff=0)
spacemenu.add_command(label="Add List",accelerator="Ctrl+Shift+N",underline=0,command=lambda : NList(root,wspace))
spacemenu.add_command(label="Import List",accelerator="Ctrl+Shift+I",underline=0,command=Import)
spacemenu.add_separator()
spacemenu.add_command(label="Prefrences",accelerator="Ctrl+.",underline=0,command=Pref)
#===============================================================================
#adding Popup menu for body
def spacePop(event):
    spacemenu.tk_popup(event.x_root,event.y_root)
lstspace.bind('<Button-3>',spacePop)
#===============================================================================
#mainloop for the gui program
root.mainloop()
