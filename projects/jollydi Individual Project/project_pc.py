import tkinter
from tkinter import ttk
import pc_delegate as pcd
import mqtt_remote_method_calls as com

def main():
    delegate = pcd.Pc_delegate()
    client = com.MqttClient()
    client.connect_to_ev3(delegate)
