import unittest
from unittest.mock import MagicMock
from ansible.module_utils.basic import AnsibleModule
from your_module_file import run_module

class TestIBMContainerImageSecurityEnableModule(unittest.TestCase):

    def setUp(self):
        self.module_args = {
            "ibmcloud_api_key": "your_api_key",
            "resource_group_id": "your_resource_group",
            "config": {
                "cluster": "your_cluster_id"
            }
        }

    def test_successful_enable_image_security(self):
        mock_image_secret = MagicMock()
        mock_image_secret.enableImageSecurity.return_value = (False, True)

        with unittest.mock.patch(
            "your_module_file.ImageSecret",
            return_value=mock_image_secret
        ):
            with unittest.mock.patch(
                "your_module_file.Authenticator.get_iam_token",
                return_value="your_iam_token"
            ):
                with unittest.mock.patch(
                    "your_module_file.AnsibleModule",
                    side_effect=lambda *args, **kwargs: AnsibleModule(argument_spec=self.module_args)
                ) as mock_module:
                    run_module()
                    mock_module.assert_called_with(
                        argument_spec=self.module_args, supports_check_mode=True
                    )
                    mock_module.return_value.exit_json.assert_called_with(changed=True)

    def test_error_enabling_image_security(self):
        mock_image_secret = MagicMock()
        mock_image_secret.enableImageSecurity.return_value = (True, False)

        with unittest.mock.patch(
            "your_module_file.ImageSecret",
            return_value=mock_image_secret
        ):
            with unittest.mock.patch(
                "your_module_file.Authenticator.get_iam_token",
                return_value="your_iam_token"
            ):
                with unittest.mock.patch(
                    "your_module_file.AnsibleModule",
                    side_effect=lambda *args, **kwargs: AnsibleModule(argument_spec=self.module_args)
                ) as mock_module:
                    run_module()
                    mock_module.assert_called_with(
                        argument_spec=self.module_args, supports_check_mode=True
                    )
                    mock_module.return_value.fail_json.assert_called_with(msg="Error enabling image security")

if __name__ == "__main__":
    unittest.main()
