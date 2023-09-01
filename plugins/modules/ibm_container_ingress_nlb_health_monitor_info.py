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
module: ibm_container_ingress_nlb_health_monitor_info
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: Enable or disable a health check monitor for an NLB subdomain
requirements: []
description:
    - Enable or disable a health check monitor for an NLB subdomain.
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
            nlbDnsType:
                description:
                    - The NLB DNS type.
                required: True
                type: str
            nlbHost:
                description:
                    - The NLB subdomain that you want health check monitor settings for.
                required: True
                type: str
            nlbIPArray:
                description:
                    - The NLB IP Array
                required: True
                type: list
                elements: str
            nlbMonitorState:
                description:
                    - The NLB Monitor state.
                required: True
                type: str
            nlbSslSecretName:
                description:
                    - The NLB SSL Secret Name
                required: True
                type: str
            nlbStatusMessage:
                description:
                    - The NLB status Message
                required: True
                type: str
            nlbType:
                description:
                    - The NLB type
                required: True
                type: str
            secretNamespace:
                description:
                    - The NLB secret Namespace
                required: True
                type: str
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_ingress_nlb_health_monitor_info:
    ibmcloud_api_key: "{{ ibmcloud_api_key }}"
    resource_group_id: "{{ resource_group_id }}"
    config:
        clusterID: "Your Cluster ID"
        idOrName: "Your Cluster ID or Name"
        nlbDnsType: "ALB List"
        nlbHost: "NLB Host"
        nlbIPArray: "IP Address"
        nlbMonitorState: "Monitor State"
        nlbSslSecretName: ""
        nlbStatusMessage: ""
        nlbType: ""
        secretNamespace: ""
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
                nlbIPArray=dict(required=True, type="list", elements="str"),
                nlbDnsType=dict(required=True, type="str"),
                nlbHost=dict(required=True, type="str"),
                nlbMonitorState=dict(required=True, type="str"),
                nlbSslSecretName=dict(required=True, type="str", no_log=True),
                nlbStatusMessage=dict(required=True, type="str"),
                nlbType=dict(required=True, type="str"),
                secretNamespace=dict(required=True, type="str", no_log=True),
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
    is_error, has_changed, info_nlb = sdk.enableDisableHealthCheckMonitorALB(
        module.params
    )

    if not is_error:
        module.exit_json(changed=has_changed)
    else:
        module.fail_json(msg="Error NLB Healt Monitor Info", meta=info_nlb)


def main():
    run_module()


if __name__ == "__main__":
    main()
