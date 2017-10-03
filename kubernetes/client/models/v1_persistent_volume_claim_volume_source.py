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


class V1PersistentVolumeClaimVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, claim_name=None, read_only=None):
        """
        V1PersistentVolumeClaimVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'claim_name': 'str',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'claim_name': 'claimName',
            'read_only': 'readOnly'
        }

        self._claim_name = claim_name
        self._read_only = read_only

    @property
    def claim_name(self):
        """
        Gets the claim_name of this V1PersistentVolumeClaimVolumeSource.
        ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

        :return: The claim_name of this V1PersistentVolumeClaimVolumeSource.
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """
        Sets the claim_name of this V1PersistentVolumeClaimVolumeSource.
        ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

        :param claim_name: The claim_name of this V1PersistentVolumeClaimVolumeSource.
        :type: str
        """
        if claim_name is None:
            raise ValueError("Invalid value for `claim_name`, must not be `None`")

        self._claim_name = claim_name

    @property
    def read_only(self):
        """
        Gets the read_only of this V1PersistentVolumeClaimVolumeSource.
        Will force the ReadOnly setting in VolumeMounts. Default false.

        :return: The read_only of this V1PersistentVolumeClaimVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1PersistentVolumeClaimVolumeSource.
        Will force the ReadOnly setting in VolumeMounts. Default false.

        :param read_only: The read_only of this V1PersistentVolumeClaimVolumeSource.
        :type: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, V1PersistentVolumeClaimVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
