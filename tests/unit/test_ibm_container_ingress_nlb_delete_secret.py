import unittest
from unittest.mock import MagicMock
from ansible.module_utils.basic import AnsibleModule
from ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_nlb_delete_secret import run_module

class TestIBMContainerIngressNLBDeleteSecretModule(unittest.TestCase):

    def setUp(self):
        self.module_args = {
            "ibmcloud_api_key": "your_api_key",
            "config": {
                "cluster": "your_cluster_id",
                "subdomain": "your_subdomain"
            }
        }

    def test_successful_delete_secret(self):
        mock_ingress = MagicMock()
        mock_ingress.deleteSecret.return_value = (False, True)

        with unittest.mock.patch(
            "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_nlb_delete_secret.Ingress",
            return_value=mock_ingress
        ):
            with unittest.mock.patch(
                "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_nlb_delete_secret.Authenticator.get_iam_token",
                return_value="your_iam_token"
            ):
                with unittest.mock.patch(
                    "ansible.module_utils.basic.AnsibleModule",
                    side_effect=lambda *args, **kwargs: AnsibleModule(argument_spec=self.module_args)
                ) as mock_module:
                    run_module()
                    mock_module.assert_called_with(
                        argument_spec=self.module_args, supports_check_mode=True
                    )
                    mock_module.return_value.exit_json.assert_called_with(
                        changed=True
                    )

    def test_error_deleting_secret(self):
        mock_ingress = MagicMock()
        mock_ingress.deleteSecret.return_value = (True, False)

        with unittest.mock.patch(
            "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_nlb_delete_secret.Ingress",
            return_value=mock_ingress
        ):
            with unittest.mock.patch(
                "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_nlb_delete_secret.Authenticator.get_iam_token",
                return_value="your_iam_token"
            ):
                with unittest.mock.patch(
                    "ansible.module_utils.basic.AnsibleModule",
                    side_effect=lambda *args, **kwargs: AnsibleModule(argument_spec=self.module_args)
                ) as mock_module:
                    run_module()
                    mock_module.assert_called_with(
                        argument_spec=self.module_args, supports_check_mode=True
                    )
                    mock_module.return_value.fail_json.assert_called_with(
                        msg="Error deleting ingress nlb secret"
                    )

if __name__ == "__main__":
    unittest.main()
