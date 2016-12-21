# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup

from scripts.constants import CLIENT_VERSION, PACKAGE_NAME

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3 >= 1.19",
    "six >= 1.10",
    "certifi",
    "python-dateutil",
    "pyyaml",
    "oauth2client",
    "ipaddress"]

setup(
    name=PACKAGE_NAME,
    version=CLIENT_VERSION,
    description="Kubernetes python client",
    author_email="",
    author="Kubernetes",
    license="Apache License Version 2.0",
    url="https://github.com/kubernetes-incubator/client-python",
    keywords=["Swagger", "OpenAPI", "Kubernetes"],
    install_requires=REQUIRES,
    packages=['kubernetes', 'kubernetes.client', 'kubernetes.config',
              'kubernetes.watch', 'kubernetes.client.apis',
              'kubernetes.client.models', 'scripts'],
    include_package_data=True,
    long_description="""\
    Python client for kubernetes http://kubernetes.io/
    """
)
