"""socket.py: socket handlers"""
import sys

if sys.version_info[0] == 2:
    print("asyncio socket handler not available in python2")
    sys.exit(0)

import asyncio
