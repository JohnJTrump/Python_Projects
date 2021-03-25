#
#
# Python:   3.9
#
# Author:   John Trump
#           
#
# Purpose:  Create GUI that will:
#               1. Allow user to browse and choose a specific folder that will contain the files to be transfered.
#               2. Allow the user to browse and choose a specific folder that will receive the files being transfered.
#               3. Button to let user initiate the file transfer.
#



from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import shutil
import os, time
import datetime
import datetime as dt
gui = Tk()
gui.geometry("400x400")
gui.title("File Transfer")


class FolderSelect(Frame): # create the widgets in tkinter
    def __init__(self,parent=None,folderDescription="",**kw):
        Frame.__init__(self,master=parent,**kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0,column=0)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0,column=1)
        self.btnFind = ttk.Button(self, text="Browse Folder",command=self.setFolderPath)
        self.btnFind.grid(row=0,column=2)
    def setFolderPath(self): # function to open file explorer
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)
       
    @property
    def folder_path(self): # function to pass selected folder in to entry box
        return self.folderPath.get()
        

def doStuff(): # function to transfer files
    now = dt.datetime.now()
    ago = now-dt.timedelta(hours=24)
    strftime = "%H:%M %m/%d/%Y"
    folder1 = directory1Select.folder_path
    folder2 = directory2Select.folder_path
    for root, dirs,files in os.walk(folder1):
        for fname in files:
            path = os.path.join(root, fname)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                print("True: ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
                shutil.move(path, folder2)
   
    
#labels for entry boxes
folderPath = StringVar()

directory1Select = FolderSelect(gui,"Transfer From")
directory1Select.grid(row=0)

directory2Select = FolderSelect(gui,"Transfer To     ")
directory2Select.grid(row=1)




c = ttk.Button(gui, text="Transfer", command=doStuff) # widget button to call the shutil function
c.grid(row=4,column=0)
gui.mainloop()
