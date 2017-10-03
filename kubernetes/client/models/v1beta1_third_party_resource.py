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


class V1beta1ThirdPartyResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, description=None, kind=None, metadata=None, versions=None):
        """
        V1beta1ThirdPartyResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'description': 'str',
            'kind': 'str',
            'metadata': 'V1ObjectMeta',
            'versions': 'list[V1beta1APIVersion]'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'description': 'description',
            'kind': 'kind',
            'metadata': 'metadata',
            'versions': 'versions'
        }

        self._api_version = api_version
        self._description = description
        self._kind = kind
        self._metadata = metadata
        self._versions = versions

    @property
    def api_version(self):
        """
        Gets the api_version of this V1beta1ThirdPartyResource.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :return: The api_version of this V1beta1ThirdPartyResource.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1beta1ThirdPartyResource.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1beta1ThirdPartyResource.
        :type: str
        """

        self._api_version = api_version

    @property
    def description(self):
        """
        Gets the description of this V1beta1ThirdPartyResource.
        Description is the description of this object.

        :return: The description of this V1beta1ThirdPartyResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this V1beta1ThirdPartyResource.
        Description is the description of this object.

        :param description: The description of this V1beta1ThirdPartyResource.
        :type: str
        """

        self._description = description

    @property
    def kind(self):
        """
        Gets the kind of this V1beta1ThirdPartyResource.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :return: The kind of this V1beta1ThirdPartyResource.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1beta1ThirdPartyResource.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1beta1ThirdPartyResource.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1beta1ThirdPartyResource.
        Standard object metadata

        :return: The metadata of this V1beta1ThirdPartyResource.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1beta1ThirdPartyResource.
        Standard object metadata

        :param metadata: The metadata of this V1beta1ThirdPartyResource.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def versions(self):
        """
        Gets the versions of this V1beta1ThirdPartyResource.
        Versions are versions for this third party object

        :return: The versions of this V1beta1ThirdPartyResource.
        :rtype: list[V1beta1APIVersion]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """
        Sets the versions of this V1beta1ThirdPartyResource.
        Versions are versions for this third party object

        :param versions: The versions of this V1beta1ThirdPartyResource.
        :type: list[V1beta1APIVersion]
        """

        self._versions = versions

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
        if not isinstance(other, V1beta1ThirdPartyResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
