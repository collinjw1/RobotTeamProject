"""
This is my individual robot project.

Author: Jonathan Collins.
"""

import tkinter
from tkinter import ttk
import time

import mqtt_remote_method_calls as com

mqtt_client = com.MqttClient()
mqtt_client.connect_to_ev3()

def main():
    kickoff()
    program = True
    while program:
        time.sleep(0.01)


def kickoff():
    root = tkinter.Tk()
    root.title("Ready")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    user_ready = ttk.Label(main_frame, text="User ready?")
    user_ready.grid()
    kickoff_button = ttk.Button(main_frame, text="Kickoff")
    kickoff_button.grid()
    kickoff_button['command'] = lambda: send_kickoff(root)

    root.mainloop()


def send_kickoff(root):
    #client.send_message('ev3_kickoff')
    root.destroy()


def send_cut_left(root):
    #client.send_message('cut_left')
    root.destroy()

def send_cut_right(root):
    #client.send_message('cut_right')
    root.destroy()

def send_juke_left(root):
    #client.send_message('juke_left')
    root.destroy()

def send_juke_right(root):
    #client.send_message('juke_right')
    root.destroy()

def send_spin_left(root):
    #client.send_message('spin_left')
    root.destroy()

def send_spin_right(root):
    #client.send_message('spin_right')
    root.destroy()




class Reciever(object):

    def defender(self):
        droot = tkinter.Tk()
        droot.title("Ready")

        main_frame = ttk.Frame(droot, padding=20)
        main_frame.grid()

        defendermessage1 = ttk.Label(main_frame, text="Defender ahead,")
        defendermessage1.grid(row=0,column=0)
        defendermessage2 = ttk.Label(main_frame, text="pick evasive move")
        defendermessage2.grid(row=0,column=1)

        cut_left_button = ttk.Button(main_frame, text="Cut left")
        cut_left_button.grid(row=1,column=0)
        cut_left_button['command'] = lambda: send_cut_left(droot)

        cut_right_button = ttk.Button(main_frame, text="Cut right")
        cut_right_button.grid(row=1, column=1)
        cut_right_button['command'] = lambda: send_cut_right(droot)

        juke_left_button = ttk.Button(main_frame, text="Juke left")
        juke_left_button.grid(row=2, column=0)
        juke_left_button['command'] = lambda: send_juke_left(droot)

        juke_right_button = ttk.Button(main_frame, text="Juke right")
        juke_right_button.grid(row=2, column=1)
        juke_left_button['command'] = lambda: send_juke_right(droot)

        spin_left_button = ttk.Button(main_frame, text="Spin left")
        spin_left_button.grid(row=3, column=0)
        spin_left_button['command'] = lambda: send_spin_left(droot)

        spin_right_button = ttk.Button(main_frame, text="Spin right")
        spin_right_button.grid(row=3, column=1)
        spin_right_button['command'] = lambda: send_spin_right(droot)

        droot.mainloop()
