from machine import PWM
from .exceptions import BadAngle


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
