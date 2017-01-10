# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.1-660c2a2
    
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


class V1PersistentVolumeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_modes=None, aws_elastic_block_store=None, azure_disk=None, azure_file=None, capacity=None, cephfs=None, cinder=None, claim_ref=None, fc=None, flex_volume=None, flocker=None, gce_persistent_disk=None, glusterfs=None, host_path=None, iscsi=None, nfs=None, persistent_volume_reclaim_policy=None, photon_persistent_disk=None, quobyte=None, rbd=None, vsphere_volume=None):
        """
        V1PersistentVolumeSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_modes': 'list[str]',
            'aws_elastic_block_store': 'V1AWSElasticBlockStoreVolumeSource',
            'azure_disk': 'V1AzureDiskVolumeSource',
            'azure_file': 'V1AzureFileVolumeSource',
            'capacity': 'dict(str, ResourceQuantity)',
            'cephfs': 'V1CephFSVolumeSource',
            'cinder': 'V1CinderVolumeSource',
            'claim_ref': 'V1ObjectReference',
            'fc': 'V1FCVolumeSource',
            'flex_volume': 'V1FlexVolumeSource',
            'flocker': 'V1FlockerVolumeSource',
            'gce_persistent_disk': 'V1GCEPersistentDiskVolumeSource',
            'glusterfs': 'V1GlusterfsVolumeSource',
            'host_path': 'V1HostPathVolumeSource',
            'iscsi': 'V1ISCSIVolumeSource',
            'nfs': 'V1NFSVolumeSource',
            'persistent_volume_reclaim_policy': 'str',
            'photon_persistent_disk': 'V1PhotonPersistentDiskVolumeSource',
            'quobyte': 'V1QuobyteVolumeSource',
            'rbd': 'V1RBDVolumeSource',
            'vsphere_volume': 'V1VsphereVirtualDiskVolumeSource'
        }

        self.attribute_map = {
            'access_modes': 'accessModes',
            'aws_elastic_block_store': 'awsElasticBlockStore',
            'azure_disk': 'azureDisk',
            'azure_file': 'azureFile',
            'capacity': 'capacity',
            'cephfs': 'cephfs',
            'cinder': 'cinder',
            'claim_ref': 'claimRef',
            'fc': 'fc',
            'flex_volume': 'flexVolume',
            'flocker': 'flocker',
            'gce_persistent_disk': 'gcePersistentDisk',
            'glusterfs': 'glusterfs',
            'host_path': 'hostPath',
            'iscsi': 'iscsi',
            'nfs': 'nfs',
            'persistent_volume_reclaim_policy': 'persistentVolumeReclaimPolicy',
            'photon_persistent_disk': 'photonPersistentDisk',
            'quobyte': 'quobyte',
            'rbd': 'rbd',
            'vsphere_volume': 'vsphereVolume'
        }

        self._access_modes = access_modes
        self._aws_elastic_block_store = aws_elastic_block_store
        self._azure_disk = azure_disk
        self._azure_file = azure_file
        self._capacity = capacity
        self._cephfs = cephfs
        self._cinder = cinder
        self._claim_ref = claim_ref
        self._fc = fc
        self._flex_volume = flex_volume
        self._flocker = flocker
        self._gce_persistent_disk = gce_persistent_disk
        self._glusterfs = glusterfs
        self._host_path = host_path
        self._iscsi = iscsi
        self._nfs = nfs
        self._persistent_volume_reclaim_policy = persistent_volume_reclaim_policy
        self._photon_persistent_disk = photon_persistent_disk
        self._quobyte = quobyte
        self._rbd = rbd
        self._vsphere_volume = vsphere_volume


    @property
    def access_modes(self):
        """
        Gets the access_modes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes

        :return: The access_modes of this V1PersistentVolumeSpec.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this V1PersistentVolumeSpec.
        AccessModes contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes

        :param access_modes: The access_modes of this V1PersistentVolumeSpec.
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def aws_elastic_block_store(self):
        """
        Gets the aws_elastic_block_store of this V1PersistentVolumeSpec.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        :return: The aws_elastic_block_store of this V1PersistentVolumeSpec.
        :rtype: V1AWSElasticBlockStoreVolumeSource
        """
        return self._aws_elastic_block_store

    @aws_elastic_block_store.setter
    def aws_elastic_block_store(self, aws_elastic_block_store):
        """
        Sets the aws_elastic_block_store of this V1PersistentVolumeSpec.
        AWSElasticBlockStore represents an AWS Disk resource that is attached to a kubelet's host machine and then exposed to the pod. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        :param aws_elastic_block_store: The aws_elastic_block_store of this V1PersistentVolumeSpec.
        :type: V1AWSElasticBlockStoreVolumeSource
        """

        self._aws_elastic_block_store = aws_elastic_block_store

    @property
    def azure_disk(self):
        """
        Gets the azure_disk of this V1PersistentVolumeSpec.
        AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

        :return: The azure_disk of this V1PersistentVolumeSpec.
        :rtype: V1AzureDiskVolumeSource
        """
        return self._azure_disk

    @azure_disk.setter
    def azure_disk(self, azure_disk):
        """
        Sets the azure_disk of this V1PersistentVolumeSpec.
        AzureDisk represents an Azure Data Disk mount on the host and bind mount to the pod.

        :param azure_disk: The azure_disk of this V1PersistentVolumeSpec.
        :type: V1AzureDiskVolumeSource
        """

        self._azure_disk = azure_disk

    @property
    def azure_file(self):
        """
        Gets the azure_file of this V1PersistentVolumeSpec.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :return: The azure_file of this V1PersistentVolumeSpec.
        :rtype: V1AzureFileVolumeSource
        """
        return self._azure_file

    @azure_file.setter
    def azure_file(self, azure_file):
        """
        Sets the azure_file of this V1PersistentVolumeSpec.
        AzureFile represents an Azure File Service mount on the host and bind mount to the pod.

        :param azure_file: The azure_file of this V1PersistentVolumeSpec.
        :type: V1AzureFileVolumeSource
        """

        self._azure_file = azure_file

    @property
    def capacity(self):
        """
        Gets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity

        :return: The capacity of this V1PersistentVolumeSpec.
        :rtype: dict(str, ResourceQuantity)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1PersistentVolumeSpec.
        A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity

        :param capacity: The capacity of this V1PersistentVolumeSpec.
        :type: dict(str, ResourceQuantity)
        """

        self._capacity = capacity

    @property
    def cephfs(self):
        """
        Gets the cephfs of this V1PersistentVolumeSpec.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :return: The cephfs of this V1PersistentVolumeSpec.
        :rtype: V1CephFSVolumeSource
        """
        return self._cephfs

    @cephfs.setter
    def cephfs(self, cephfs):
        """
        Sets the cephfs of this V1PersistentVolumeSpec.
        CephFS represents a Ceph FS mount on the host that shares a pod's lifetime

        :param cephfs: The cephfs of this V1PersistentVolumeSpec.
        :type: V1CephFSVolumeSource
        """

        self._cephfs = cephfs

    @property
    def cinder(self):
        """
        Gets the cinder of this V1PersistentVolumeSpec.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :return: The cinder of this V1PersistentVolumeSpec.
        :rtype: V1CinderVolumeSource
        """
        return self._cinder

    @cinder.setter
    def cinder(self, cinder):
        """
        Sets the cinder of this V1PersistentVolumeSpec.
        Cinder represents a cinder volume attached and mounted on kubelets host machine More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        :param cinder: The cinder of this V1PersistentVolumeSpec.
        :type: V1CinderVolumeSource
        """

        self._cinder = cinder

    @property
    def claim_ref(self):
        """
        Gets the claim_ref of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#binding

        :return: The claim_ref of this V1PersistentVolumeSpec.
        :rtype: V1ObjectReference
        """
        return self._claim_ref

    @claim_ref.setter
    def claim_ref(self, claim_ref):
        """
        Sets the claim_ref of this V1PersistentVolumeSpec.
        ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#binding

        :param claim_ref: The claim_ref of this V1PersistentVolumeSpec.
        :type: V1ObjectReference
        """

        self._claim_ref = claim_ref

    @property
    def fc(self):
        """
        Gets the fc of this V1PersistentVolumeSpec.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :return: The fc of this V1PersistentVolumeSpec.
        :rtype: V1FCVolumeSource
        """
        return self._fc

    @fc.setter
    def fc(self, fc):
        """
        Sets the fc of this V1PersistentVolumeSpec.
        FC represents a Fibre Channel resource that is attached to a kubelet's host machine and then exposed to the pod.

        :param fc: The fc of this V1PersistentVolumeSpec.
        :type: V1FCVolumeSource
        """

        self._fc = fc

    @property
    def flex_volume(self):
        """
        Gets the flex_volume of this V1PersistentVolumeSpec.
        FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. This is an alpha feature and may change in future.

        :return: The flex_volume of this V1PersistentVolumeSpec.
        :rtype: V1FlexVolumeSource
        """
        return self._flex_volume

    @flex_volume.setter
    def flex_volume(self, flex_volume):
        """
        Sets the flex_volume of this V1PersistentVolumeSpec.
        FlexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. This is an alpha feature and may change in future.

        :param flex_volume: The flex_volume of this V1PersistentVolumeSpec.
        :type: V1FlexVolumeSource
        """

        self._flex_volume = flex_volume

    @property
    def flocker(self):
        """
        Gets the flocker of this V1PersistentVolumeSpec.
        Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

        :return: The flocker of this V1PersistentVolumeSpec.
        :rtype: V1FlockerVolumeSource
        """
        return self._flocker

    @flocker.setter
    def flocker(self, flocker):
        """
        Sets the flocker of this V1PersistentVolumeSpec.
        Flocker represents a Flocker volume attached to a kubelet's host machine and exposed to the pod for its usage. This depends on the Flocker control service being running

        :param flocker: The flocker of this V1PersistentVolumeSpec.
        :type: V1FlockerVolumeSource
        """

        self._flocker = flocker

    @property
    def gce_persistent_disk(self):
        """
        Gets the gce_persistent_disk of this V1PersistentVolumeSpec.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :return: The gce_persistent_disk of this V1PersistentVolumeSpec.
        :rtype: V1GCEPersistentDiskVolumeSource
        """
        return self._gce_persistent_disk

    @gce_persistent_disk.setter
    def gce_persistent_disk(self, gce_persistent_disk):
        """
        Sets the gce_persistent_disk of this V1PersistentVolumeSpec.
        GCEPersistentDisk represents a GCE Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        :param gce_persistent_disk: The gce_persistent_disk of this V1PersistentVolumeSpec.
        :type: V1GCEPersistentDiskVolumeSource
        """

        self._gce_persistent_disk = gce_persistent_disk

    @property
    def glusterfs(self):
        """
        Gets the glusterfs of this V1PersistentVolumeSpec.
        Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :return: The glusterfs of this V1PersistentVolumeSpec.
        :rtype: V1GlusterfsVolumeSource
        """
        return self._glusterfs

    @glusterfs.setter
    def glusterfs(self, glusterfs):
        """
        Sets the glusterfs of this V1PersistentVolumeSpec.
        Glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md

        :param glusterfs: The glusterfs of this V1PersistentVolumeSpec.
        :type: V1GlusterfsVolumeSource
        """

        self._glusterfs = glusterfs

    @property
    def host_path(self):
        """
        Gets the host_path of this V1PersistentVolumeSpec.
        HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath

        :return: The host_path of this V1PersistentVolumeSpec.
        :rtype: V1HostPathVolumeSource
        """
        return self._host_path

    @host_path.setter
    def host_path(self, host_path):
        """
        Sets the host_path of this V1PersistentVolumeSpec.
        HostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath

        :param host_path: The host_path of this V1PersistentVolumeSpec.
        :type: V1HostPathVolumeSource
        """

        self._host_path = host_path

    @property
    def iscsi(self):
        """
        Gets the iscsi of this V1PersistentVolumeSpec.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

        :return: The iscsi of this V1PersistentVolumeSpec.
        :rtype: V1ISCSIVolumeSource
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """
        Sets the iscsi of this V1PersistentVolumeSpec.
        ISCSI represents an ISCSI Disk resource that is attached to a kubelet's host machine and then exposed to the pod. Provisioned by an admin.

        :param iscsi: The iscsi of this V1PersistentVolumeSpec.
        :type: V1ISCSIVolumeSource
        """

        self._iscsi = iscsi

    @property
    def nfs(self):
        """
        Gets the nfs of this V1PersistentVolumeSpec.
        NFS represents an NFS mount on the host. Provisioned by an admin. More info: http://kubernetes.io/docs/user-guide/volumes#nfs

        :return: The nfs of this V1PersistentVolumeSpec.
        :rtype: V1NFSVolumeSource
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """
        Sets the nfs of this V1PersistentVolumeSpec.
        NFS represents an NFS mount on the host. Provisioned by an admin. More info: http://kubernetes.io/docs/user-guide/volumes#nfs

        :param nfs: The nfs of this V1PersistentVolumeSpec.
        :type: V1NFSVolumeSource
        """

        self._nfs = nfs

    @property
    def persistent_volume_reclaim_policy(self):
        """
        Gets the persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy

        :return: The persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        :rtype: str
        """
        return self._persistent_volume_reclaim_policy

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, persistent_volume_reclaim_policy):
        """
        Sets the persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy

        :param persistent_volume_reclaim_policy: The persistent_volume_reclaim_policy of this V1PersistentVolumeSpec.
        :type: str
        """

        self._persistent_volume_reclaim_policy = persistent_volume_reclaim_policy

    @property
    def photon_persistent_disk(self):
        """
        Gets the photon_persistent_disk of this V1PersistentVolumeSpec.
        PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine

        :return: The photon_persistent_disk of this V1PersistentVolumeSpec.
        :rtype: V1PhotonPersistentDiskVolumeSource
        """
        return self._photon_persistent_disk

    @photon_persistent_disk.setter
    def photon_persistent_disk(self, photon_persistent_disk):
        """
        Sets the photon_persistent_disk of this V1PersistentVolumeSpec.
        PhotonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine

        :param photon_persistent_disk: The photon_persistent_disk of this V1PersistentVolumeSpec.
        :type: V1PhotonPersistentDiskVolumeSource
        """

        self._photon_persistent_disk = photon_persistent_disk

    @property
    def quobyte(self):
        """
        Gets the quobyte of this V1PersistentVolumeSpec.
        Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

        :return: The quobyte of this V1PersistentVolumeSpec.
        :rtype: V1QuobyteVolumeSource
        """
        return self._quobyte

    @quobyte.setter
    def quobyte(self, quobyte):
        """
        Sets the quobyte of this V1PersistentVolumeSpec.
        Quobyte represents a Quobyte mount on the host that shares a pod's lifetime

        :param quobyte: The quobyte of this V1PersistentVolumeSpec.
        :type: V1QuobyteVolumeSource
        """

        self._quobyte = quobyte

    @property
    def rbd(self):
        """
        Gets the rbd of this V1PersistentVolumeSpec.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :return: The rbd of this V1PersistentVolumeSpec.
        :rtype: V1RBDVolumeSource
        """
        return self._rbd

    @rbd.setter
    def rbd(self, rbd):
        """
        Sets the rbd of this V1PersistentVolumeSpec.
        RBD represents a Rados Block Device mount on the host that shares a pod's lifetime. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md

        :param rbd: The rbd of this V1PersistentVolumeSpec.
        :type: V1RBDVolumeSource
        """

        self._rbd = rbd

    @property
    def vsphere_volume(self):
        """
        Gets the vsphere_volume of this V1PersistentVolumeSpec.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :return: The vsphere_volume of this V1PersistentVolumeSpec.
        :rtype: V1VsphereVirtualDiskVolumeSource
        """
        return self._vsphere_volume

    @vsphere_volume.setter
    def vsphere_volume(self, vsphere_volume):
        """
        Sets the vsphere_volume of this V1PersistentVolumeSpec.
        VsphereVolume represents a vSphere volume attached and mounted on kubelets host machine

        :param vsphere_volume: The vsphere_volume of this V1PersistentVolumeSpec.
        :type: V1VsphereVirtualDiskVolumeSource
        """

        self._vsphere_volume = vsphere_volume

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
