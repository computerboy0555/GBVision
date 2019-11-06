import math
from gbvision.constants.math import SQRT_PI as sPI
from gbvision.constants.types import Rect, Number, Circle
from gbvision.continuity.continues_shape import ContinuesShape
from gbvision.utils.tracker import Tracker


class ContinuesCircle(ContinuesShape):
    def __init__(self, circle: Circle, tracker: Tracker = None, max_area_ratio = 2.0, max_distance_ratio = 1.0):
        self._circle = circle
        self._tracker = tracker if tracker is not None else Tracker()
        self._max_area_ratio = max_area_ratio
        self._max_distance_ratio = max_distance_ratio

    def _shape_collision(self, shape: Circle) -> bool:
            return self._shape_square_distance(shape) < (self._shape[1] + shape[1])**2

    @staticmethod
    def _shape_area(shape: Circle) -> Number:
        return sPI**2 * shape[1]**2

    def _shape_square_distance(self, shape: Circle) -> Number:
        return self._shape[0[0]] - shape[0[0]]) ** 2 + (self._shape[0[1]] - shape[0[1]]) ** 2

    @staticmethod
    def _from_bounding_rect(bounding_rect: Rect):
        pass

    @staticmethod
    def _to_bounding_rect(shape) -> Rect:
        pass
