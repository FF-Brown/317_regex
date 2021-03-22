# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:23:06 2021

@author: Nathan
"""


#from tkinter import *
import tkinter.filedialog
import tkinter as tk
import re
#from tkfiledialog import *
 
class App(object):
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        self.text = tk.Text()
        self.text.pack()
 
        menu = tk.Menu(master)
        root.config(menu=menu)
        # file menu
        filemenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="Save", command=self.file_save)   
        filemenu.add_command(label="Regex", command=self.regex)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.do_exit)
 
    def file_open(self):
        """open a file to read"""
        # optional initial directory (default is current directory)
        initial_dir = "C:\Temp"
        # the filetype mask (default is all files)
        mask = \
        [("Text and Python files","*.txt *.py *.pyw"), 
        ("HTML files","*.htm"), 
        ("All files","*.*")]        
        #fin = tk.filedialog.askopenfile(initialdir=initial_dir, filetypes=mask, mode='r')
        fin = tk.filedialog.askopenfile(mode="r", initialdir=initial_dir, filetypes=mask)
        text = fin.read()
        if text != None:
            self.text.delete(0.0, tk.END)
            self.text.insert(tk.END,text)
 
    def file_save(self):
        """get a filename and save the text in the editor widget"""
        # default extension is optional, here will add .txt if missing
        fout = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(self.text.get(0.0,tk.END))
        fout.write(text2save)
        fout.close()
        
    def regex(self):
        pass
        
 
    def do_exit(self):
        root.destroy()
 
root = tk.Tk()
root.title("a very simple editor")
app = App(root)
root.mainloop()