# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageUrlBatch(Model):
    """ImageUrlBatch.

    :param urls:
    :type urls: list of str
    """

    _attribute_map = {
        'urls': {'key': 'Urls', 'type': '[str]'},
    }

    def __init__(self, urls=None):
        self.urls = urls
