import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com


class Pc_delegate(object):
    def __init__(self):
        self.client = com.MqttClient()
        self.client.connect_to_ev3()
        self.root = tkinter.Tk()

    def give_directions(self):

        main_frame = ttk.Frame(self.root, padding=20, relief='raised')
        main_frame.grid()

        left_button = ttk.Button(main_frame, text='Adjust left')
        left_button['command'] = lambda: self.send_adjust_left(self.client)
        left_button.grid(row=0, column=0)

        right_button = ttk.Button(main_frame, text='Adjust right')
        right_button['command'] = lambda: self.send_adjust_right(self.client)
        right_button.grid(row=0, column=1)

        close_button = ttk.Button(main_frame, text='Close')
        close_button['command'] = lambda: self.close_window()

        self.root.mainloop()

    def send_adjust_left(self, client):
        print('Directions given')
        client.send_message('adjust_left')

    def send_adjust_right(self, client):
        print('Directions given')
        client.send_message('adjust_right')

    def close_window(self):
        self.client.close()
        self.root.destroy()