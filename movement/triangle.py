from .leg import Leg
from time import sleep


class Triangle:
    def __init__(self, front: tuple, middle: tuple, back: tuple, freq: int = 50, neutral_angle: int = 90) -> None:
        self.freq = freq
        self.neutral_angle = neutral_angle
        self.legs = self.set_triangle(front, middle, back)

    def set_triangle(self, front: tuple, middle: tuple, back: tuple) -> dict[str, Leg]:
        return {"front": self.init_leg(front), 'middle': self.init_leg(middle), 'back': self.init_leg(back)}

    def init_leg(self, leg: tuple) -> Leg:
        return Leg(leg[0], leg[1], self.freq)

    def neutral(self) -> None:
        for leg in self.legs.values():
            leg.set_position(self.neutral_angle, self.neutral_angle)
        sleep(1)

    def move(self, thigh_angle: int = 150, knee_angle: int = 125) -> None:
        self.neutral()
        self.legs_up(knee_angle)
        self.legs_move(knee_angle, thigh_angle, thigh_angle)
        self.legs_down(thigh_angle, thigh_angle)

    def rotate(self, thigh_angle_middle: int, thigh_angle_rest: int, knee_angle: int = 125) -> None:
        self.neutral()
        self.legs_up(knee_angle)
        self.legs_move(knee_angle, thigh_angle_middle, thigh_angle_rest)
        self.legs_down(thigh_angle_middle, thigh_angle_rest)

    def legs_up(self, knee_angle: int) -> None:
        for leg in self.legs.values():
            leg.set_position(knee_angle, self.neutral_angle)
        sleep(1)

    def legs_down(self, thigh_angle_middle: int, thigh_angle_rest: int) -> None:
        self.legs["front"].set_position(self.neutral_angle, thigh_angle_rest)
        self.legs["middle"].set_position(self.neutral_angle, thigh_angle_middle)
        self.legs["back"].set_position(self.neutral_angle, thigh_angle_rest)
        sleep(1)

    def legs_move(self, knee_angle: int, thigh_angle_middle: int, thigh_angle_rest: int) -> None:
        self.legs["front"].set_position(knee_angle, thigh_angle_rest)
        self.legs["middle"].set_position(knee_angle, thigh_angle_middle)
        self.legs["back"].set_position(knee_angle, thigh_angle_rest)
        sleep(1)

