"""
This is my individual robot project.

Author: Aaron Kondrat.
"""

import mqtt_remote_method_calls as com
import robot_controller as robo


def main():

    swing_the_bat()


def swing_the_bat():
    robot.arm_up()
    robot.arm_down()
    mqtt_client.send_message('pitch')


robot = robo.Snatch3r()
mqtt_client = com.MqttClient(robot)
mqtt_client.connect_to_pc()
robot.loop(mqtt_client)


main()
