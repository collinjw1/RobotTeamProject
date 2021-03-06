"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called. That way it's a generic action that could be used in any task
"""

import ev3dev.ev3 as ev3
import math
import time
import mqtt_remote_method_calls as com


class Snatch3r(object):
    """Commands for the Snatch3r robot that might be useful in many different programs."""

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sens = ev3.TouchSensor
        self.running = None
        self.ir_sensor = ev3.InfraredSensor()
        self.bs = ev3.BeaconSeeker(sensor=None, channel=1)
        self.blocked = False
        self.at_beacon = False
        self.color_sensor = ev3.ColorSensor()

        assert self.ir_sensor.connected
        assert self.left_motor.connected
        assert self.right_motor.connected
        assert self.arm_motor.connected

    def forward(self, inches, speed=100, stop_action='brake'):
        gogojuice = speed * 8
        disd = (inches / (1.3 * math.pi)) * 360
        self.left_motor.run_to_rel_pos(position_sp=disd, speed_sp=gogojuice, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=disd, speed_sp=gogojuice, stop_action=stop_action)
        self.left_motor.wait_while("running")
        self.right_motor.wait_while("running")

    def forward_smart(self, dist, speed=800):
        self.drive(speed, speed)
        while True:
            if self.ir_sensor.proximity < dist:
                break
            time.sleep(0.01)
        self.stop()

    def drive(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=left_speed)
        self.right_motor.run_forever(speed_sp=right_speed)

    def drive_back(self, left_speed, right_speed):
        self.left_motor.run_forever(speed_sp=-left_speed)
        self.right_motor.run_forever(speed_sp=-right_speed)

    def left_turn(self, speed):
        self.right_motor.run_forever(speed_sp=speed)

    def right_turn(self, speed):
        self.left_motor.run_forever(speed_sp=speed)

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()
        self.arm_motor.stop()

    def backward(self, inches, speed=100, stop_action='brake'):
        self.forward(-inches, speed, stop_action)

    def spin_right(self, degrees, speed, stop_action='brake'):
        radians = math.pi * (degrees / 180)
        robot_speed = abs(4 * ((speed * 8) / 360))
        omega_robot = robot_speed / 2.8125
        rotate_time = radians / omega_robot
        wheel_degrees = (speed * 8) * rotate_time

        self.left_motor.run_to_rel_pos(position_sp=-wheel_degrees, speed_sp=-speed * 8)
        self.right_motor.run_to_rel_pos(position_sp=wheel_degrees, speed_sp=speed * 8)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.left_motor.stop(stop_action=stop_action)
        self.right_motor.stop(stop_action=stop_action)
        ev3.Sound.beep().wait()

    def spin_left(self, degrees, speed, stop_action='brake'):
        self.spin_right(degrees, -speed, stop_action)

    def turn_right(self, degrees, speed, stop_action='brake'):
        deg = 10 * degrees
        self.right_motor.run_to_rel_pos(position_sp=deg, speed_sp=speed * 8)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.stop(stop_action=stop_action)
        ev3.Sound.beep().wait()

    def turn_left(self, degrees, speed, stop_action='brake'):
        self.turn_right(-degrees, speed, stop_action)

    def arm_up(self, speed=900):
        self.arm_motor.run_forever(speed_sp=speed)
        while True:
            if self.touch_sens.is_pressed:
                break

    def arm_down(self, speed=900):
        self.arm_motor.run_forever(speed_sp=-speed)

    def loop_forever(self):
        self.running = True
        while self.running:
            time.sleep(0.01)

    def shutdown(self):
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        self.left_motor.stop()
        self.right_motor.stop()
        self.arm_motor.stop()
        self.running = False

    ##############################################################
    #  For Chio's Project
    ##############################################################

    def spin_move_right(self):
        self.spin_right(270, 100, stop_action='brake')
        self.forward(20, 100, stop_action='brake')
        self.turn_right(95, 100, stop_action='brake')

    def spin_move_left(self):
        self.spin_left(270, 100, stop_action='brake')
        self.forward(20, 100, stop_action='brake')
        self.turn_left(85, 100, stop_action='brake')

    def juke_right(self):
        self.spin_right(20, 100, stop_action='brake')
        self.spin_left(120, 100, stop_action='brake')
        self.forward(20, 100, stop_action='brake')
        self.turn_right(90, 100, stop_action='brake')

    def juke_left(self):
        self.spin_left(20, 100, stop_action='brake')
        self.spin_right(120, 100, stop_action='brake')
        self.forward(20, 100, stop_action='brake')
        self.turn_left(80, 100, stop_action='brake')

    def cut_right(self):
        self.spin_left(90, 100, stop_action='brake')
        self.forward(20, 100, stop_action='brake')
        self.turn_right(95, 100, stop_action='brake')

    def cut_left(self):
        self.spin_right(90, 100, stop_action='brake')
        self.forward(20, 100, stop_action='brake')
        self.turn_left(85, 100, stop_action='brake')


####################################################################
# For Isaiah's Project
####################################################################

    def spin_forever(self, speed=400):
        self.left_motor.run_forever(speed_sp=speed)
        self.right_motor.run_forever(speed_sp=-speed)

    def get_beacon_heading(self):
        self.spin_forever()
        while True:
            if self.bs.heading == 0:
                self.stop()
                dist = self.bs.distance
                break
        self.spin_forever()
        time.sleep(2)
        self.stop()
        if self.bs.distance < dist:
            while True:
                self.spin_forever()
                if self.bs.heading == 0:
                    self.stop()
                    print('Beacon found')
                    break
        else:
            self.spin_forever(-400)
            time.sleep(2)
            self.stop()
            print('Beacon found')

    def drive_until_obstacle(self, speed):
        self.drive(speed, speed)
        while True:
            if self.bs.distance < 2:
                self.stop()
                print('Beacon found')
                self.at_beacon = True
                break

            if self.ir_sensor.proximity < 5:
                self.stop()
                self.blocked = True
                print('Obstacle found')
                break

    def ask_for_directions(self, client):
        print('Asking for directions')
        client.send_message('give_directions')
        self.blocked = False

    def adjust_left(self):
        print('Adjusting path')
        self.spin_forever(-300)
        time.sleep(3)
        self.stop()
        self.drive(400, 400)
        time.sleep(2)
        self.stop()

    def adjust_right(self):
        print('Adjusting path')
        self.spin_forever()
        time.sleep(3)
        self.stop()
        self.drive(400, 400)
        time.sleep(2.5)
        self.stop()

    def shut_off(self):
        print('Quitting')
        self.stop()
        self.arm_down()
        self.running = False

    def loop(self, client):
        self.running = True
        while self.running:
            # if self.blocked:
            #     self.ask_for_directions(client)
            #     continue
            # if self.at_beacon:
            #     self.arm_up()
            #     print('Beacon picked up!')
            #     self.at_beacon = False
            time.sleep(0.05)

    def go_to_beacon(self, speed, stop_action='brake'):
        # cm = self.bs.distance * (6 / 7)
        inches = self.bs.distance * (7 / 10)
        theta = (inches / math.pi) * 360
        self.left_motor.run_to_rel_pos(position_sp=theta, speed_sp=speed, stop_action=stop_action)
        self.right_motor.run_to_rel_pos(position_sp=theta, speed_sp=speed, stop_action=stop_action)
        self.left_motor.wait_while('running')
        self.at_beacon = True
        self.arm_up()


####################################################################
# For Aaron's Project
####################################################################

    def run_bases(self):
        self.drive(600, 600)
        while True:
            if self.color_sensor.reflected_light_intensity >= 85:
                self.stop()
                self.turn_right(90, 50)

    def swing_the_bat(self):
        self.arm_up()
        self.arm_down()

