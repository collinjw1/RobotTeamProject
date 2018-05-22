"""
This is my individual robot project.

Author: Jonathan Collins.
"""

import mqtt_remote_method_calls as com
import robot_controller as robo
import time


def main():
    robot.loop_forever()


class Returnman(object):

    def kickoff(self):
        self.run()

    def touchdown(self):
        time.sleep(5.0)
        robot.shutdown()

    def run(self):
        robot.forward_smart(60)
        mqtt_client.send_message('defender')

    def cut_left(self):
        robot.cut_left()
        self.run()

    def cut_right(self):
        robot.cut_right()
        self.run()

    def juke_left(self):
        robot.juke_left()
        self.run()

    def juke_right(self):
        robot.juke_right()
        self.run()

    def spin_left(self):
        robot.spin_move_left()
        self.run()

    def spin_right(self):
        robot.spin_move_right()
        self.run()


robot = robo.Snatch3r()
returnman = Returnman()
mqtt_client = com.MqttClient(returnman)
mqtt_client.connect_to_pc()
main()