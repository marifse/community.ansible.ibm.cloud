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
module: ibm_container_storage_attachment_create
author: arifnafees (@marifse)
version_added: "1.0.0"
short_description: create IKS Cluster Storage Attachment
requirements: []
description:
    - Create the IKS Container Storage Attachment
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
            - ID of the resource group that the cluster is in. To check the resource group ID of the cluster, use the GET /v1/clusters/idOrName API.

    vpcVolumeAttachmentConfig:
        description:
            - command for the worker update
        required: True
        type: dict
        suboptions:
            cluster:
                description:
                    - The cluster where we have to attach the storage.
                required: True
                type: str

            volumeAttachmentID:
                description:
                    -   The Volume Attachment ID
                required: True
                type : str

            volumeID:
                description:
                    -   The Volume ID which needs to be attached
                required: True
                type : str

            worker:
                description:
                    -   The Worker ID of the Given Cluster
                required: True
                type : str
"""


EXAMPLES = r"""
# Target the cluster which is present in default resource group
- ibm_container_storage_attachment_create:
    resource_group_id: "{{ name }}"
    vpcVolumeAttachmentConfig:
        cluster: "Your Cluster ID"
        volumeAttachmentID : "Your Volume Attachment ID"
        volumeID: "Your Volume ID"
        worker: "Your Worker ID"
"""

from ..module_utils.auth import Authenticator
from ..module_utils.sdk.container.storage import Storage
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
        vpcVolumeAttachmentConfig=dict(
            required=True,
            type="dict",
            options=dict(
                cluster=dict(required=True, type="str"),
                volumeAttachmentID=dict(required=True, type="str"),
                volumeID=dict(required=True, type="str"),
                worker=dict(required=True, type="str"),
            ),
        ),
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    cluster = module.params["vpcVolumeAttachmentConfig"]["cluster"]
    worker = module.params["vpcVolumeAttachmentConfig"]["worker"]
    resource_group_id = module.params["resource_group_id"]
    ibmcloud_api_key = module.params["ibmcloud_api_key"]

    sdk = Storage(
        cluster_id=cluster,
    )

    authenticator = Authenticator(
        api_key=ibmcloud_api_key,
    )

    module.params["iam_token"] = authenticator.get_iam_token()

    # List baisc info a cluster.
    is_error, has_changed, storage_info = sdk.create_storage_attachment(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, storage_info=storage_info)
    else:
        module.fail_json(msg="Error creating storage attachment", meta=storage_info)


def main():
    run_module()


if __name__ == "__main__":
    main()
