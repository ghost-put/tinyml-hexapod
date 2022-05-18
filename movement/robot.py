from .leg import Leg
from .triangle import Triangle
from machine import Pin


class Robot:
    def __init__(self, left_triangle: Triangle, right_triangle: Triangle, led_pin: int = 25) -> None:
        self.triangles = self.init_triangles(left_triangle, right_triangle)
        self.led_on(led_pin)

    @staticmethod
    def led_on(led_pin) -> None:
        led = Pin(led_pin, Pin.OUT)
        led(1)

    @staticmethod
    def init_triangles(left_triangle: Triangle, right_triangle) -> dict[str, Triangle]:
        return {"left": left_triangle, "right": right_triangle}

    @staticmethod
    def set_leg_position(leg: Leg, knee_angle: int, thigh_angle: int) -> None:
        leg.set_position(knee_angle, thigh_angle)

    def neutral_position(self) -> None:
        self.triangles["left"].neutral()
        self.triangles["right"].neutral()

    def move_forward(self) -> None:
        self.triangles["left"].move()
        self.triangles["right"].move()

    def move_left(self) -> None:
        self.triangles["left"].rotate(thigh_angle_middle=150, thigh_angle_rest=30)
        self.triangles["right"].rotate(thigh_angle_middle=30, thigh_angle_rest=150)

    def move_right(self) -> None:
        self.triangles["left"].rotate(thigh_angle_middle=30, thigh_angle_rest=150)
        self.triangles["right"].rotate(thigh_angle_middle=150, thigh_angle_rest=30)

    def move_left(self) -> None:
        self.triangles["left"].move(self.triangles["right"], thigh_angle_middle=125, thigh_angle_rest=125)
        self.triangles["right"].move(self.triangles["left"], thigh_angle_middle=55, thigh_angle_rest=55)

