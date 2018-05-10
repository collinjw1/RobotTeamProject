"""
Functions for TURNING the robot LEFT and RIGHT.
Authors: David Fisher, David Mutchler and Aaron Kondrat.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implment turn_left_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for turn_left_by_time.
#   Then repeat for turn_left_by_encoders.
#   Then repeat for the turn_right functions.

import ev3dev.ev3 as ev3
import time


def test_turn_left_turn_right():
    """
    Tests the turn_left and turn_right functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets degrees and runs turn_left_by_time.
      3. Same as #2, but runs turn_left_by_encoders.
      4. Same as #1, 2, 3, but tests the turn_right functions.
    """

    # turn_left_seconds

    while True:
        seconds = int(input('Time to travel (s): '))
        if seconds == 0:
            break
        speed = int(input('Speed (0 to 100): '))
        stpact = str(input('Input "brake", "coast", or "hold": '))
        if stpact == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stpact == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        elif stpact == 'hold':
            stop_action = ev3.Motor.STOP_ACTION_HOLD
        turn_left_seconds(seconds, speed, stop_action)

    # turn_left_by_time

    while True:
        degrees = int(input('Degrees to turn: '))
        if degrees == 0:
            break
        speed = int(input('Speed (0 to 100): '))
        stpact = str(input('Input "brake", "coast", or "hold": '))
        if stpact == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stpact == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        elif stpact == 'hold':
            stop_action = ev3.Motor.STOP_ACTION_HOLD
        turn_left_by_time(degrees, speed, stop_action)

    # turn_left_by_encoders

    while True:
        degrees = int(input('Degrees to turn: '))
        if degrees == 0:
            break
        speed = int(input('Speed (0 to 100): '))
        stpact = str(input('Input "brake", "coast", or "hold": '))
        if stpact == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stpact == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        elif stpact == 'hold':
            stop_action = ev3.Motor.STOP_ACTION_HOLD
        turn_left_by_encoders(degrees, speed, stop_action)

    # turn_right_seconds

    while True:
        seconds = int(input('Time to travel (s): '))
        if seconds == 0:
            break
        speed = int(input('Speed (-100 to 0): '))
        stpact = str(input('Input "brake", "coast", or "hold": '))
        if stpact == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stpact == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        elif stpact == 'hold':
            stop_action = ev3.Motor.STOP_ACTION_HOLD
        turn_right_seconds(seconds, speed, stop_action)

    # turn_right_by_time

    while True:
        degrees = int(input('Degrees to turn: '))
        if degrees == 0:
            break
        speed = int(input('Speed (-100 to 0): '))
        stpact = str(input('Input "brake", "coast", or "hold": '))
        if stpact == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stpact == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        elif stpact == 'hold':
            stop_action = ev3.Motor.STOP_ACTION_HOLD
        turn_right_by_time(degrees, speed, stop_action)

    # turn_right_by_encoders

    while True:
        degrees = int(input('Degrees to turn: '))
        if degrees == 0:
            break
        speed = int(input('Speed (-100 to 0): '))
        stpact = str(input('Input "brake", "coast", or "hold": '))
        if stpact == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stpact == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        elif stpact == 'hold':
            stop_action = ev3.Motor.STOP_ACTION_HOLD
        turn_right_by_encoders(degrees, speed, stop_action)


def turn_left_seconds(seconds, speed, stop_action):
    """
    Makes the robot turn in place left for the given number of seconds at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the given stop_action.
    """
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor.run_forever(speed_sp=speed*8)
    time.sleep(seconds)
    right_motor.stop(stop_action=stop_action)
    ev3.Sound.beep().wait()


def turn_left_by_time(degrees, speed, stop_action):
    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    seconds = 1.11 * degrees / abs(speed)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    right_motor.run_forever(speed_sp=speed*8)
    time.sleep(seconds)
    right_motor.stop(stop_action=stop_action)
    ev3.Sound.beep().wait()


def turn_left_by_encoders(degrees, speed, stop_action):
    """
    Makes the robot turn in place left the given number of degrees at the given speed,
    where speed is between -100 (full speed turn_right) and 100 (full speed turn_left).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should turn to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    deg = 10*degrees
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    assert right_motor.connected
    right_motor.run_to_rel_pos(position_sp=deg, speed_sp=speed*8)
    right_motor.wait_while(ev3.Motor.STATE_RUNNING)
    right_motor.stop(stop_action=stop_action)
    ev3.Sound.beep().wait()


def turn_right_seconds(seconds, speed, stop_action):
    """ Calls turn_left_seconds with negative speeds to achieve turn_right motion. """
    turn_left_seconds(seconds, speed, stop_action)


def turn_right_by_time(degrees, speed, stop_action):
    """ Calls turn_left_by_time with negative speeds to achieve turn_right motion. """
    turn_left_by_time(degrees, speed, stop_action)


def turn_right_by_encoders(degrees, speed, stop_action):
    """ Calls turn_left_by_encoders with negative speeds to achieve turn_right motion. """
    turn_left_by_encoders(-degrees, speed, stop_action)


test_turn_left_turn_right()
