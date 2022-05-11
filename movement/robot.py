from .leg import Leg
from machine import Pin
from time import sleep


class Robot:
    def __init__(self, leg_ids: dict, triangles: tuple, freq: int = 50, led_pin: int = 25) -> None:
        self.freq = freq
        self.legs = self.initialize_legs(leg_ids)
        self.triangles = {}
        self.initialize_triangles(triangles)
        self.led_on(led_pin)

    @staticmethod
    def led_on(led_pin) -> None:
        led = Pin(led_pin, Pin.OUT)
        led(1)

    def initialize_legs(self, leg_ids: dict) -> dict:
        legs = {}
        for leg in leg_ids:
            knee, thigh = leg_ids[leg]
            legs[leg] = Leg(knee, thigh, self.freq)
        return legs

    def initialize_triangles(self, triangles: tuple) -> None:
        self.triangles["left"] = triangles[0]
        self.triangles["right"] = triangles[1]

    def set_leg_position(self, leg_id: str, knee_angle: int, thigh_angle: int) -> None:
        self.legs[leg_id].set_position(knee_angle, thigh_angle)

    def neutral_position(self) -> None:
        for leg_id in self.legs:
            self.set_leg_position(leg_id, 90, 90)

    def move_forward(self) -> None:
        self.move_triangle("left")
        self.move_triangle("right")

    def move_left(self) -> None:
        pass

    def move_right(self) -> None:
        pass

    def move_triangle(self, triangle: str, knee_angle: int = 125, thigh_angle: int = 150) -> None:
        self.neutral_position()
        sleep(1)
        self.triangle_up(self.triangles[triangle], knee_angle)
        # self.triangle_move(self.triangles[triangle], knee_angle, thigh_angle)
        # self.triangle_down(self.triangles[triangle], thigh_angle)

    def triangle_up(self, triangle, knee_angle):
        for leg_id in triangle:
            self.set_leg_position(leg_id, knee_angle, 90)

    def triangle_move(self, triangle, knee_angle, thigh_angle):
        for leg_id in triangle:
            self.set_leg_position(leg_id, knee_angle, thigh_angle)
        sleep(1)

    def triangle_down(self, triangle, thigh_angle):
        for leg_id in triangle:
            self.set_leg_position(leg_id, 90, thigh_angle)
        sleep(1)
