from typing import List

import cv2
import numpy as np

from gbvision.constants.types import Frame, Contour, Color, Circle, Rect, RotatedRect, Ellipse


def draw_contours(frame: Frame, cnts: List[Contour], color: Color, *args, **kwargs) -> Frame:
    """
    draws all contours on a copy of the frame and returns the copy

    :param frame: the frame to draw on
    :param cnts: the contours to draw
    :param color: the color to draw in
    :param args: all extra args to opencv's  drawContours (for example thickness)
    :param kwargs: all extra keyword args to opencv's  drawContours (for example thickness)
    :return: a copy of the frame, after drawing
    """
    frame = frame.copy()
    cv2.drawContours(frame, cnts, -1, color, *args, **kwargs)
    return frame


def draw_circles(frame: Frame, circs: List[Circle], color: Color, *args, **kwargs) -> Frame:
    """
    draws all circles on a copy of the frame and returns the copy

    :param frame: the frame to draw on
    :param circs: the circles to draw
    :param color: the color to draw in
    :param args: all extra args to opencv's circle (for example thickness)
    :param kwargs: all extra keyword args to opencv's circle (for example thickness)
    :return: a copy of the frame, after drawing
    """
    frame = frame.copy()
    for c in circs:
        cv2.circle(frame, (int(c[0][0]), int(c[0][1])), int(c[1]), color, *args, **kwargs)
    return frame


def draw_rects(frame: Frame, rects: List[Rect], color: Color, *args, **kwargs) -> Frame:
    """
    draws all rects on a copy of the frame and returns the copy

    :param frame: the frame to draw on
    :param rects: the rects to draw
    :param color: the color to draw in
    :param args: all extra args to opencv's rectangle (for example thickness)
    :param kwargs: all extra keyword args to opencv's rectangle (for example thickness)
    :return: a copy of the frame, after drawing
    """
    frame = frame.copy()
    for r in rects:
        cv2.rectangle(frame, (int(r[0]), int(r[1])), (int(r[0] + r[2]), int(r[1] + r[3])), color, *args, **kwargs)
    return frame


def draw_rotated_rects(frame: Frame, rotated_rects: List[RotatedRect], color: Color, *args, **kwargs) -> Frame:
    """
    draws all rotated rects on a copy of the frame and returns the copy

    :param frame: the frame to draw on
    :param rotated_rects: the rotated rects to draw
    :param color: the color to draw in
    :param args: all extra args to opencv's drawContours (for example thickness)
    :param kwargs: all extra keyword args to opencv's drawContours (for example thickness)
    :return: a copy of the frame, after drawing
    """
    frame = frame.copy()
    for r in rotated_rects:
        box = cv2.boxPoints(r)
        box = np.int0(box)
        cv2.drawContours(frame, [box], 0, color, *args, **kwargs)
    return frame


def draw_ellipses(frame: Frame, ellipses: List[Ellipse], color: Color, *args, **kwargs) -> Frame:
    """
    draws all contours on a copy of the frame and returns the copy
    
    :param frame: the frame to draw on
    :param ellipses: the ellipses to draw
    :param color: the color to draw in
    :param args: all extra args to opencv's ellipse (for example thickness)
    :param kwargs: all extra keyword args to opencv's ellipse (for example thickness)
    :return: a copy of the frame, after drawing
    """
    frame = frame.copy()
    for e in ellipses:
        cv2.ellipse(frame, e, color, *args, **kwargs)
    return frame
