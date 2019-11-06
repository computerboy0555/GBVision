
from .tracker import Tracker
import math
#TODO add docs

class ContinuesRect:
    def __init__(self, rect , tracker=None, max_area_ratio=2.0, max_distance_ratio=0.1):
        assert max_area_ratio > 1.0
        self._rect = rect
        self._count = 0
        self._tracker = Tracker() if tracker is None else tracker
        self.max_area_ratio = max_area_ratio
        self.max_distance_ratio = max_distance_ratio

    @staticmethod
    def rect_collision(rect1, rect2):
        x1, y1, w1, h1 = rect1
        x2, y2, w2, h2 = rect2
        return not (x1 > x2 + w2 or x2 > x1 + w1 or y1 > y2 + h2 or y2 > y1 + h1)

    @staticmethod
    def rect_area(rect):
        return rect[2] * rect[3]

    def get(self):
        return self._rect

    def _is_legal(self, rect):
        if self.rect_collision(self._rect, rect):
            if 1.0/self.max_area_ratio <= self.rect_area(self._rect) / self.rect_area(rect) <= self.max_area_ratio:
                x1, y1, w1, h1 = self._rect
                x2, y2, w2, h2 = rect
                if math.sqrt((x1 - x2)**2 + (y1 - y2)**2) <= math.sqrt(min(w1, w2)**2 + min(h1, h2)**2) * self.max_distance_ratio:
                    return True
        return False

    def update(self, frame, rect):
        if self._is_legal(rect):
            self._rect = rect
            self._tracker.init(frame, rect)
            self._count = 0
            return True
        return False

    def update_not_found(self, frame):
        self._count += 1
        rect = self._tracker.get_rect(frame)
        if self._is_legal(rect):
            self._rect = rect

    def is_alive(self, max_wait: int = None):
        if max_wait is not None:
            return self._count <= max_wait
        return True

    
