# Publishing a release

Releases use PyPI Trusted Publishing and do not store an API token in GitHub.

## One-time PyPI setup

Create a pending trusted publisher at <https://pypi.org/manage/account/publishing/>
with these exact values:

| Field | Value |
| --- | --- |
| PyPI project name | `proxyrequest-sdk` |
| GitHub owner | `proxyrequest` |
| GitHub repository | `python-sdk` |
| Workflow filename | `release.yml` |
| Environment name | `pypi` |

The GitHub repository must also contain an environment named `pypi`. The
release workflow uses GitHub OIDC to create the project on its first publish.

## Release procedure

1. Confirm that the package name remains available on PyPI.
2. Update the version in `pyproject.toml` and add the matching changelog entry.
3. Run `make quality generate-check build` and install the built wheel in a
   clean virtual environment.
4. Push the release commit to `main` and wait for CI.
5. Create a `vX.Y.Z` GitHub release from that commit.
6. Verify the `Publish to PyPI` workflow and the package page on PyPI.

The workflow refuses a tag that does not exactly match the project version.
