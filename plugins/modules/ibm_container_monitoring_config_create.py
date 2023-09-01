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
module: ibm_container_monitoring_config_create
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: Create Config for SysDig Monitoring
requirements: []
description:
    - Create a monitoring configuration for your IBM Cloud Kubernetes Service .
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
                    - The cluster id which needs to be monitored.
                required: True
                type: str

            ingestionKey:
                description:
                    -   The Ingestion Key which needs to used for connecting to Sysdig Service Instance
                required: False
                type : str

            instance:
                description:
                    -   The Service Instance Name/ID of the Sysdig Monitoring - IBM Cloud Monitoring
                required: True
                type : str

            privateEndpoint:
                description:
                    -   The privateEndpoint of the Sysdig Monitoring - IBM Cloud Monitoring
                required: False
                type : bool
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_monitoring_config_create:
    ibmcloud_api_key: "{{ name }}"
    config:
        cluster: "Your Cluster ID"
        ingestionKey : "Your Volume Attachment ID"
        instance: "Your Volume ID"
        privateEndpoint: "Your Worker ID"
"""

from ..module_utils.auth import Authenticator
from ..module_utils.sdk.container.monitoring import Monitoring
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
                ingestionKey=dict(required=False, no_log=True, type="str"),
                privateEndpoint=dict(required=False, type="bool"),
                instance=dict(required=True, type="str"),
            ),
        ),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    cluster = module.params["config"]["cluster"]
    ibmcloud_api_key = module.params["ibmcloud_api_key"]

    sdk = Monitoring(
        cluster_id=cluster,
    )

    authenticator = Authenticator(
        api_key=ibmcloud_api_key,
    )

    module.params["iam_token"] = authenticator.get_iam_token()
    module.params["refresh_token"] = authenticator.get_refresh_token()

    # List baisc info a cluster.
    is_error, has_changed, monitoring_info = sdk.create_config_monitoring(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, monitoring_info=monitoring_info)
    else:
        module.fail_json(msg="Error creating monitoring config", meta=monitoring_info)


def main():
    run_module()


if __name__ == "__main__":
    main()
