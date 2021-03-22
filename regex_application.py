# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:23:06 2021

@author: Nathan
"""


#from tkinter import *
import tkinter.filedialog
import tkinter as tk
import re
import logging
 
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
        
        self.createLogger()
        
    def createLogger(self):
        self.logger = logging.getLogger("zoomRegEx")
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler("./zoomRegEx.log")
        fh.setLevel(logging.INFO)
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt =  "%Y-%m-%d %H:%M")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)
            
        # Indicates fresh run.
        self.logger.info('~~~~~~~~~~~~\n')
 
    def file_open(self):
        """open a file to read"""
        # optional initial directory (default is current directory)
        initial_dir = "C:\Temp"
        # the filetype mask (default is all files)
        mask = \
        [("Text and Python files","*.txt *.py *.pyw"), 
        ("HTML files","*.htm"), 
        ("All files","*.*")]        
        fin = tk.filedialog.askopenfile(mode="r", initialdir=initial_dir, filetypes=mask)
        self.setText(fin.read())
 
    def file_save(self):
        """get a filename and save the text in the editor widget"""
        # default extension is optional, here will add .txt if missing
        fout = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(self.text.get(0.0,tk.END))
        fout.write(text2save)
        fout.close()
        
    def regex(self):
        text = self.text.get("1.0", tk.END)
        text = text.split('\n') 
        newText = []
        
        for line in text:
            newLine = re.findall("^[0-9]{2}:[0-9]{2}:[0-9]{2}.*:[\s]*(.*)$", line)
            try:
                newText.append(newLine[0])
            except:
                # print("No match found")
                self.logger.warning("No match found.")
        
        # Debug
        for line in newText:
            print(line)
            
        self.setText("\n".join(newText))
        
    def setText(self, txt):
        if txt != None:
            self.text.delete(0.0, tk.END)
            self.text.insert(tk.END, txt) 
 
    def do_exit(self):
        root.destroy()
        

# logger = logging.getLogger("zoomRegEx")
# logger.setLevel(logging.INFO)
# fh = logging.FileHandler("./zoomRegEx.log")
# fh.setLevel(logging.INFO)
# ch = logging.StreamHandler()
# ch.setLevel(logging.WARNING)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt =  "%Y-%m-%d %H:%M")
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
# if not logger.handlers:
#     logger.addHandler(fh)
#     logger.addHandler(ch)

# # Indicates fresh run.
# logger.info('~~~~~~~~~~~~\n')
 
root = tk.Tk()
root.title("a very simple editor")
app = App(root)
root.mainloop()