import socket
import struct

from gbvision.constants.net import LOCAL_SERVER_IP
from .stream_broadcaster import StreamBroadcaster
from gbvision.exceptions.tcp_stream_closed import TCPStreamClosed


class TCPStreamBroadcaster(StreamBroadcaster):
    """
    this class uses TCP to send a stream over the network, the stream is by default set to be MJPEG
    the broadcaster is the server and the receiver is the client
    
    :param port: the port which TCP will be using
    :param im_encode: the type of image encoding to send over the network, default is .jpg (JPEG)
        for missing parameters, see documentation on StreamBroadcaster
    """

    def __init__(self, port: int, shape=(0, 0), fx=1.0, fy=1.0, im_encode='.jpg',
                 use_grayscale=False, max_fps: int = None):
        """
        initializes the streamer
        
        """
        StreamBroadcaster.__init__(self, shape=shape, fx=fx, fy=fy, use_grayscale=use_grayscale, max_fps=max_fps,
                                   im_encode=im_encode)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_addr = (LOCAL_SERVER_IP, port)
        self.socket.bind(self.server_addr)
        self.socket.listen(10)
        self.socket, addr = self.socket.accept()
        self.payload_size = struct.calcsize("I")

    def _send_frame(self, frame):
        try:
            self.socket.send(frame)
        except IOError:
            raise TCPStreamClosed()
        self._update_time()
