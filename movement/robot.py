from .leg import Leg
from .triangle import Triangle
from machine import Pin
from time import sleep


class Robot:
    def __init__(self, left_triangle: Triangle, right_triangle: Triangle, led_pin: int = 25) -> None:
        self.triangles = self.init_triangles(left_triangle, right_triangle)
        self.led_on(led_pin)

    @staticmethod
    def led_on(led_pin) -> None:
        led = Pin(led_pin, Pin.OUT)
        led(1)

    @staticmethod
    def init_triangles(left_triangle: Triangle, right_triangle) -> dict:
        return {"left": left_triangle, "right": right_triangle}

    @staticmethod
    def set_leg_position(leg: Leg, knee_angle: int, thigh_angle: int) -> None:
        leg.set_position(knee_angle, thigh_angle)

    def neutral_position(self) -> None:
        for leg in self.triangles["left"].legs.values():
            leg.set_position(90, 90)
        for leg in self.triangles["right"].legs.values():
            leg.set_position(90, 90)

    def move_forward(self) -> None:
        self.move_triangle("left")
        self.move_triangle("right")

    def move_left(self) -> None:
        self.rotate_triangle("left", 150, 30)
        self.rotate_triangle("right", 30, 150)

    def move_right(self) -> None:
        self.rotate_triangle("left", 30, 150)
        self.rotate_triangle("right", 150, 30)

    def move_backward(self) -> None:
        self.move_triangle("left", thigh_angle = 30)
        self.move_triangle("right", thigh_angle = 30)

    def move_triangle(self, triangle: str, knee_angle: int = 125, thigh_angle: int = 150) -> None:
        self.neutral_position()
        sleep(1)
        self.triangle_up(self.triangles[triangle], knee_angle)
        self.triangle_move(self.triangles[triangle], knee_angle, thigh_angle)
        self.triangle_down(self.triangles[triangle], thigh_angle, thigh_angle)

    def rotate_triangle(self, triangle: str, thigh_angle_middle: int, thigh_angle_rest: int, knee_angle: int = 125) -> None:
        self.neutral_position()
        sleep(1)
        self.triangle_up(self.triangles[triangle], knee_angle)
        self.triangle_rotate(self.triangles[triangle], knee_angle, thigh_angle_middle, thigh_angle_rest)
        self.triangle_down(self.triangles[triangle], thigh_angle_middle, thigh_angle_rest)

    def triangle_up(self, triangle: Triangle, knee_angle: int) -> None:
        for leg in triangle.legs.values():
            self.set_leg_position(leg, knee_angle, 90)
        sleep(1)

    def triangle_down(self, triangle: Triangle, thigh_angle_middle: int, thigh_angle_rest: int) -> None:
        self.set_leg_position(triangle.legs["front"], 90, thigh_angle_rest)
        self.set_leg_position(triangle.legs["middle"], 90, thigh_angle_middle)
        self.set_leg_position(triangle.legs["back"], 90, thigh_angle_rest)
        sleep(1)

    def triangle_move(self, triangle: Triangle, knee_angle: int, thigh_angle: int) -> None:
        for leg in triangle.legs.values():
            self.set_leg_position(leg, knee_angle, thigh_angle)
        sleep(1)

    def triangle_rotate(self, triangle: Triangle, knee_angle: int, thigh_angle_middle: int, thigh_angle_rest: int) -> None:
        self.set_leg_position(triangle.legs["front"], knee_angle, thigh_angle_rest)
        self.set_leg_position(triangle.legs["middle"], knee_angle, thigh_angle_middle)
        self.set_leg_position(triangle.legs["back"], knee_angle, thigh_angle_rest)
        sleep(1)

