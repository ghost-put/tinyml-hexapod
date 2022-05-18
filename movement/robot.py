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

    def neutral_position(self) -> None:
        self.triangles["left"].neutral()
        self.triangles["right"].neutral()

    def move_forward(self) -> None:
        self.triangles["left"].move(self.triangles["right"], thigh_angle_middle=55, thigh_angle_rest=125)
        self.triangles["right"].move(self.triangles["left"], thigh_angle_middle=125, thigh_angle_rest=55)

    def move_backward(self) -> None:
        self.triangles["left"].move(self.triangles["right"], thigh_angle_middle=125, thigh_angle_rest=55)
        self.triangles["right"].move(self.triangles["left"], thigh_angle_middle=55, thigh_angle_rest=125)

    def move_right(self) -> None:
        self.triangles["left"].move(self.triangles["right"], thigh_angle_middle=55, thigh_angle_rest=55)
        self.triangles["right"].move(self.triangles["left"], thigh_angle_middle=125, thigh_angle_rest=125)

    def move_left(self) -> None:
        self.triangles["left"].move(self.triangles["right"], thigh_angle_middle=125, thigh_angle_rest=125)
        self.triangles["right"].move(self.triangles["left"], thigh_angle_middle=55, thigh_angle_rest=55)
