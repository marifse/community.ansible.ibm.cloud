import unittest
from unittest.mock import patch, MagicMock
from community_ibm_iks_ansible_collections.ibm.custom_iks_collection.plugins.modules.ibm_container_update_master import run_module

class TestIbmContainerUpdateMaster(unittest.TestCase):
    @patch("community_ibm_iks_ansible_collections.ibm.custom_iks_collection.plugins.modules.ibm_container_update_master.Authenticator")
    @patch("community_ibm_iks_ansible_collections.ibm.custom_iks_collection.plugins.modules.ibm_container_update_master.Beta")
    @patch("community_ibm_iks_ansible_collections.ibm.custom_iks_collection.plugins.modules.ibm_container_update_master.AnsibleModule")
    def test_run_module_successful(self, mock_ansible_module, mock_beta, mock_authenticator):
        # Mock the Authenticator instance and its return value
        mock_authenticator_instance = mock_authenticator.return_value
        mock_authenticator_instance.get_iam_token.return_value = "mocked_iam_token"

        # Create a MagicMock instance for the Beta class and its return value
        mock_beta_instance = mock_beta.return_value
        mock_beta_instance.updateMaster.return_value = (False, True)

        # Create a MagicMock instance for the AnsibleModule class
        mock_module_instance = mock_ansible_module.return_value

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "35tbgCTr910xpx6n_bv7edfjtKRHYIVej_e1l1DHnv-H",
            "resource_group_id": "0b8e94b052eb4513b73ef414d36cab5f",
            "config": {
                "cluster": "cji7k0bd06dr9smqeuvg",
                "force": True,
                "version": "1.0",
            },
        }

        # Set the module_instance.params value to the test arguments
        mock_module_instance.params = args

        # Simulate the run_module function call
        run_module()

        # Mocked objects assertions
        mock_beta.assert_called_once_with(cluster_id=args["config"]["cluster"])
        mock_authenticator.assert_called_once_with(api_key=args["ibmcloud_api_key"])
        mock_authenticator_instance.get_iam_token.assert_called_once()
        mock_beta_instance.updateMaster.assert_called_once_with(args)
        mock_module_instance.exit_json.assert_called_once_with(changed=True)
        mock_module_instance.fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
