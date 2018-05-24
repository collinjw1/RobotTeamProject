"""
This is my individual robot project.

Author: Aaron Kondrat.
"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time


class BabeRuth(object):

    def pitch(self):
        root = tkinter.Tk()
        root.title("Batter Up")

        main_frame = ttk.Frame(root, padding=20)
        main_frame.grid()

        single = ttk.Button(main_frame, text='Single')
        single.grid(row=3, column=0)
        single['command'] = lambda: run_bases(1, root, mqtt_client)
        double = ttk.Button(main_frame, text='Double')
        double.grid(row=3, column=1)
        double['command'] = lambda: run_bases(2, root, mqtt_client)
        triple = ttk.Button(main_frame, text='Triple')
        triple.grid(row=3, column=2)
        triple['command'] = lambda: run_bases(3, root, mqtt_client)
        home_run = ttk.Button(main_frame, text='Homerun')
        home_run.grid(row=4, column=1)
        home_run['command'] = lambda: run_bases(4, root, mqtt_client)

        root.mainloop()


player = BabeRuth()
mqtt_client = com.MqttClient(player)
mqtt_client.connect_to_ev3()


def main():
    up_to_bat()


def up_to_bat():
    root = tkinter.Tk()
    root.title("Batter Up")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()

    batter_up = ttk.Label(main_frame, text='Batter Up')
    batter_up.grid()
    swing = ttk.Button(main_frame, text='Swing')
    swing.grid()
    swing['command'] = lambda: swing_the_bat(root, mqtt_client)


def run_bases(num, root, client):
    for k in range(num):
        client.send_message('run_bases')
    root.destroy()


def swing_the_bat(root, client):
    client.send_message('swing_the_bat')
    root.destroy()


main()
