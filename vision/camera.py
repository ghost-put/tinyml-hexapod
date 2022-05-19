from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2


class Camera:
    def __init__(self) -> None:
        camera = PiCamera()
        image_width = 680
        image_height = 480
        camera.resolution = (image_width, image_height)
        camera.framerate = 32
        self.rawCapture = PiRGBArray(camera, size=(image_width, image_width))
        self.camera = camera

        center_image_x = image_width / 2
        center_image_y = image_height / 2

        hue_val = 28  # we need to choose this for the particular color
        self.lower_color = np.array([hue_val - 10, 100, 100])
        self.upper_color = np.array([hue_val + 10, 255, 255])

        self.minimum_area = 250
        self.maximum_area = 100000

    def capture(self) -> tuple:

        for frame in self.camera.capture(self.rawCapture, format="bgr", use_video_port=True):
            image = frame.array

            hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            color_mask = cv2.inRange(hsv, self.lower_color, self.upper_color)

            image2, contours, hierarchy = cv2.findContours(color_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            object_area = 0
            bounding_box = (0, 0, 0, 0)

            for contour in contours:
                x, y, width, height = cv2.boundingRect(contours)

                found_area = width * height

                if found_area > object_area:
                    bounding_box = (x, y, width, height)

            if object_area > 0:
                return bounding_box

            return None
