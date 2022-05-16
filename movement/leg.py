from machine import PWM, Pin
from .exceptions import BadAngle


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

    @staticmethod
    def set_servo_angle(angle: int, servo_pin: PWM) -> None:
        """
                 Linear function

                 0 degrees = 1350
                 180 degrees = 8200
                 final value = 1350 + angle*6850/180
        """
        if angle < 0 or angle > 180:
            raise BadAngle('Only <0;180> degrees INT values can be accepted')
        else:
            value_duty = int(1350 + (angle * 6850) / 180)
            servo_pin.duty_u16(value_duty)
            print(f"Servo: {servo_pin}; Angle: {angle}; Duty: {value_duty}")

    def set_position(self, knee_angle: int, thigh_angle: int):
        self.set_knee_position(knee_angle)
        self.set_thigh_position(thigh_angle)

    def set_knee_position(self, angle):
        self.set_servo_angle(angle, self.knee)

    def set_thigh_position(self, angle):
        self.set_servo_angle(angle, self.thigh)

