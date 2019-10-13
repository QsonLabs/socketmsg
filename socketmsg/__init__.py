"""
socketmsg is a simple protocol to process streaming data from a socket and
format into a message that can be posted to a broker
"""
import os
import sys

from . import socket
if sys.version_info[0] != 2:
    from . import asyncio

name = "socketmsg"
__version__ = '0.0.1'
