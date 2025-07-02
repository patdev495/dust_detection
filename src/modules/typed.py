from typing import TypedDict
import numpy as np

class CCDResult(TypedDict):
    original_image:  np.ndarray
    binary_image: np.ndarray
    rotated_image: np.ndarray
    cropped_image: np.ndarray
    ccd_box_original: np.int32
    top_left_point : tuple[int,...]
    ccd_box_rotated: np.ndarray
    rotate_angle: float
    center: tuple[int,int]
            