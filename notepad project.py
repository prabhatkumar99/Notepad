from tkinter import Tk,scrolledtext,Menu,filedialog,END,messagebox
notepad=Tk(className="notepad")
def saveFile():
    file=filedialog.asksaveasfile(mode='w')

    if file != None:
        data=textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()
def exitnotepad():
    if messagebox.askyesno("Quit","Are you sure you want to quit?"):
        notepad.destroy()
    
menu=Menu(notepad)
notepad.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...') 
filemenu.add_command(label='Save',command=saveFile)
filemenu.add_command(label='Save as...')
filemenu.add_separator()
filemenu.add_command(label='Page Setup...')
filemenu.add_command(label='Page Setup...')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=exitnotepad)
Editmenu=Menu(menu)
menu.add_cascade(label='Edit',menu=Editmenu)
Editmenu.add_command(label='Undu')
Editmenu.add_separator()
Editmenu.add_command(label='Cut')
Editmenu.add_command(label='Copy')
Editmenu.add_command(label='Paste')
Editmenu.add_command(label='Delete')
Editmenu.add_separator()
Editmenu.add_command(label='Find')
Editmenu.add_command(label='Find Text...')
Editmenu.add_command(label='Replace goto...')
Editmenu.add_command(label='Go To...')
Editmenu.add_separator()
Editmenu.add_command(label='Select All')
Editmenu.add_command(label='Time/Date')
Formetmenu=Menu(menu)
menu.add_cascade(label='Formet',menu=Formetmenu)
Formetmenu.add_command(label='Word Wrap')
Formetmenu.add_command(label='Font...')
Viewmenu=Menu(menu)
menu.add_cascade(label='View',menu=Viewmenu)
Viewmenu.add_command(label='Status Bar')
Helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=Helpmenu)
Helpmenu.add_command(label='View Help')
Helpmenu.add_separator()
Helpmenu.add_command(label='About Notepad')
textArea=scrolledtext.ScrolledText(notepad,width=100,height=80)
textArea.pack()
notepad.mainloop()
