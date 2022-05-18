from .leg import Leg
from time import sleep_ms


class Triangle:
    def __init__(self, front: tuple, middle: tuple, back: tuple, freq: int = 50, neutral_angle: int = 90) -> None:
        self.freq = freq
        self.neutral_angle = neutral_angle
        self.legs = self.set_triangle(front, middle, back)
        self.sleep_time = 250

    def set_triangle(self, front: tuple, middle: tuple, back: tuple) -> dict[str, Leg]:
        return {"front": self.init_leg(front), 'middle': self.init_leg(middle), 'back': self.init_leg(back)}

    def init_leg(self, leg: tuple) -> Leg:
        return Leg(leg[0], leg[1], self.freq)

    @staticmethod
    def set_leg_position(leg: Leg, knee_angle: int, thigh_angle: int) -> None:
        leg.set_position(knee_angle, thigh_angle)

    def neutral(self) -> None:
        for leg in self.legs.values():
            self.set_leg_position(leg, self.neutral_angle, self.neutral_angle)
        sleep_ms(self.sleep_time)

    def move(self, other: 'Triangle', thigh_angle_middle: int, thigh_angle_rest: int, knee_angle: int = 30) -> None:
        self.legs_up(knee_angle)
        other.neutral()
        self.legs_move(knee_angle, thigh_angle_middle, thigh_angle_rest)
        self.legs_down(thigh_angle_middle, thigh_angle_rest)

    def legs_up(self, knee_angle: int) -> None:
        for leg in self.legs.values():
            self.set_leg_position(leg, knee_angle, self.neutral_angle)
        sleep_ms(self.sleep_time)

    def legs_down(self, thigh_angle_middle: int, thigh_angle_rest: int) -> None:
        self.set_leg_position(self.legs["front"], self.neutral_angle, thigh_angle_rest)
        self.set_leg_position(self.legs["middle"], self.neutral_angle, thigh_angle_middle)
        self.set_leg_position(self.legs["back"], self.neutral_angle, thigh_angle_rest)
        sleep_ms(self.sleep_time)

    def legs_move(self, knee_angle: int, thigh_angle_middle: int, thigh_angle_rest: int) -> None:
        self.set_leg_position(self.legs["front"], knee_angle, thigh_angle_rest)
        self.set_leg_position(self.legs["middle"], knee_angle, thigh_angle_middle)
        self.set_leg_position(self.legs["back"], knee_angle, thigh_angle_rest)
        sleep_ms(self.sleep_time)
