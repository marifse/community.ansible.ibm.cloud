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
module: ibm_container_ingress_alb_enable
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: Enable an existing ALB in a VPC cluster
requirements: []
description:
    - Enable an existing ALB in a VPC cluster.
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
                    - The cluster id on which the ALB is to be disabled
                required: True
                type: str
            enable:
                description:
                    - Set to true to enable the ALB, or false to disable the ALB for the cluster.
                required: False
                type: bool
            albBuild:
                description:
                    - The build number of the ALB.
                required: False
                type: str
            albID:
                description:
                    - The ID of the application load balancer (ALB).
                required: True
                type: str
            albType:
                description:
                    - The type of ALB.
                required: False
                type: str
            authBuild:
                description:
                    - The auth build of the ALB.
                required: False
                type: str
            createdDate:
                description:
                    - The date the ALB was created.
                required: False
                type: str
            disableDeployment:
                description:
                    - If set to true, the deployment of the ALB is disabled.
                required: False
                type: bool
            loadBalancerHostname:
                description:
                    - The hostname/dns name for ALB.
                required: False
                type: str
            name:
                description:
                    - The name of the cluster that the ALB belongs to.
                required: False
                type: str
            numOfInstances:
                description:
                    - Desired number of ALB replicas that you want in your cluster.
                required: False
                type: str
            resize:
                description:
                    - If set to true, resizing of the ALB is done.
                required: False
                type: bool
            state:
                description:
                    - The state of the ALB.
                required: False
                type: str
            status:
                description:
                    - The status of the ALB.
                required: False
                type: str
            zone:
                description:
                    - The zone where you want to add ALBs.
                required: False
                type: str
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_ingress_alb_enable:
    ibmcloud_api_key: "{{ ibmcloud_api_key }}"
    resource_group_id: "{{ resource_group_id }}"
    config:
        cluster: "Your Cluster ID"
        enable: True
        albBuild: "ALB Build"
        albID: "ALB ID"
        albType: "ALB Type"
        authBuild: "Auth Build"
        createdDate: "Created Date"
        disableDeployment: False
        loadBalancerHostname: "Load Balancer Host Name"
        name: "Name"
        numOfInstances: "Number of Instances"
        resize: False
        state: "State"
        status: "Status"
        zone: "Zone"
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
                enable=dict(required=False, type="bool"),
                albBuild=dict(required=False, type="str"),
                albID=dict(required=True, type="str"),
                albType=dict(required=False, type="str"),
                authBuild=dict(required=False, type="str"),
                createdDate=dict(required=False, type="str"),
                disableDeployment=dict(required=False, type="bool"),
                loadBalancerHostname=dict(required=False, type="str"),
                name=dict(required=False, type="str"),
                numOfInstances=dict(required=False, type="str"),
                resize=dict(required=False, type="bool"),
                state=dict(required=False, type="str"),
                status=dict(required=False, type="str"),
                zone=dict(required=False, type="str"),
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
    is_error, has_changed = sdk.enableAlb(module.params)

    if not is_error:
        module.exit_json(changed=has_changed)
    else:
        module.fail_json(msg="Error enabling ingress alb")


def main():
    run_module()


if __name__ == "__main__":
    main()
