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


class V1GroupVersionForDiscovery(object):
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
        'group_version': 'str',
        'version': 'str'
    }

    attribute_map = {
        'group_version': 'groupVersion',
        'version': 'version'
    }

    def __init__(self, group_version=None, version=None):
        """
        V1GroupVersionForDiscovery - a model defined in Swagger
        """

        self._group_version = None
        self._version = None
        self.discriminator = None

        self.group_version = group_version
        self.version = version

    @property
    def group_version(self):
        """
        Gets the group_version of this V1GroupVersionForDiscovery.
        groupVersion specifies the API group and version in the form \"group/version\"

        :return: The group_version of this V1GroupVersionForDiscovery.
        :rtype: str
        """
        return self._group_version

    @group_version.setter
    def group_version(self, group_version):
        """
        Sets the group_version of this V1GroupVersionForDiscovery.
        groupVersion specifies the API group and version in the form \"group/version\"

        :param group_version: The group_version of this V1GroupVersionForDiscovery.
        :type: str
        """
        if group_version is None:
            raise ValueError("Invalid value for `group_version`, must not be `None`")

        self._group_version = group_version

    @property
    def version(self):
        """
        Gets the version of this V1GroupVersionForDiscovery.
        version specifies the version in the form of \"version\". This is to save the clients the trouble of splitting the GroupVersion.

        :return: The version of this V1GroupVersionForDiscovery.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this V1GroupVersionForDiscovery.
        version specifies the version in the form of \"version\". This is to save the clients the trouble of splitting the GroupVersion.

        :param version: The version of this V1GroupVersionForDiscovery.
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version

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
        if not isinstance(other, V1GroupVersionForDiscovery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
