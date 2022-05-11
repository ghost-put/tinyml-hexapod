from .leg import Leg

FREQ = 50


class Triangle:
    def __init__(self, front: tuple, middle: tuple, back: tuple):
        self.legs = self.initialize_legs(front, middle, back)

    @staticmethod
    def initialize_legs(front: tuple, middle: tuple, back: tuple) -> dict:
        legs = {"front": Leg(front[0], front[1], front[2])}
        for leg in leg_ids:
            knee, thigh = leg
            legs[leg] = Leg(knee, thigh, FREQ)
        return legs
