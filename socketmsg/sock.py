"""socket.py: socket handlers implemented as functions"""
import socket
import re


class SockListener(object):
    def __init__(self, config):
        self.host = config.get('host', 'localhost')
        self.port = config.get('port', None)
        self.delimeter = config.get('delimeter', '\r?\n')
        self.connect()
        self.msg = self.recv()

    def connect(self):
        self.buf = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))

    def disconnect(self):
        if self.socket:
            self.socket.close()

    def recv(self):
        while re.search(self.delimeter, self.buf) is None:
            self.buf += self.socket.recv(4096)
        [text, self.buf] = re.split('\r?\n', self.buf, 1)
        return text


def _resolve_protocol(protocol):
    """Returns the appropriate tocket protocol for UDP or TCP"""
    p = protocol.lower()
    if p == "tcp":
        return socket.SOCK_STREAM
    elif p == "udp":
        return socket.SOCK_DGRAM
    else:
        raise ValueError("Must provide protocol as UDP or TCP")
