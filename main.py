from movement.robot import Robot
from movement.triangle import Triangle
from time import sleep

LEGS = {
    "L1": (0, 1),
    "L2": (2, 3),
    "L3": (4, 5),
    "R1": (12, 13),
    "R2": (10, 11),
    "R3": (8, 9)
}

LEFT_TRIANGLE = Triangle(LEGS["L1"], LEGS["R2"], LEGS["L3"])
RIGHT_TRIANGLE = Triangle(LEGS["R1"], LEGS["L2"], LEGS["R3"])

if __name__ == "__main__":
    robot = Robot(LEFT_TRIANGLE, RIGHT_TRIANGLE)
    robot.neutral_position()

    while True:
        if input():
            robot.move_forward()
        robot.neutral_position()

