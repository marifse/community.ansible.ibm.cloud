import os
import unittest
from unittest.mock import patch
from ansible_collections.your_collection.your_module import ibm_container_image_security_disable


class TestIBMContainerImageSecurityDisable(unittest.TestCase):
    @patch("ansible_collections.your_collection.your_module.ibm_container_image_security_disable.Authenticator")
    @patch("ansible_collections.your_collection.your_module.ibm_container_image_security_disable.ImageSecret")
    @patch("ansible_collections.your_collection.your_module.ibm_container_image_security_disable.AnsibleModule")
    def test_run_module_success(self, mock_module, mock_image_secret, mock_authenticator):
        # Mock the module parameters
        module_params = {
            "ibmcloud_api_key": "your_api_key",
            "resource_group_id": "your_resource_group_id",
            "config": {
                "cluster": "your_cluster_id"
            }
        }
        mock_module.return_value.params = module_params

        # Create instance of Authenticator and mock its get_iam_token method
        mock_auth_instance = mock_authenticator.return_value
        mock_auth_instance.get_iam_token.return_value = "your_iam_token"

        # Create instance of ImageSecret and mock its disableImageSecurity method
        mock_image_secret_instance = mock_image_secret.return_value
        mock_image_secret_instance.disableImageSecurity.return_value = (False, True)

        # Run the module
        ibm_container_image_security_disable.run_module()

        # Assertions
        mock_authenticator.assert_called_once_with(api_key="your_api_key")
        mock_auth_instance.get_iam_token.assert_called_once()
        mock_image_secret.assert_called_once_with(cluster_id="your_cluster_id")
        mock_image_secret_instance.disableImageSecurity.assert_called_once_with(module_params)

        # Additional assertions based on your requirements

    # Add more test methods for other scenarios


if __name__ == "__main__":
    unittest.main()
