# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.0.1.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImageUploadResultModel(Model):
    """ImageUploadResultModel.

    :param url:
    :type url: str
    :param status: Possible values include: 'OK', 'ErrorDuplicate',
     'ErrorSource', 'ErrorImage', 'ErrorStorage', 'ErrorUnknown'
    :type status: str or :class:`enum <training.models.enum>`
    """

    _attribute_map = {
        'url': {'key': 'Url', 'type': 'str'},
        'status': {'key': 'Status', 'type': 'str'},
    }

    def __init__(self, url=None, status=None):
        self.url = url
        self.status = status
