import unittest
from unittest.mock import patch, MagicMock
from plugins.module_utils.basic import AnsibleModule
from plugins.module_utils.sdk.container.ingress import Ingress
from plugins.modules.ibm_container_ingress_nlb_regenerate_secret import run_module

class TestIbmContainerIngressNlbRegenerateSecret(unittest.TestCase):
    @patch("plugins.module_utils.auth.Authenticator.get_iam_token")
    @patch.object(Ingress, "regenerateCert")
    @patch.object(AnsibleModule, "exit_json")
    @patch.object(AnsibleModule, "fail_json")
    def test_run_module_successful(self, mock_fail_json, mock_exit_json, mock_regenerate, mock_get_iam_token):
        mock_get_iam_token.return_value = "mocked_iam_token"
        mock_regenerate.return_value = (False, True)

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "mocked_api_key",
            "config": {
                "cluster": "mocked_clusterID",
                "subdomain": "mocked_subdomain",
            },
        }

        module = MagicMock(spec=AnsibleModule)
        module.params = args
        AnsibleModule.return_value = module

        run_module()

        mock_get_iam_token.assert_called_once()
        mock_regenerate.assert_called_once_with(args["config"])
        mock_exit_json.assert_called_once_with(changed=True)
        mock_fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
