import pytest
import sys
import re
import socket

# Python 2.x 3.x compatibility
from six.moves import xrange

from socketmsg import sock


class TestSocket(object):

    # for more info on parameterize
    # https://docs.pytest.org/en/latest/parametrize.html#parametrize
    @pytest.mark.parametrize("protocol", [
        "tcp",
        "TCP",
    ], scope="class")
    def test__resolve_protocol_handles_tcp(self, protocol):
        assert socket.SOCK_STREAM == sock._resolve_protocol(protocol)
