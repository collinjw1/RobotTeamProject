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
        ball['command'] = lambda: called_ball(self.ball, root, mqtt_client)
        strike = ttk.Button(main_frame, text='Strike')
        strike.grid(row=2, column=1)
        strike['command'] = lambda: called_strike(self.strike, root, mqtt_client)
        out = ttk.Button(main_frame, text='Out')
        out.grid(row=2, column=2)
        out['command'] = lambda: called_out(self.out, root, mqtt_client)
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
    player.pitch()


def run_bases(num, root, client):
    for k in range(num):
        client.send_message('run_bases')
    root.destroy()


def called_ball(ball, root, client):
    ball = ball + 1
    client.send_message('ball')
    root.destroy()
    return ball


def called_strike(strike, root, client):
    strike = strike + 1
    client.send_message('strike')
    root.destroy()
    return strike


def called_out(outs, root, client):
    outs = outs + 1
    client.send_message('out')
    root.destroy()
    return outs


main()
