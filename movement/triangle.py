from .leg import Leg


class Triangle:
    def __init__(self, front: tuple, middle: tuple, back: tuple, freq: int = 50) -> None:
        self.freq = freq
        self.legs = self.set_triangle(front, middle, back)

    def set_triangle(self, front: tuple, middle: tuple, back: tuple) -> dict:
        return {"front": self.init_leg(front), 'middle': self.init_leg(middle), 'back': self.init_leg(back)}

    def init_leg(self, leg: tuple) -> Leg:
        return Leg(leg[0], leg[1], self.freq)
