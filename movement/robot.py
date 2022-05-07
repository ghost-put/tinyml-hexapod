from .leg import Leg
from machine import Pin


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

    def move_forward(self):
        angle = 120

        self.triangle_up(self.triangles["left"], angle)
        self.triangle_move(self.triangles["left"], angle, angle)
        self.triangle_down(self.triangles["left"], angle)
        self.triangle_up(self.triangles["right"], angle)
        self.triangle_move(self.triangles["left"], 90, 90)
        self.triangle_down(self.triangles["right"], angle)

    def triangle_up(self, triangle, knee_angle):
        for leg_id in triangle:
            self.set_leg_position(leg_id, knee_angle, 90)

    def triangle_move(self, triangle, knee_angle, thigh_angle):
        for leg_id in triangle:
            self.set_leg_position(leg_id, knee_angle, thigh_angle)

    def triangle_down(self, triangle, thigh_angle):
        for leg_id in triangle:
            self.set_leg_position(leg_id, 90, thigh_angle)
