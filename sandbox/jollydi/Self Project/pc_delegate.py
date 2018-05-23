import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com

class Pc_delegate(object):
    def give_directions(self):
        root = tkinter.Tk()

        main_frame = ttk.Frame(root, padding=20, relief='raised')
        main_frame.grid()