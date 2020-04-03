"""Zoom.us REST API Python Client -- Chat Messages component"""

from zoomapi import util
from zoomapi.components import base

class ChatChannelsComponentV2(base.BaseComponent):
    """Component dealing with all chat channels related matters"""

    def list(self, **kwargs):
        return self.get_request("/chat/users/me/channels")

    def post(self, **kwargs):
        util.require_keys(kwargs, "name")
        return self.post_request("/chat/users/me/channels", data=kwargs)

