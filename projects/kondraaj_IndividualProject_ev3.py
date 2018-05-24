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

    def run_bases(self, num):
        for k in range(num):
            robot.run_bases()
            time.sleep(4)


robot = robo.Snatch3r()
batter = Sammy_Sosa()
mqtt_client = com.MqttClient(batter)
mqtt_client.connect_to_pc()


main()
