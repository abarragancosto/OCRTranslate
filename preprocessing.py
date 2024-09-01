import cv2
import numpy as np

class Preprocessing:
    @staticmethod
    def convert_to_grayscale(image):
        image_np = np.array(image)
        return cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
