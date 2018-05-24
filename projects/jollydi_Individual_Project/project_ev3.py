import mqtt_remote_method_calls as com
import robot_controller as robo
import time


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.running = True
    while robot.running:
        if robot.blocked:
            robot.ask_for_directions(mqtt_client)
            continue
        time.sleep(0.05)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
