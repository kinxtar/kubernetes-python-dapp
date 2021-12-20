#!/bin/sh

# Copyright 2020 The Kubernetes Authors.
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

# Script to apply hotfixes after generating the client
# More details: https://github.com/kubernetes-client/python/blob/master/devel/release.md#hot-issues

# Check if working directory is dirty
if [ $(git status --porcelain | wc -l) -gt 0 ]
then
    echo Your working directory is not clean. Please clean your working directory.
    exit 1
fi

# Patching commit for custom client behavior
# UPDATE: The commit being cherry-picked is updated since the the client generated in 1adaaecd0879d7315f48259ad8d6cbd66b835385
# differs from the initial hotfix
# Ref: https://github.com/kubernetes-client/python/pull/995/commits/9959273625b999ae9a8f0679c4def2ee7d699ede
git cherry-pick -n 88397bcc5b3b348a41dbf641367756b86552d362
if [ $? -eq 0 ]
then
    echo Successfully patched changes for custom client behavior
else
    echo Failed to patch changes for custom client behavior
    git restore --staged .
    exit 1
fi

# Patching commits for enabling from kubernetes import apis
# UPDATE: The commit being cherry-picked is updated to include both the commits as one
# Ref: https://github.com/kubernetes-client/python/blob/0976d59d6ff206f2f428cabc7a6b7b1144843b2a/kubernetes/client/apis/__init__.py
git cherry-pick -n 56ab983036bcb5c78eee91483c1e610da69216d1
if [ $? -eq 0 ]
then
    echo Successfully patched changes for enabling from kubernetes import apis
else
    echo Failed to patch changes for enabling from kubernetes import apis
    git restore --staged .
    exit 1
fi;

# Patching commits for Client Context Manager
# UPDATE: OpenAPI generator v4.3.0 has the context manager as a functionality. Cherry-picking just the tests for completeness.
# Ref: https://github.com/kubernetes-client/python/pull/1073
git cherry-pick -n 13dffb897617f87aaaee247095107d7011e002d5
if [ $? -eq 0 ]
then
    echo Successfully patched changes for Client Context Manager
else
    echo Failed to patch changes for Client Context Manager
    git restore --staged .
    exit 1
fi;

# Patching commit for no_proxy support
# UPDATE: The commit being cherry-picked is updated kubernetes/client/ unless OpenAPI generator v5.3.1 involved (offinical support of no_proxy feature).
# Ref: https://github.com/kubernetes-client/python/pull/1579/commits/95a893cd1c34de11a4e3893dd1dfde4a0ca30bdc and conversations in the PR.
git cherry-pick -n 95a893cd1c34de11a4e3893dd1dfde4a0ca30bdc
if [ $? -eq 0 ]
then
    echo Successfully patched changes for no_proxy support
else
    echo Failed to patch changes for no_proxy support
    git restore --staged .
    exit 1
fi;


git commit -m "Apply hotfixes"
