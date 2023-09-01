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
module: ibm_container_ingress_alb_create
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: Create a public or private ALB in a specified zone and VPC cluster.
requirements: []
description:
    - Create a public or private ALB in a specified zone and VPC cluster.
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
                    - The cluster id where the ALB is to be created.
                required: True
                type: str
            enableByDefault:
                description:
                    - If set to true, the ALB is enabled by default.
                required: True
                type: bool
            ingressImage:
                description:
                    - The type of Ingress image that you want to use for your ALB deployment.
                required: True
                type: str
            type:
                description:
                    - The type of ALB that you want to create.
                required: True
                type: str
            zone:
                description:
                    - The zone where you want to deploy the ALB.
                required: True
                type: str
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_ingress_alb_create:
    ibmcloud_api_key: "{{ ibmcloud_api_key }}"
    resource_group_id: "{{ resource_group_id }}"
    config:
        cluster: "Your Cluster ID"
        enableByDefault: True
        ingressImage: "Ingress Image"
        type: "ALB Type"
        zone: "ALB Zone"
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
                enableByDefault=dict(required=True, type="bool"),
                ingressImage=dict(required=True, type="str"),
                type=dict(required=True, type="str"),
                zone=dict(required=True, type="str"),
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
    is_error, has_changed, alb_info = sdk.createAlb(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, alb_info=alb_info)
    else:
        module.fail_json(msg="Error creating ingress ALB", meta=alb_info)


def main():
    run_module()


if __name__ == "__main__":
    main()
