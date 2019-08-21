# Release Process

The Kubernetes Python client is released on an as-needed basis. The process is as follows:

1. An issue is proposing a new release with a changelog since the last release
1. Update the support matrix in README.md removing the oldest version and adding the
   proposed release.
1. All [OWNERS](OWNERS) must LGTM this release
1. An OWNER runs `git tag -s $VERSION` and inserts the changelog and pushes
   the tag with `git push $VERSION`
1. The release issue is closed
1. An announcement email is sent to `kubernetes-dev@googlegroups.com`
   with the subject `[ANNOUNCE] kubernetes-python-client $VERSION is released`
