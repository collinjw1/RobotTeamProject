"""
This is my individual robot project.

Author: Aaron Kondrat.
"""

import mqtt_remote_method_calls as com
import robot_controller as robo
import time


def main():

    robot.loop_forever()


class Sammy_Sosa(object):

    def swing_the_bat():
        robot.arm_up()
        time.sleep(3)
        robot.arm_down()
        mqtt_client.send_message('pitch')


robot = robo.Snatch3r()
pitcher = Sammy_Sosa
mqtt_client = com.MqttClient(pitcher)
mqtt_client.connect_to_pc()


main()
