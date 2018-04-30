"""
Functions for SPINNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Isaiah Jolly.
"""  # Isaiah Jolly: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement spin_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for spin_left_by_time.
#   Then repeat for spin_left_by_encoders.
#   Then repeat for the spin_right functions.


import ev3dev.ev3 as ev3
import time
import math


def test_spin_left_spin_right():
    """
    Tests the spin_left and spin_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs spin_left_by_time.
      3. Same as #2, but runs spin_left_by_encoders.
      4. Same as #1, 2, 3, but tests the spin_right functions.
    """
    # Testing spin_left_seconds:

    print('** Testing of spin_left_seconds is starting **')
    print()

    while True:
        seconds = int(input('Enter a number of seconds to travel for: '))
        if seconds == 0:
            break
        speed = int(input('Enter a speed for the wheels to spin at between 0 and 100: '))
        stop_action = str(input('Enter a stop action (brake, coast, or hold): '))

        if stop_action == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stop_action == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        else:
            stop_action = ev3.Motor.STOP_ACTION_HOLD

        spin_left_seconds(seconds, speed, stop_action)

    # Testing spin_left_by_time:

    print()
    print('** Testing of spin_left_by_time is starting **')
    print()

    while True:
        degrees = int(input('Enter a number of degrees for the robot to spin: '))
        if degrees == 0:
            break
        speed = int(input('Enter a speed for the wheels to spin at between 0 and 100: '))
        stop_action = str(input('Enter a stop action (brake, coast, or hold): '))

        if stop_action == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stop_action == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        else:
            stop_action = ev3.Motor.STOP_ACTION_HOLD

        spin_left_by_time(degrees, speed, stop_action)

    # Testing spin_left_by_encoders:

    print()
    print('** Testing of spin_left_by_encoders is starting **')
    print()

    while True:
        degrees = int(input('Enter a number of degrees to rotate by: '))
        if degrees == 0:
            break
        speed = int(input('Enter a speed for the wheels to spin at between 0 and 100: '))
        stop_action = str(input('Enter a stop action (brake, coast, or hold): '))

        if stop_action == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stop_action == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        else:
            stop_action = ev3.Motor.STOP_ACTION_HOLD

        spin_left_by_encoders(degrees, speed, stop_action)

    # Testing spin_right_seconds:

    print()
    print('** Testing of spin_right_seconds is starting **')
    print()

    while True:
        seconds = int(input('Enter a number of seconds to travel for: '))
        if seconds == 0:
            break
        speed = int(input('Enter a speed for the wheels to spin at between 0 and 100: '))
        stop_action = str(input('Enter a stop action (brake, coast, or hold): '))

        if stop_action == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stop_action == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        else:
            stop_action = ev3.Motor.STOP_ACTION_HOLD

        spin_right_seconds(seconds, speed, stop_action)

    # Testing spin_right_by_time:

    print()
    print('** Testing of spin_right_by_time is starting **')
    print()

    while True:
        degrees = int(input('Enter a number of degrees for the robot to rotate: '))
        if degrees == 0:
            break
        speed = int(input('Enter a number between -100 and 100: '))
        stop_action = str(input('Enter a stop action (brake, coast, or hold): '))

        if stop_action == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stop_action == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        else:
            stop_action = ev3.Motor.STOP_ACTION_HOLD

        spin_right_by_time(degrees, speed, stop_action)

    # Testing spin_right_by_encoders:

    print()
    print('** Testing of spin_right_by_encoders is starting **')
    print()

    while True:
        degrees = int(input('Enter a number of degrees for the robot to rotate by: '))
        if degrees == 0:
            break
        speed = int(input('Enter a number between -100 and 100: '))
        stop_action = str(input('Enter a stop action (brake, coast, or hold): '))

        if stop_action == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stop_action == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        else:
            stop_action = ev3.Motor.STOP_ACTION_HOLD

        spin_right_by_encoders(degrees, speed, stop_action)

    print()
    print('Testing has ended.')


def spin_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot spin in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the given stop_action.
    """

    left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)

    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=-speed * 8)
    right_motor.run_forever(speed_sp=speed * 8)
    time.sleep(seconds)
    left_motor.stop(stop_action=stop_action)
    right_motor.stop(stop_action=stop_action)
    ev3.Sound.beep().wait()


def spin_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """

    radians = math.pi * (degrees / 180)
    robot_speed = 4 * ((speed * 8) / 360)
    omega_robot = robot_speed / 2.8125
    sleep_time = (radians / omega_robot)

    left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)

    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_forever(speed_sp=-speed * 8)
    right_motor.run_forever(speed_sp=speed * 8)
    time.sleep(sleep_time)
    left_motor.stop(stop_action=stop_action)
    right_motor.stop(stop_action=stop_action)
    ev3.Sound.beep().wait()


def spin_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot spin in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed spin_right) and 100 (full speed spin_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """

    radians = math.pi * (degrees / 180)
    robot_speed = 4 * ((speed * 8) / 360)
    omega_robot = robot_speed / 2.8125
    rotate_time = radians / omega_robot
    wheel_degrees = (speed * 8) * rotate_time

    left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)

    assert left_motor.connected
    assert right_motor.connected

    left_motor.run_to_rel_pos(position_sp=-wheel_degrees)
    right_motor.run_to_rel_pos(position_sp=wheel_degrees)
    time.sleep(rotate_time)
    left_motor.stop(stop_action=stop_action)
    right_motor.stop(stop_action=stop_action)
    ev3.Sound.beep().wait()


def spin_right_seconds(seconds, speed, stop_action):
    """ Calls spin_left_seconds with negative speeds to achieve spin_right motion. """
    spin_left_seconds(seconds, -speed, stop_action)


def spin_right_by_time(degrees, speed, stop_action):
    """ Calls spin_left_by_time with negative speeds to achieve spin_right motion. """
    spin_left_by_time(degrees, -speed, stop_action)


def spin_right_by_encoders(degrees, speed, stop_action):
    """ Calls spin_left_by_encoders with negative speeds to achieve spin_right motion. """
    spin_left_by_encoders(degrees, speed, stop_action)


test_spin_left_spin_right()
