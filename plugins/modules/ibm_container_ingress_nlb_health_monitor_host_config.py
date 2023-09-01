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
module: ibm_container_ingress_nlb_health_monitor_host_config
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: View the health check monitor settings for an NLB subdomain.
requirements: []
description:
    - View the health check monitor settings for an NLB subdomain.
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
            idOrName:
                description:
                    - The name or ID of the cluster.
                required: True
                type: str
            nlbHost:
                description:
                    - The NLB subdomain that you want health check monitor settings for.
                required: True
                type: str
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_ingress_nlb_health_monitor_host_config:
    ibmcloud_api_key: "{{ ibmcloud_api_key }}"
    resource_group_id: "{{ resource_group_id }}"
    config:
        idOrName: "Your Cluster ID or Name"
        nlbHost: "The NLB subdomain that you want health check monitor settings for."
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
                idOrName=dict(required=True, type="str"),
                nlbHost=dict(required=True, type="str"),
            ),
        ),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    cluster = module.params["config"]["idOrName"]
    ibmcloud_api_key = module.params["ibmcloud_api_key"]

    sdk = IngressNlbHealthMonitor(
        cluster_id=cluster,
    )

    authenticator = Authenticator(
        api_key=ibmcloud_api_key,
    )

    module.params["iam_token"] = authenticator.get_iam_token()

    # List baisc info a cluster.
    is_error, has_changed, alb_config = sdk.viewHealthCheckMonitorALB(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, new_config=alb_config)
    else:
        module.fail_json(msg="Error NLB Health Monitor Host Config", meta=alb_config)


def main():
    run_module()


if __name__ == "__main__":
    main()
