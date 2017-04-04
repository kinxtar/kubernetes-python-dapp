# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1GitRepoVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, directory=None, repository=None, revision=None):
        """
        V1GitRepoVolumeSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'directory': 'str',
            'repository': 'str',
            'revision': 'str'
        }

        self.attribute_map = {
            'directory': 'directory',
            'repository': 'repository',
            'revision': 'revision'
        }

        self._directory = directory
        self._repository = repository
        self._revision = revision

    @property
    def directory(self):
        """
        Gets the directory of this V1GitRepoVolumeSource.
        Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.

        :return: The directory of this V1GitRepoVolumeSource.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """
        Sets the directory of this V1GitRepoVolumeSource.
        Target directory name. Must not contain or start with '..'.  If '.' is supplied, the volume directory will be the git repository.  Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.

        :param directory: The directory of this V1GitRepoVolumeSource.
        :type: str
        """

        self._directory = directory

    @property
    def repository(self):
        """
        Gets the repository of this V1GitRepoVolumeSource.
        Repository URL

        :return: The repository of this V1GitRepoVolumeSource.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """
        Sets the repository of this V1GitRepoVolumeSource.
        Repository URL

        :param repository: The repository of this V1GitRepoVolumeSource.
        :type: str
        """
        if repository is None:
            raise ValueError("Invalid value for `repository`, must not be `None`")

        self._repository = repository

    @property
    def revision(self):
        """
        Gets the revision of this V1GitRepoVolumeSource.
        Commit hash for the specified revision.

        :return: The revision of this V1GitRepoVolumeSource.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this V1GitRepoVolumeSource.
        Commit hash for the specified revision.

        :param revision: The revision of this V1GitRepoVolumeSource.
        :type: str
        """

        self._revision = revision

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
