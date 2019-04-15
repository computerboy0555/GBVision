from .camera import CameraData, Camera
import cv2


class USBCamera(cv2.VideoCapture, Camera):
    def __init__(self, port, data):
        cv2.VideoCapture.__init__(self, port)
        self._data = data
        self.port = port

    def is_opened(self) -> bool:
        return self.isOpened()

    def set_exposure(self, exposure: int or float or bool) -> bool:
        if type(exposure) is bool:
            return self.set(cv2.CAP_PROP_EXPOSURE, int(exposure))
        return self.set(cv2.CAP_PROP_EXPOSURE, exposure)

    def set_auto_exposure(self, auto: int or float or bool) -> bool:
        if type(auto) is bool:
            return self.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.75 if auto else 0.25)
        return self.set(cv2.CAP_PROP_AUTO_EXPOSURE, auto)

    @property
    def data(self):
        return self._data

    @property
    def width(self):
        return self.get(cv2.CAP_PROP_FRAME_WIDTH)

    @property
    def height(self):
        return self.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def _set_width(self, width):
        return self.set(cv2.CAP_PROP_FRAME_WIDTH, width)

    def _set_height(self, height):
        return self.set(cv2.CAP_PROP_FRAME_HEIGHT, height)