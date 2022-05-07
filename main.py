from movement.robot import Robot
from time import sleep

LEGS = {
    "L1": (0, 1),
    "L2": (2, 3),
    "L3": (4, 5),
    "P1": (12, 13),
    "P2": (10, 11),
    "P3": (8, 9)
}

TRIANGLES = (
    ("L1", "L3", "P2"),
    ("L2", "P1", "P3")
)

if __name__ == "__main__":
    robot = Robot(LEGS, TRIANGLES)

    while True:
        robot.neutral_position()
        sleep(10)
        robot.move_forward()
        sleep(10)


