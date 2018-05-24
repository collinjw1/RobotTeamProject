import tkinter
from tkinter import ttk
import pc_delegate as pcd
import mqtt_remote_method_calls as com


def main():
    delegate = pcd.Pc_delegate()
    client = com.MqttClient(delegate)
    client.connect_to_ev3()

    root = tkinter.Tk()
    root.title('MQTT Robot Controller')
    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    speed_entry_label = ttk.Label(main_frame, text='Enter speed between 0 and 100 here:')
    speed_entry_label.grid(row=0, column=0)
    speed_entry = ttk.Entry(main_frame, width=6)
    speed_entry.grid(row=1, column=0)

    find_button = ttk.Button(main_frame, text='Find Beacon')
    find_button['command'] = lambda: send_find(client)
    find_button.grid(row=2, column=0)

    drive_button = ttk.Button(main_frame, text='Drive Until Obstacle')
    drive_button['command'] = lambda: send_drive(client, int(speed_entry.get()))
    drive_button.grid(row=3, column=0)

    quit_button = ttk.Button(main_frame, text='Quit')
    quit_button['command'] = lambda: quit_program(client)
    quit_button.grid(row=4, column=0)

    root.mainloop()


def send_find(client):
    client.send_message('get_beacon_heading')
    print('Finding beacon')


def send_drive(client, speed):
    client.send_message('go_to_beacon', [speed * 8])
    print('Driving towards beacon')


def quit_program(client):
    client.send_message('shut_off')
    client.close()
    exit()


main()
