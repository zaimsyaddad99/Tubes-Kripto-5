#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Nov 22, 2021 05:22:54 PM +07  platform: Windows NT

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

import page.option as option
import start
from rsa import save_key_pub, save_key_pri, findPrivate

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def setTkVariable():
    global labelStatusVar
    labelStatusVar = tk.StringVar()
    labelStatusVar.set(start.status)

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def openOptionWindow(char):
    start.SorV = char
    destroy_window()
    option.vp_start_gui()

def generatePubKey():
    save_key_pub(start.e, start.p*start.q)
    labelStatusVar.set("Status: Public Key generated to './key/rsa.pub'")

def generatePriKey():
    save_key_pri(start.p*start.q, findPrivate(start.e, (start.p-1)*(start.q-1)))
    labelStatusVar.set("Status: Private Key generated to './key/rsa.pri'")