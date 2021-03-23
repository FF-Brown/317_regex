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
        """Initializes logger object for the app."""
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
        self.logger.info('\n~~~~~~~~~~~~')
 
    def file_open(self):
        """Open a file and read its contents into the editor."""        
        try:
            filename = tk.filedialog.askopenfilename(title="Choose a Zoom chat file to open.", filetypes = [("Text Files", "*.txt"), ("All files", "*.*")])
            with open(filename, "r") as inFile:
                try:
                    self.setText(inFile.read().encode("cp1252").decode("utf-8"))
                except:
                    self.setText(inFile.read())
        except FileNotFoundError:
            self.logger.info("Tk exception caught: User chose not to open file.")

    def file_save(self):
        """Get a filename and save editor text to that file."""
        
        try:
            filename = tk.filedialog.asksaveasfilename(title="Save", filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
            with open(filename, "wb") as outFile:
                text2save = str(self.text.get(0.0, tk.END))
                outFile.write(text2save.encode("utf-8"))
        except FileNotFoundError:
            self.logger.info("Tk exception caught: User chose not to save file.")
        
    def regex(self):
        """
        Strip all text from a Zoom chat document except the messages themselves.
        Writes the results to the editor window so they can be saved.

        Returns
        -------
        None.

        """
        text = self.text.get("1.0", tk.END)
        text = text.split('\n') 
        newText = []
        
        for line in text:
            newLine = re.findall("^[0-9]{2}:[0-9]{2}:[0-9]{2}.*:[\s]*(.*)$", line)
            try:
                newText.append(newLine[0])
            except:
                self.logger.info("No match found.")
            
        self.setText("\n".join(newText))
        
    def setText(self, txt):
        """Writes text to the editor window."""
        if txt != None:
            self.text.delete(0.0, tk.END)
            self.text.insert(tk.END, txt) 
 
    def do_exit(self):
        root.destroy()
        
root = tk.Tk()
root.title("317 Zoom Chat Editor")
app = App(root)
root.mainloop()