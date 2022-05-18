from machine import PWM, Pin
from .functions import set_servo_angle


class Leg:
    """
    """
    def __init__(self, thigh_id: int, knee_id: int, freq: int) -> None:
        #TODO: offset serwa
        self.thigh = PWM(Pin(thigh_id))
        self.knee = PWM(Pin(knee_id))
        self.set_freq(freq)

    def set_freq(self, freq: int) -> None:
        """
        :param freq:
        :return:
        """
        self.knee.freq(freq)
        self.thigh.freq(freq)

    def set_position(self, knee_angle: int, thigh_angle: int):
        self.set_knee_position(knee_angle)
        self.set_thigh_position(thigh_angle)

    def set_knee_position(self, angle):
        self.set_servo_angle(angle, self.knee)

    def set_thigh_position(self, angle):
        self.set_servo_angle(angle, self.thigh)
