# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.21
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1CustomResourceSubresources(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'scale': 'V1beta1CustomResourceSubresourceScale',
        'status': 'object'
    }

    attribute_map = {
        'scale': 'scale',
        'status': 'status'
    }

    def __init__(self, scale=None, status=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1CustomResourceSubresources - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scale = None
        self._status = None
        self.discriminator = None

        if scale is not None:
            self.scale = scale
        if status is not None:
            self.status = status

    @property
    def scale(self):
        """Gets the scale of this V1beta1CustomResourceSubresources.  # noqa: E501


        :return: The scale of this V1beta1CustomResourceSubresources.  # noqa: E501
        :rtype: V1beta1CustomResourceSubresourceScale
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this V1beta1CustomResourceSubresources.


        :param scale: The scale of this V1beta1CustomResourceSubresources.  # noqa: E501
        :type: V1beta1CustomResourceSubresourceScale
        """

        self._scale = scale

    @property
    def status(self):
        """Gets the status of this V1beta1CustomResourceSubresources.  # noqa: E501

        status indicates the custom resource should serve a `/status` subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the `status` stanza of the object. 2. requests to the custom resource `/status` subresource ignore changes to anything other than the `status` stanza of the object.  # noqa: E501

        :return: The status of this V1beta1CustomResourceSubresources.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1beta1CustomResourceSubresources.

        status indicates the custom resource should serve a `/status` subresource. When enabled: 1. requests to the custom resource primary endpoint ignore changes to the `status` stanza of the object. 2. requests to the custom resource `/status` subresource ignore changes to anything other than the `status` stanza of the object.  # noqa: E501

        :param status: The status of this V1beta1CustomResourceSubresources.  # noqa: E501
        :type: object
        """

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1CustomResourceSubresources):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1CustomResourceSubresources):
            return True

        return self.to_dict() != other.to_dict()
