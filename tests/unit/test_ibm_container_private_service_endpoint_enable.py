import unittest
from unittest.mock import patch, MagicMock
from plugins.module_utils.auth import Authenticator
from plugins.module_utils.sdk.container.beta import Beta
from plugins.modules.ibm_container_private_service_endpoint_enable import run_module

class TestIbmContainerPrivateServiceEndpointEnable(unittest.TestCase):
    @patch("plugins.module_utils.auth.Authenticator.get_iam_token")
    @patch.object(Beta, "enablePrivateServiceEndpoint")
    def test_run_module_successful(self, mock_enable_private_service_endpoint, mock_get_iam_token):
        mock_get_iam_token.return_value = "mocked_iam_token"
        mock_enable_private_service_endpoint.return_value = (False, True)

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "mocked_api_key",
            "resource_group_id": "mocked_resource_group_id",
            "config": {
                "cluster": "mocked_cluster",
            },
        }

        module = MagicMock()
        module.params = args
        run_module()

        mock_get_iam_token.assert_called_once()
        mock_enable_private_service_endpoint.assert_called_once_with(args["config"])
        module.exit_json.assert_called_once_with(changed=True)
        module.fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
