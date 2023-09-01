#!/usr/bin/python
# -*- coding: utf-8 -*-

# (C) Copyright IBM Corp. 2022.
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: ibm_container_ingress_nlb_delete_secret
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: Remove a secret from an NLB subdomain
requirements: []
description:
    - Delete a secret from an NLB subdomain in your cluster and prevent future renewal of the certificate.
options:
    ibmcloud_api_key:
        required: True
        type: str
        description:
            - The IBM Cloud API Key.

    config:
        description:
            - Configuration
        required: True
        type: dict
        suboptions:
            cluster:
                description:
                    - The cluster id where the NLB secret is to be deleted
                required: True
                type: str

            subdomain:
                description:
                    -   The Ingestion Key which needs to used for connecting to Sysdig Service Instance
                required: False
                type : str
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_ingress_nlb_delete_secret:
    ibmcloud_api_key: "{{ name }}"
    config:
        cluster: "Your Cluster ID"
        subdomain : "Your Subdomain"
"""

from ..module_utils.auth import Authenticator
from ..module_utils.sdk.container.ingress import Ingress
from ansible.module_utils.basic import env_fallback
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        ibmcloud_api_key=dict(
            required=True,
            type="str",
            no_log=True,
            fallback=(env_fallback, ["IC_API_KEY"]),
        ),
        config=dict(
            required=True,
            type="dict",
            options=dict(
                cluster=dict(required=True, type="str"),
                subdomain=dict(required=False, type="str"),
            ),
        ),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    cluster = module.params["config"]["cluster"]
    ibmcloud_api_key = module.params["ibmcloud_api_key"]

    sdk = Ingress(
        cluster_id=cluster,
    )

    authenticator = Authenticator(
        api_key=ibmcloud_api_key,
    )

    module.params["iam_token"] = authenticator.get_iam_token()

    # List baisc info a cluster.
    is_error, has_changed = sdk.deleteSecret(module.params)

    if not is_error:
        module.exit_json(
            changed=has_changed,
        )
    else:
        module.fail_json(msg="Error deleting ingress nlb secret")


def main():
    run_module()


if __name__ == "__main__":
    main()
