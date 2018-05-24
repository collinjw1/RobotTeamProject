"""
This is my individual robot project.

Author: Aaron Kondrat.
"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


class BabeRuth(object):

    def __init__(self):
        self.ball = 0
        self.strike = 0
        self.out = 0
        self.base_one = 'X'
        self.base_two = 'X'
        self.base_three = 'X'
        self.home_plate = 'X'

    def called_ball(self, root):
        self.ball = self.ball + 1
        if self.ball == 4:
            self.ball = 0
            self.strike = 0
            run_bases(1, root, mqtt_client)

    def called_strike(self):
        self.strike = self.strike + 1
        if self.strike == 3:
            self.strike = 0
            self.ball = 0
            self.out = self.out + 1

    def called_out(self):
        self.out = self.out + 1
        if self.out == 3:
            game_over(root, client)

    def pitch(self):
        root = tkinter.Tk()
        root.title("Batter Up")

        main_frame = ttk.Frame(root, padding=20)
        main_frame.grid()

        ball_counter = ttk.Label(main_frame, text="Ball")
        ball_counter.grid(row=0, column=0)
        strike_counter = ttk.Label(main_frame, text="Strike")
        strike_counter.grid(row=0, column=1)
        out_counter = ttk.Label(main_frame, text="Out")
        out_counter.grid(row=0, column=2)

        number_balls = ttk.Label(main_frame, text=self.ball)
        number_balls.grid(row=1, column=0)
        number_strikes = ttk.Label(main_frame, text=self.strike)
        number_strikes.grid(row=1, column=1)
        number_outs = ttk.Label(main_frame, text=self.out)
        number_outs.grid(row=1, column=2)

        ball = ttk.Button(main_frame, text='Ball')
        ball.grid(row=2, column=0)
        ball['command'] = lambda: called_ball(root)
        strike = ttk.Button(main_frame, text='Strike')
        strike.grid(row=2, column=1)
        strike['command'] = lambda: called_strike()
        out = ttk.Button(main_frame, text='Out')
        out.grid(row=2, column=2)
        out['command'] = lambda: called_out()
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

        first_base = ttk.Label(main_frame, text=self.base_one)
        first_base.grid(row=2, column=6)
        second_base = ttk.Label(main_frame, text=self.base_two)
        second_base.grid(row=1, column=5)
        third_base = ttk.Label(main_frame, text=self.base_three)
        third_base.grid(row=2, column=4)
        homeplate = ttk.Label(main_frame, text=self.home_plate)
        homeplate.grid(row=3, column=5)

        root.mainloop()


def run_bases(num, root, client):
    for k in range(num):
        client.send_message('run_bases')
    root.destroy()


def game_over(root, client):
    client.send_message('game')
    root.destroy()


def main():
    player = BabeRuth()
    mqtt_client = com.MqttClient(player)
    mqtt_client.connect_to_ev3()


main()

