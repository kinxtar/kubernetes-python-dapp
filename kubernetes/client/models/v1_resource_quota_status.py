# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.13.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ResourceQuotaStatus(object):
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
        'hard': 'dict(str, str)',
        'used': 'dict(str, str)'
    }

    attribute_map = {
        'hard': 'hard',
        'used': 'used'
    }

    def __init__(self, hard=None, used=None):
        """
        V1ResourceQuotaStatus - a model defined in Swagger
        """

        self._hard = None
        self._used = None
        self.discriminator = None

        if hard is not None:
          self.hard = hard
        if used is not None:
          self.used = used

    @property
    def hard(self):
        """
        Gets the hard of this V1ResourceQuotaStatus.
        Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/

        :return: The hard of this V1ResourceQuotaStatus.
        :rtype: dict(str, str)
        """
        return self._hard

    @hard.setter
    def hard(self, hard):
        """
        Sets the hard of this V1ResourceQuotaStatus.
        Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/

        :param hard: The hard of this V1ResourceQuotaStatus.
        :type: dict(str, str)
        """

        self._hard = hard

    @property
    def used(self):
        """
        Gets the used of this V1ResourceQuotaStatus.
        Used is the current observed total usage of the resource in the namespace.

        :return: The used of this V1ResourceQuotaStatus.
        :rtype: dict(str, str)
        """
        return self._used

    @used.setter
    def used(self, used):
        """
        Sets the used of this V1ResourceQuotaStatus.
        Used is the current observed total usage of the resource in the namespace.

        :param used: The used of this V1ResourceQuotaStatus.
        :type: dict(str, str)
        """

        self._used = used

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
        if not isinstance(other, V1ResourceQuotaStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
