# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1alpha1CertificateSigningRequestSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, groups=None, request=None, uid=None, username=None):
        """
        V1alpha1CertificateSigningRequestSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'groups': 'list[str]',
            'request': 'str',
            'uid': 'str',
            'username': 'str'
        }

        self.attribute_map = {
            'groups': 'groups',
            'request': 'request',
            'uid': 'uid',
            'username': 'username'
        }

        self._groups = groups
        self._request = request
        self._uid = uid
        self._username = username


    @property
    def groups(self):
        """
        Gets the groups of this V1alpha1CertificateSigningRequestSpec.


        :return: The groups of this V1alpha1CertificateSigningRequestSpec.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this V1alpha1CertificateSigningRequestSpec.


        :param groups: The groups of this V1alpha1CertificateSigningRequestSpec.
        :type: list[str]
        """

        self._groups = groups

    @property
    def request(self):
        """
        Gets the request of this V1alpha1CertificateSigningRequestSpec.
        Base64-encoded PKCS#10 CSR data

        :return: The request of this V1alpha1CertificateSigningRequestSpec.
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """
        Sets the request of this V1alpha1CertificateSigningRequestSpec.
        Base64-encoded PKCS#10 CSR data

        :param request: The request of this V1alpha1CertificateSigningRequestSpec.
        :type: str
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")

        self._request = request

    @property
    def uid(self):
        """
        Gets the uid of this V1alpha1CertificateSigningRequestSpec.


        :return: The uid of this V1alpha1CertificateSigningRequestSpec.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this V1alpha1CertificateSigningRequestSpec.


        :param uid: The uid of this V1alpha1CertificateSigningRequestSpec.
        :type: str
        """

        self._uid = uid

    @property
    def username(self):
        """
        Gets the username of this V1alpha1CertificateSigningRequestSpec.
        Information about the requesting user (if relevant) See user.Info interface for details

        :return: The username of this V1alpha1CertificateSigningRequestSpec.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this V1alpha1CertificateSigningRequestSpec.
        Information about the requesting user (if relevant) See user.Info interface for details

        :param username: The username of this V1alpha1CertificateSigningRequestSpec.
        :type: str
        """

        self._username = username

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
