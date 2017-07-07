# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1StatusDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, causes=None, group=None, kind=None, name=None, retry_after_seconds=None, uid=None):
        """
        V1StatusDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'causes': 'list[V1StatusCause]',
            'group': 'str',
            'kind': 'str',
            'name': 'str',
            'retry_after_seconds': 'int',
            'uid': 'str'
        }

        self.attribute_map = {
            'causes': 'causes',
            'group': 'group',
            'kind': 'kind',
            'name': 'name',
            'retry_after_seconds': 'retryAfterSeconds',
            'uid': 'uid'
        }

        self._causes = causes
        self._group = group
        self._kind = kind
        self._name = name
        self._retry_after_seconds = retry_after_seconds
        self._uid = uid

    @property
    def causes(self):
        """
        Gets the causes of this V1StatusDetails.
        The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.

        :return: The causes of this V1StatusDetails.
        :rtype: list[V1StatusCause]
        """
        return self._causes

    @causes.setter
    def causes(self, causes):
        """
        Sets the causes of this V1StatusDetails.
        The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.

        :param causes: The causes of this V1StatusDetails.
        :type: list[V1StatusCause]
        """

        self._causes = causes

    @property
    def group(self):
        """
        Gets the group of this V1StatusDetails.
        The group attribute of the resource associated with the status StatusReason.

        :return: The group of this V1StatusDetails.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this V1StatusDetails.
        The group attribute of the resource associated with the status StatusReason.

        :param group: The group of this V1StatusDetails.
        :type: str
        """

        self._group = group

    @property
    def kind(self):
        """
        Gets the kind of this V1StatusDetails.
        The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1StatusDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1StatusDetails.
        The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1StatusDetails.
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1StatusDetails.
        The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).

        :return: The name of this V1StatusDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1StatusDetails.
        The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).

        :param name: The name of this V1StatusDetails.
        :type: str
        """

        self._name = name

    @property
    def retry_after_seconds(self):
        """
        Gets the retry_after_seconds of this V1StatusDetails.
        If specified, the time in seconds before the operation should be retried.

        :return: The retry_after_seconds of this V1StatusDetails.
        :rtype: int
        """
        return self._retry_after_seconds

    @retry_after_seconds.setter
    def retry_after_seconds(self, retry_after_seconds):
        """
        Sets the retry_after_seconds of this V1StatusDetails.
        If specified, the time in seconds before the operation should be retried.

        :param retry_after_seconds: The retry_after_seconds of this V1StatusDetails.
        :type: int
        """

        self._retry_after_seconds = retry_after_seconds

    @property
    def uid(self):
        """
        Gets the uid of this V1StatusDetails.
        UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids

        :return: The uid of this V1StatusDetails.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this V1StatusDetails.
        UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids

        :param uid: The uid of this V1StatusDetails.
        :type: str
        """

        self._uid = uid

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
        if not isinstance(other, V1StatusDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
