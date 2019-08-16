from .recording_opencv_window import RecordingOpenCVWindow
from .wrapper_opencv_window import WrapperOpenCVWindow
from gbvision.constants.system import EMPTY_PIPELINE


class RecordingWrapperOpenCVWindow(RecordingOpenCVWindow, WrapperOpenCVWindow):
    def __init__(self, window_name: str, wrap_object, file_name: str, fps=20.0, exit_button='qQ',
                 drawing_pipeline=EMPTY_PIPELINE, recording_pipeline=EMPTY_PIPELINE, width=0, height=0):
        RecordingOpenCVWindow.__init__(self, window_name, file_name=file_name, fps=fps,
                                       recording_pipeline=recording_pipeline, width=width, height=height)
        WrapperOpenCVWindow.__init__(self, window_name=window_name, wrap_object=wrap_object, exit_button=exit_button,
                                     drawing_pipeline=drawing_pipeline)