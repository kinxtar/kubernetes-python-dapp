# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ConfigMapVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_mode': 'int',
        'items': 'list[V1KeyToPath]',
        'name': 'str',
        'optional': 'bool'
    }

    attribute_map = {
        'default_mode': 'defaultMode',
        'items': 'items',
        'name': 'name',
        'optional': 'optional'
    }

    def __init__(self, default_mode=None, items=None, name=None, optional=None):
        """
        V1ConfigMapVolumeSource - a model defined in Swagger
        """

        self._default_mode = None
        self._items = None
        self._name = None
        self._optional = None
        self.discriminator = None

        if default_mode is not None:
          self.default_mode = default_mode
        if items is not None:
          self.items = items
        if name is not None:
          self.name = name
        if optional is not None:
          self.optional = optional

    @property
    def default_mode(self):
        """
        Gets the default_mode of this V1ConfigMapVolumeSource.
        Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.

        :return: The default_mode of this V1ConfigMapVolumeSource.
        :rtype: int
        """
        return self._default_mode

    @default_mode.setter
    def default_mode(self, default_mode):
        """
        Sets the default_mode of this V1ConfigMapVolumeSource.
        Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.

        :param default_mode: The default_mode of this V1ConfigMapVolumeSource.
        :type: int
        """

        self._default_mode = default_mode

    @property
    def items(self):
        """
        Gets the items of this V1ConfigMapVolumeSource.
        If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

        :return: The items of this V1ConfigMapVolumeSource.
        :rtype: list[V1KeyToPath]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this V1ConfigMapVolumeSource.
        If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.

        :param items: The items of this V1ConfigMapVolumeSource.
        :type: list[V1KeyToPath]
        """

        self._items = items

    @property
    def name(self):
        """
        Gets the name of this V1ConfigMapVolumeSource.
        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :return: The name of this V1ConfigMapVolumeSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ConfigMapVolumeSource.
        Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names

        :param name: The name of this V1ConfigMapVolumeSource.
        :type: str
        """

        self._name = name

    @property
    def optional(self):
        """
        Gets the optional of this V1ConfigMapVolumeSource.
        Specify whether the ConfigMap or it's keys must be defined

        :return: The optional of this V1ConfigMapVolumeSource.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """
        Sets the optional of this V1ConfigMapVolumeSource.
        Specify whether the ConfigMap or it's keys must be defined

        :param optional: The optional of this V1ConfigMapVolumeSource.
        :type: bool
        """

        self._optional = optional

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1ConfigMapVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
