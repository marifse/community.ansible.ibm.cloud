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
module: ibm_container_ingress_alb_update
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: Update ALBs in a cluster
requirements: []
description:
    - Update ALBs in a cluster
options:
    ibmcloud_api_key:
        required: True
        type: str
        description:
            - The IBM Cloud API Key.

    resource_group_id:
        required: True
        type: str
        description:
            - The ResourceGroup ID

    config:
        description:
            - Configuration
        required: True
        type: dict
        suboptions:
            cluster:
                description:
                    - The cluster id where the ALB's are to be updated
                required: True
                type: str
            albBuild:
                description:
                    - The ALB build IDs
                required: True
                type: str
            albList:
                description:
                    - The list of the ALB's which are required to be updated
                required: True
                type: list
                elements: str
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_ingress_alb_update:
    ibmcloud_api_key: "{{ ibmcloud_api_key }}"
    resource_group_id: "{{ resource_group_id }}"
    config:
        cluster: "Your Cluster ID"
        albBuild: "ALB Build ID"
        albList: "ALB List"
"""

from ..module_utils.auth import Authenticator
from ..module_utils.sdk.container.ingressAlbBeta import IngressALBBeta
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
        resource_group_id=dict(required=True, type="str"),
        config=dict(
            required=True,
            type="dict",
            options=dict(
                cluster=dict(required=True, type="str"),
                albBuild=dict(required=True, type="str"),
                albList=dict(required=True, type="list", elements="str"),
            ),
        ),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    cluster = module.params["config"]["cluster"]
    ibmcloud_api_key = module.params["ibmcloud_api_key"]

    sdk = IngressALBBeta(
        cluster_id=cluster,
    )

    authenticator = Authenticator(
        api_key=ibmcloud_api_key,
    )

    module.params["iam_token"] = authenticator.get_iam_token()

    # List baisc info a cluster.
    is_error, has_changed = sdk.updateAlb(module.params)

    if not is_error:
        module.exit_json(changed=has_changed)
    else:
        module.fail_json(msg="Error updating ingress alb")


def main():
    run_module()


if __name__ == "__main__":
    main()
