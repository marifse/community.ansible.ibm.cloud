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
module: ibm_container_ingress_nlb_health_monitor_config
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: Create and optionally enable a health check monitor for an existing NLB subdomain in a cluster.
requirements: []
description:
    - Create and optionally enable a health check monitor for an existing NLB subdomain in a cluster.
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
            clusterID:
                description:
                    - The cluster id which needs to be monitored.
                required: True
                type: str
            idOrName:
                description:
                    - The name or ID of the cluster.
                required: True
                type: str
            allowInsecureSet:
                description:
                    - Allow insecure set
                required: False
                type: str
            createdOn:
                description:
                    - Created on
                required: False
                type: str
            healthcheckProperties:
                description:
                    - Health check properties
                required: False
                type: list
                elements: str
            desc:
                description:
                    - Desc
                required: True
                type: str
            followRedirectSet:
                description:
                    - Follow redirect set
                required: False
                type: str
            healtcheckPropertiesSetStatus:
                description:
                    - Health check properties
                required: False
                type: str
            modifiedOn:
                description:
                    - Modified on
                required: False
                type: str
            monitorState:
                description:
                    - Monitor State
                required: False
                type: str
            nlbHost:
                description:
                    - DNS name subdomain
                required: True
                type: str
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_ingress_nlb_health_monitor_config:
    ibmcloud_api_key: "{{ ibmcloud_api_key }}"
    resource_group_id: "{{ resource_group_id }}"
    config:
        clusterID: "Your Cluster ID"
        idOrName: "Your Cluster ID or Name"
        allowInsecureSet: "ALB List"
        createdOn: "NLB Host"
        healthcheckProperties: ["IP Address"]
        desc: "Monitor State"
        followRedirectSet: ""
        healtcheckPropertiesSetStatus: ""
        nlbHost: ""
        modifiedOn: ""
        monitorState: ""
"""

from ..module_utils.auth import Authenticator
from ..module_utils.sdk.container.ingressNlbHealthMonitor import IngressNlbHealthMonitor
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
                clusterID=dict(required=True, type="str"),
                idOrName=dict(required=True, type="str"),
                healthcheckProperties=dict(required=False, type="list", elements="str"),
                allowInsecureSet=dict(required=False, type="str"),
                nlbHost=dict(required=True, type="str"),
                createdOn=dict(required=False, type="str"),
                desc=dict(required=True, type="str"),
                followRedirectSet=dict(required=False, type="str"),
                healtcheckPropertiesSetStatus=dict(required=False, type="str"),
                modifiedOn=dict(required=False, type="str"),
                monitorState=dict(required=False, type="str"),
            ),
        ),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    cluster = module.params["config"]["clusterID"]
    ibmcloud_api_key = module.params["ibmcloud_api_key"]

    sdk = IngressNlbHealthMonitor(
        cluster_id=cluster,
    )

    authenticator = Authenticator(
        api_key=ibmcloud_api_key,
    )

    module.params["iam_token"] = authenticator.get_iam_token()

    # List baisc info a cluster.
    is_error, has_changed, alb_config = sdk.configureHealthCheckMonitorALB(
        module.params
    )

    if not is_error:
        module.exit_json(changed=has_changed, new_config=alb_config)
    else:
        module.fail_json(msg="Error NLB Health Monitor Config", meta=alb_config)


def main():
    run_module()


if __name__ == "__main__":
    main()
