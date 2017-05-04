# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1ReplicationController(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, kind=None, metadata=None, spec=None, status=None):
        """
        V1ReplicationController - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'kind': 'str',
            'metadata': 'V1ObjectMeta',
            'spec': 'V1ReplicationControllerSpec',
            'status': 'V1ReplicationControllerStatus'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'metadata': 'metadata',
            'spec': 'spec',
            'status': 'status'
        }

        self._api_version = api_version
        self._kind = kind
        self._metadata = metadata
        self._spec = spec
        self._status = status

    @property
    def api_version(self):
        """
        Gets the api_version of this V1ReplicationController.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1ReplicationController.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1ReplicationController.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1ReplicationController.
        :type: str
        """

        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind of this V1ReplicationController.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1ReplicationController.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1ReplicationController.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1ReplicationController.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1ReplicationController.
        If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :return: The metadata of this V1ReplicationController.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1ReplicationController.
        If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object's metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata

        :param metadata: The metadata of this V1ReplicationController.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def spec(self):
        """
        Gets the spec of this V1ReplicationController.
        Spec defines the specification of the desired behavior of the replication controller. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status

        :return: The spec of this V1ReplicationController.
        :rtype: V1ReplicationControllerSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """
        Sets the spec of this V1ReplicationController.
        Spec defines the specification of the desired behavior of the replication controller. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status

        :param spec: The spec of this V1ReplicationController.
        :type: V1ReplicationControllerSpec
        """

        self._spec = spec

    @property
    def status(self):
        """
        Gets the status of this V1ReplicationController.
        Status is the most recently observed status of the replication controller. This data may be out of date by some window of time. Populated by the system. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status

        :return: The status of this V1ReplicationController.
        :rtype: V1ReplicationControllerStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1ReplicationController.
        Status is the most recently observed status of the replication controller. This data may be out of date by some window of time. Populated by the system. Read-only. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#spec-and-status

        :param status: The status of this V1ReplicationController.
        :type: V1ReplicationControllerStatus
        """

        self._status = status

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
        if not isinstance(other, V1ReplicationController):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
