import robot_interface

# Test
robot = robot_interface.RobotInterface()
speed, direction = robot.rate_to_motor(100,50)

print speed, direction

print robot.ultrasonic_to_probability(100)