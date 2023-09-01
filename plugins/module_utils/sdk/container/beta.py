# coding: utf-8

# Copyright 2022 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function

__metaclass__ = type
import traceback

try:
    import requests
except ImportError:
    HAS_ANOTHER_LIBRARY = False
    ANOTHER_LIBRARY_IMPORT_ERROR = traceback.format_exc()
else:
    HAS_ANOTHER_LIBRARY = True


class Beta:
    """Beta class to support following functionalities.
    * disable_private_service_endpoint
    * disable_public_service_endpoint
    * enable_private_service_endpoint
    * enable_public_service_endpoint
    * enable_pull_secret
    * replace_worker
    * update_master
    """

    # Class Variable
    DEFAULT_SERVICE_URL = "https://containers.cloud.ibm.com/global/"

    # The init method or constructor
    def __init__(self, cluster_id):

        # Instance Variable
        self.cluster_id = cluster_id

    # Method to fetch error code based on status code
    def get_status(self, status_code):
        if status_code == 200 or status_code == 204:
            status = "OK. Request successfully processed"
        elif status_code == 401:
            status = "Unauthorized. The IAM token is invalid or expired."
        elif status_code == 404:
            status = "Not found. The specified cluster could not be found."
        elif status_code == 500:
            status = "Internal Server Error. IBM Cloud Kubernetes Service is currently unavailable."
        else:
            status = "ERROR. status_code mismatch"
        return status

    # Method to disable private service endpoint
    def disablePrivateServiceEndpoint(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/disablePrivateServiceEndpoint"
        response = requests.post(
            Beta.DEFAULT_SERVICE_URL + TARGET_URL, headers=headers, json=data["config"]
        )

        if response.status_code == 200 or response.status_code == 204:
            return True, False
        elif response.status_code == 401:
            return True, False
        elif response.status_code == 404:
            return True, False
        elif response.status_code == 500:
            return True, False
        else:
            return True, False

    # Method to disable public service endpoint
    def disablePublicServiceEndpoint(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/disablePublicServiceEndpoint"
        response = requests.post(
            Beta.DEFAULT_SERVICE_URL + TARGET_URL, headers=headers, json=data["config"]
        )

        if response.status_code == 200 or response.status_code == 204:
            return False, True
        elif response.status_code == 401:
            return True, False
        elif response.status_code == 404:
            return True, False
        elif response.status_code == 500:
            return True, False
        else:
            return True, False

    # Method to enable private service endpoint
    def enablePrivateServiceEndpoint(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/enablePrivateServiceEndpoint"
        response = requests.post(
            Beta.DEFAULT_SERVICE_URL + TARGET_URL, headers=headers, json=data["config"]
        )

        if response.status_code == 200 or response.status_code == 204:
            return False, True
        elif response.status_code == 401:
            return True, False
        elif response.status_code == 404:
            return True, False
        elif response.status_code == 500:
            return True, False
        else:
            return True, False

    # Method to enable public service endpoint
    def enablePublicServiceEndpoint(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/enablePublicServiceEndpoint"
        response = requests.post(
            Beta.DEFAULT_SERVICE_URL + TARGET_URL, headers=headers, json=data["config"]
        )

        if response.status_code == 200 or response.status_code == 204:
            return False, True
        elif response.status_code == 401:
            return True, False
        elif response.status_code == 404:
            return True, False
        elif response.status_code == 500:
            return True, False
        else:
            return True, False

    # Method to enable pullsecret
    def enablePullSecret(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/enablePullSecret"
        response = requests.post(
            Beta.DEFAULT_SERVICE_URL + TARGET_URL, headers=headers, json=data["config"]
        )

        if response.status_code == 200 or response.status_code == 204:
            return False, True
        elif response.status_code == 401:
            return True, False
        elif response.status_code == 404:
            return True, False
        elif response.status_code == 500:
            return True, False
        else:
            return True, False

    # Method to replace worker node in cluster
    def replaceWorker(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/vpc/replaceWorker"
        response = requests.post(
            Beta.DEFAULT_SERVICE_URL + TARGET_URL, headers=headers, json=data["config"]
        )

        if response.status_code == 200 or response.status_code == 204:
            return False, True
        elif response.status_code == 401:
            return True, False
        elif response.status_code == 404:
            return True, False
        elif response.status_code == 500:
            return True, False
        else:
            return True, False

    # Method to update master kube api version
    def updateMaster(self, data):
        headers = {
            "Authorization": data["iam_token"],
            "X-Auth-Resource-Group": data["resource_group_id"],
        }
        TARGET_URL = "/v2/updateMaster"
        response = requests.post(
            Beta.DEFAULT_SERVICE_URL + TARGET_URL, headers=headers, json=data["config"]
        )

        if response.status_code == 200 or response.status_code == 204:
            return False, True
        elif response.status_code == 401:
            return True, False
        elif response.status_code == 404:
            return True, False
        elif response.status_code == 500:
            return True, False
        else:
            return True, False
