# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.27
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1ContainerState(object):
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
        'running': 'V1ContainerStateRunning',
        'terminated': 'V1ContainerStateTerminated',
        'waiting': 'V1ContainerStateWaiting'
    }

    attribute_map = {
        'running': 'running',
        'terminated': 'terminated',
        'waiting': 'waiting'
    }

    def __init__(self, running=None, terminated=None, waiting=None, local_vars_configuration=None):  # noqa: E501
        """V1ContainerState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._running = None
        self._terminated = None
        self._waiting = None
        self.discriminator = None

        if running is not None:
            self.running = running
        if terminated is not None:
            self.terminated = terminated
        if waiting is not None:
            self.waiting = waiting

    @property
    def running(self):
        """Gets the running of this V1ContainerState.  # noqa: E501


        :return: The running of this V1ContainerState.  # noqa: E501
        :rtype: V1ContainerStateRunning
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this V1ContainerState.


        :param running: The running of this V1ContainerState.  # noqa: E501
        :type: V1ContainerStateRunning
        """

        self._running = running

    @property
    def terminated(self):
        """Gets the terminated of this V1ContainerState.  # noqa: E501


        :return: The terminated of this V1ContainerState.  # noqa: E501
        :rtype: V1ContainerStateTerminated
        """
        return self._terminated

    @terminated.setter
    def terminated(self, terminated):
        """Sets the terminated of this V1ContainerState.


        :param terminated: The terminated of this V1ContainerState.  # noqa: E501
        :type: V1ContainerStateTerminated
        """

        self._terminated = terminated

    @property
    def waiting(self):
        """Gets the waiting of this V1ContainerState.  # noqa: E501


        :return: The waiting of this V1ContainerState.  # noqa: E501
        :rtype: V1ContainerStateWaiting
        """
        return self._waiting

    @waiting.setter
    def waiting(self, waiting):
        """Sets the waiting of this V1ContainerState.


        :param waiting: The waiting of this V1ContainerState.  # noqa: E501
        :type: V1ContainerStateWaiting
        """

        self._waiting = waiting

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
        if not isinstance(other, V1ContainerState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ContainerState):
            return True

        return self.to_dict() != other.to_dict()
