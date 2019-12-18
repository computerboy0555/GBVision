from typing import List

import cv2
import numpy as np

from gbvision.constants.system import EMPTY_PIPELINE
from gbvision.constants.types import Frame, Polygon, Contour, Number, Point, FilterFunction
from gbvision.models.contours import FilterContours, find_contours, sort_polygons, contour_center, contours_to_polygons
from .object_finder import ObjectFinder


class PolygonFinder(ObjectFinder):
    """
    finds any generic polygon, not recommended when another finder can be used

    :param area_scalar: optional, a scalar to multiply the area by, for fine tuning of the function's output
    :param contour_min_area: the minimal area of a contour, used for FilterContours, default is 0 (no area limit)
    :param threshold_func: a pipeline (or any sort of function) that returns a binary threshold of the object
     the finder is searching, the object needs to be white and the rest if the image black (doesn't
     have to be perfect)
    """

    def __init__(self, threshold_func: FilterFunction, game_object, area_scalar=1.0, contour_min_area=0.0):
        ObjectFinder.__init__(self, game_object, area_scalar=area_scalar)
        self._full_pipeline = (EMPTY_PIPELINE +
                               threshold_func +
                               find_contours +
                               FilterContours(min_area=contour_min_area) +
                               contours_to_polygons +
                               sort_polygons)

    def find_shapes(self, frame: Frame) -> List[Polygon]:
        return self._full_pipeline(frame)

    @staticmethod
    def _shape_root_area(shape: Contour) -> Number:
        return np.sqrt(cv2.contourArea(shape))

    @staticmethod
    def _shape_center(shape: Contour) -> Point:
        return contour_center(shape)
