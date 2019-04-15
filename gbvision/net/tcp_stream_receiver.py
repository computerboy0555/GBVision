from .stream_receiver import StreamReceiver
import socket
import cv2
import pickle
import struct


class TCPStreamReceiver(StreamReceiver):
    """
    this class uses TCP to receive a stream over the network, the stream is by default set to be MJPEG
    the broadcaster is the server and the receiver is the client
    """

    def __init__(self, ip: str, port: int, fx: float = 1.0, fy: float = 1.0):
        """
        initializes the stream receiver
        :param ip: the IPv4 address of the stream broadcaster, for example '10.45.90.8'
        :param port: the port which TCP should use
        """
        StreamReceiver.__init__(self, fx=fx, fy=fy)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_addr = (ip, port)
        self.socket.connect(self.server_addr)
        self.payload_size = struct.calcsize("I")
        self.data = b''

    def get_frame(self):
        while len(self.data) < self.payload_size:
            self.data += self.socket.recv(4096)

        packed_msg_size = self.data[:self.payload_size]

        self.data = self.data[self.payload_size:]

        msg_size = struct.unpack("I", packed_msg_size)[0]

        while len(self.data) < msg_size:
            self.data += self.socket.recv(4096)

        frame_data = self.data[:msg_size]
        self.data = self.data[msg_size:]
        frame = pickle.loads(frame_data)
        if frame is None:
            return None
        frame = cv2.imdecode(frame, -1)
        return cv2.resize(frame, (0, 0), fx=self.fx, fy=self.fy)