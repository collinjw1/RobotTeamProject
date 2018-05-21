"""
This is my individual robot project.

Author: Jonathan Collins.
"""

import tkinter
from tkinter import ttk

import mqtt_remote_method_calls as com
import robot_controller as robo

robot=robo.Snatch3r()
mqtt_client = com.MqttClient(robot)
mqtt_client.connect_to_pc()

def main():
    robot.loop_forever()


def touchdown():



def run():
    robot.forward_smart(15)
    mqtt_client.send_message('command')


#client gives to delegate(snatcher)
#delegate==class


def cut_left():
    robot.cut_left()
    run()
#cut/spin/juke/TD






""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
main()
