# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1beta1DaemonSetSpec(object):
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
        'min_ready_seconds': 'int',
        'revision_history_limit': 'int',
        'selector': 'V1LabelSelector',
        'template': 'V1PodTemplateSpec',
        'template_generation': 'int',
        'update_strategy': 'V1beta1DaemonSetUpdateStrategy'
    }

    attribute_map = {
        'min_ready_seconds': 'minReadySeconds',
        'revision_history_limit': 'revisionHistoryLimit',
        'selector': 'selector',
        'template': 'template',
        'template_generation': 'templateGeneration',
        'update_strategy': 'updateStrategy'
    }

    def __init__(self, min_ready_seconds=None, revision_history_limit=None, selector=None, template=None, template_generation=None, update_strategy=None):
        """
        V1beta1DaemonSetSpec - a model defined in Swagger
        """

        self._min_ready_seconds = None
        self._revision_history_limit = None
        self._selector = None
        self._template = None
        self._template_generation = None
        self._update_strategy = None
        self.discriminator = None

        if min_ready_seconds is not None:
          self.min_ready_seconds = min_ready_seconds
        if revision_history_limit is not None:
          self.revision_history_limit = revision_history_limit
        if selector is not None:
          self.selector = selector
        self.template = template
        if template_generation is not None:
          self.template_generation = template_generation
        if update_strategy is not None:
          self.update_strategy = update_strategy

    @property
    def min_ready_seconds(self):
        """
        Gets the min_ready_seconds of this V1beta1DaemonSetSpec.
        The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).

        :return: The min_ready_seconds of this V1beta1DaemonSetSpec.
        :rtype: int
        """
        return self._min_ready_seconds

    @min_ready_seconds.setter
    def min_ready_seconds(self, min_ready_seconds):
        """
        Sets the min_ready_seconds of this V1beta1DaemonSetSpec.
        The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).

        :param min_ready_seconds: The min_ready_seconds of this V1beta1DaemonSetSpec.
        :type: int
        """

        self._min_ready_seconds = min_ready_seconds

    @property
    def revision_history_limit(self):
        """
        Gets the revision_history_limit of this V1beta1DaemonSetSpec.
        The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.

        :return: The revision_history_limit of this V1beta1DaemonSetSpec.
        :rtype: int
        """
        return self._revision_history_limit

    @revision_history_limit.setter
    def revision_history_limit(self, revision_history_limit):
        """
        Sets the revision_history_limit of this V1beta1DaemonSetSpec.
        The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.

        :param revision_history_limit: The revision_history_limit of this V1beta1DaemonSetSpec.
        :type: int
        """

        self._revision_history_limit = revision_history_limit

    @property
    def selector(self):
        """
        Gets the selector of this V1beta1DaemonSetSpec.
        A label query over pods that are managed by the daemon set. Must match in order to be controlled. If empty, defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

        :return: The selector of this V1beta1DaemonSetSpec.
        :rtype: V1LabelSelector
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1beta1DaemonSetSpec.
        A label query over pods that are managed by the daemon set. Must match in order to be controlled. If empty, defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

        :param selector: The selector of this V1beta1DaemonSetSpec.
        :type: V1LabelSelector
        """

        self._selector = selector

    @property
    def template(self):
        """
        Gets the template of this V1beta1DaemonSetSpec.
        An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template

        :return: The template of this V1beta1DaemonSetSpec.
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this V1beta1DaemonSetSpec.
        An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template's node selector (or on every node if no node selector is specified). More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template

        :param template: The template of this V1beta1DaemonSetSpec.
        :type: V1PodTemplateSpec
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")

        self._template = template

    @property
    def template_generation(self):
        """
        Gets the template_generation of this V1beta1DaemonSetSpec.
        DEPRECATED. A sequence number representing a specific generation of the template. Populated by the system. It can be set only during the creation.

        :return: The template_generation of this V1beta1DaemonSetSpec.
        :rtype: int
        """
        return self._template_generation

    @template_generation.setter
    def template_generation(self, template_generation):
        """
        Sets the template_generation of this V1beta1DaemonSetSpec.
        DEPRECATED. A sequence number representing a specific generation of the template. Populated by the system. It can be set only during the creation.

        :param template_generation: The template_generation of this V1beta1DaemonSetSpec.
        :type: int
        """

        self._template_generation = template_generation

    @property
    def update_strategy(self):
        """
        Gets the update_strategy of this V1beta1DaemonSetSpec.
        An update strategy to replace existing DaemonSet pods with new pods.

        :return: The update_strategy of this V1beta1DaemonSetSpec.
        :rtype: V1beta1DaemonSetUpdateStrategy
        """
        return self._update_strategy

    @update_strategy.setter
    def update_strategy(self, update_strategy):
        """
        Sets the update_strategy of this V1beta1DaemonSetSpec.
        An update strategy to replace existing DaemonSet pods with new pods.

        :param update_strategy: The update_strategy of this V1beta1DaemonSetSpec.
        :type: V1beta1DaemonSetUpdateStrategy
        """

        self._update_strategy = update_strategy

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
        if not isinstance(other, V1beta1DaemonSetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
