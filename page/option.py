#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Nov 22, 2021 05:30:58 PM +07  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import page.option_support as option_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Option (root)
    option_support.init(root, top)
    root.mainloop()

w = None
def create_Option(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Option(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Option (w)
    option_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Option():
    global w
    w.destroy()
    w = None

class Option:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#ffffff'  # X11 color: 'white'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("400x150+600+300")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Option")
        top.configure(background="#ffffff")

        self.insertButton = tk.Button(top)
        self.insertButton.place(relx=0.225, rely=0.467, height=33, width=107)
        self.insertButton.configure(activebackground="#ececec")
        self.insertButton.configure(activeforeground="#000000")
        self.insertButton.configure(background="#ffffff")
        self.insertButton.configure(disabledforeground="#a3a3a3")
        self.insertButton.configure(font="-family {Segoe UI} -size 9")
        self.insertButton.configure(foreground="#000000")
        self.insertButton.configure(highlightbackground="#ffffff")
        self.insertButton.configure(highlightcolor="black")
        self.insertButton.configure(pady="0")
        self.insertButton.configure(text='''Embed To File''')
        self.insertButton.configure(command=lambda:option_support.backToMenuWindow())

        self.separateButton = tk.Button(top)
        self.separateButton.place(relx=0.525, rely=0.467, height=33, width=107)
        self.separateButton.configure(activebackground="#ececec")
        self.separateButton.configure(activeforeground="#000000")
        self.separateButton.configure(background="#ffffff")
        self.separateButton.configure(disabledforeground="#a3a3a3")
        self.separateButton.configure(font="-family {Segoe UI} -size 9")
        self.separateButton.configure(foreground="#000000")
        self.separateButton.configure(highlightbackground="#ffffff")
        self.separateButton.configure(highlightcolor="black")
        self.separateButton.configure(pady="0")
        self.separateButton.configure(text='''Separated File''')
        self.separateButton.configure(command=lambda:option_support.backToMenuWindow())

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.225, rely=0.2, height=26, width=222)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 9")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''How does file signed?''')