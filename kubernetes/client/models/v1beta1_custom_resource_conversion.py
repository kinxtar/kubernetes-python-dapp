# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.20
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1CustomResourceConversion(object):
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
        'conversion_review_versions': 'list[str]',
        'strategy': 'str',
        'webhook_client_config': 'ApiextensionsV1beta1WebhookClientConfig'
    }

    attribute_map = {
        'conversion_review_versions': 'conversionReviewVersions',
        'strategy': 'strategy',
        'webhook_client_config': 'webhookClientConfig'
    }

    def __init__(self, conversion_review_versions=None, strategy=None, webhook_client_config=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1CustomResourceConversion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conversion_review_versions = None
        self._strategy = None
        self._webhook_client_config = None
        self.discriminator = None

        if conversion_review_versions is not None:
            self.conversion_review_versions = conversion_review_versions
        self.strategy = strategy
        if webhook_client_config is not None:
            self.webhook_client_config = webhook_client_config

    @property
    def conversion_review_versions(self):
        """Gets the conversion_review_versions of this V1beta1CustomResourceConversion.  # noqa: E501

        conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. Defaults to `[\"v1beta1\"]`.  # noqa: E501

        :return: The conversion_review_versions of this V1beta1CustomResourceConversion.  # noqa: E501
        :rtype: list[str]
        """
        return self._conversion_review_versions

    @conversion_review_versions.setter
    def conversion_review_versions(self, conversion_review_versions):
        """Sets the conversion_review_versions of this V1beta1CustomResourceConversion.

        conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail. Defaults to `[\"v1beta1\"]`.  # noqa: E501

        :param conversion_review_versions: The conversion_review_versions of this V1beta1CustomResourceConversion.  # noqa: E501
        :type: list[str]
        """

        self._conversion_review_versions = conversion_review_versions

    @property
    def strategy(self):
        """Gets the strategy of this V1beta1CustomResourceConversion.  # noqa: E501

        strategy specifies how custom resources are converted between versions. Allowed values are: - `None`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `Webhook`: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhookClientConfig to be set.  # noqa: E501

        :return: The strategy of this V1beta1CustomResourceConversion.  # noqa: E501
        :rtype: str
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """Sets the strategy of this V1beta1CustomResourceConversion.

        strategy specifies how custom resources are converted between versions. Allowed values are: - `None`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `Webhook`: API Server will call to an external webhook to do the conversion. Additional information   is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhookClientConfig to be set.  # noqa: E501

        :param strategy: The strategy of this V1beta1CustomResourceConversion.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and strategy is None:  # noqa: E501
            raise ValueError("Invalid value for `strategy`, must not be `None`")  # noqa: E501

        self._strategy = strategy

    @property
    def webhook_client_config(self):
        """Gets the webhook_client_config of this V1beta1CustomResourceConversion.  # noqa: E501


        :return: The webhook_client_config of this V1beta1CustomResourceConversion.  # noqa: E501
        :rtype: ApiextensionsV1beta1WebhookClientConfig
        """
        return self._webhook_client_config

    @webhook_client_config.setter
    def webhook_client_config(self, webhook_client_config):
        """Sets the webhook_client_config of this V1beta1CustomResourceConversion.


        :param webhook_client_config: The webhook_client_config of this V1beta1CustomResourceConversion.  # noqa: E501
        :type: ApiextensionsV1beta1WebhookClientConfig
        """

        self._webhook_client_config = webhook_client_config

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
        if not isinstance(other, V1beta1CustomResourceConversion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1CustomResourceConversion):
            return True

        return self.to_dict() != other.to_dict()
