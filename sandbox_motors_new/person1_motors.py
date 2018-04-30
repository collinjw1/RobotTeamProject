"""
Functions for moving the robot FORWARD and BACKWARD.
Authors: David Fisher, David Mutchler and Jonathan Collins.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implment forward_seconds, then the relevant part of the test function.
#          Test and correct as needed.
#   Then repeat for forward_by_time.
#   Then repeat for forward_by_encoders.
#   Then repeat for the backward functions.

import ev3dev.ev3 as ev3
import time
import math


def test_forward_backward():
    """
    Tests the forward and backward functions, as follows:
      1. Repeatedly:
          -- Prompts for and gets input from the console for:
             -- Seconds to travel
                  -- If this is 0, BREAK out of the loop.
             -- Speed at which to travel (-100 to 100)
             -- Stop action ("brake", "coast" or "hold")
          -- Makes the robot run per the above.
      2. Same as #1, but gets inches and runs forward_by_time.
      3. Same as #2, but runs forward_by_encoders.
      4. Same as #1, 2, 3, but tests the BACKWARD functions.
    """
    while True:
        seconds_to_travel=int(input('Seconds to travel:'))
        if seconds_to_travel == 0:
            break
        speed=int(input('Speed(-100 to 100):'))
        input_stop=str(input('Stop Action:'))

        if input_stop == 'brake':
            stop_action = ev3.Motor.STOP_ACTION_BRAKE
        elif stop_action == 'coast':
            stop_action = ev3.Motor.STOP_ACTION_COAST
        elif stop_action == 'hold':
            stop_action == ev3.Motor.STOP_ACTION_HOLD


        forward_seconds(seconds_to_travel,speed,stop_action)


def forward_seconds(seconds, speed, stop_action):
    """
    Makes the robot move forward for the given number of seconds at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the given stop_action.
    """
    left_motor=ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor=ev3.LargeMotor(ev3.OUTPUT_B)

    assert left_motor.connected
    assert right_motor.connected

    gogojuice=speed*8
    left_motor.run_forever(speed_sp=gogojuice)
    right_motor.run_forever(speed_sp=gogojuice)

    time.sleep(seconds)

    left_motor.stop(stop_action=stop_action)
    right_motor.stop(stop_action=stop_action)

def forward_by_time(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      0. Compute the number of seconds to move to achieve the desired distance.
      1. Start moving.
      2. Sleep for the computed number of seconds.
      3. Stop moving.
    """
    gogojuice=speed*8
    disd=(inches/(1.3*math.pi))*360
    time=disd/gogojuice
    forward_seconds(time,speed,stop_action)


def forward_by_encoders(inches, speed, stop_action):
    """
    Makes the robot move forward the given number of inches at the given speed,
    where speed is between -100 (full speed backward) and 100 (full speed forward).
    Uses the algorithm:
      1. Compute the number of degrees the wheels should spin to achieve the desired distance.
      2. Move until the computed number of degrees is reached.
    """
    left_motor = ev3.LargeMotor(ev3.OUTPUT_C)
    right_motor = ev3.LargeMotor(ev3.OUTPUT_B)
    gogojuice = speed * 8
    disd = (inches / (1.3 * math.pi))*360
    left_motor.run_to_rel_pos(position_sp=disd, speed_sp=gogojuice)
    right_motor.run_to_rel_pos(position_sp=-disd, speed_sp=gogojuice)


def backward_seconds(seconds, speed, stop_action):
    """ Calls forward_seconds with negative speeds to achieve backward motion. """
    forward_seconds(seconds,-speed,stop_action)


def backward_by_time(inches, speed, stop_action):
    """ Calls forward_by_time with negative speeds to achieve backward motion. """
    forward_by_time(inches,-speed,stop_action)


def backward_by_encoders(inches, speed, stop_action):
    """ Calls forward_by_encoders with negative speeds to achieve backward motion. """
    forward_by_encoders(inches,-speed,stop_action)


test_forward_backward()
