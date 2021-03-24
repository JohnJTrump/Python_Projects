#
#
# Python:   3.9
#
# Author:   John Trump
#           
#
# Purpose:  Create a Web Page Generator:
#               1. Create GUI that allows a user to input text and initiate a web page with the text they typed.
#               2. Generates a web page that sets the users input as the body text for the web page.
#               3. Opens the generated web page in the browser.
#





#importing all modules for use
import tkinter
from tkinter import *
from tkinter import messagebox
import webbrowser



class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__ (self, master, *args, **kwargs)

        self.master = master
        self.master.geometry('{}x{}'.format(500, 200)) # Establish the ititial size of the resizable window which will hold the widgets
        self.master.title('Basic Web Page Generator')  # Title on top bar of window

        self.varSource = StringVar() # Create variable to hold user inputed text
        


        self.txtEntryBX = Entry(self.master,width=56, textvariable=self.varSource) # Entry box with size, for user inputed text pushing text to variable 
        self.txtEntryBX.grid(row=1, column=1, rowspan=2, columnspan=2, padx=(10,0), pady=(30,0)) # Painting the Entry box position in window

        

        self.btn_Create = Button(self.master,width=12,height=1,text='Try it!',command=self.creator) # Button with size to initiate the web page creation calling the creator function
        self.btn_Create.grid(row=1, column=0, padx=(10,20), pady=(35,5), sticky=W) # Painting the Buttons position in window

        

        self.btn_close = Button(self.master,width=12,height=2,text='Close Program', command=self.cancel) # Button with size to close program by calling the cancel function
        self.btn_close.grid(row=3, column=2, padx=(10,0), pady=(10,10), sticky=E) # Painting the Buttons position in window




    def cancel(self): # Defining the function
        self.master.destroy() # calling the built in destroy function to close program



    def creator(self): # Defining the function
        f= open('index.html','w')    # create variable to call seperate page for use
        text = self.varSource.get()     # create variable to call different variable for use
        message = "<html><head></head><body><h1>%s</h1></body></html>" % text   # create variable to combine html with user input text
        f.write(message)   # write the completed message variable to the seperate file being held in f variable 
        f.close()    # close and save the completed file?????
        webbrowser.open_new_tab('index.html') #open the completed file in a new tab in the browser






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
