import unittest
from unittest.mock import patch, MagicMock
from plugins.module_utils.basic import AnsibleModule
from plugins.module_utils.sdk.container.monitoring import Monitoring
from plugins.modules.ibm_container_monitoring_config_modify import run_module

class TestIbmContainerMonitoringConfigModify(unittest.TestCase):
    @patch("plugins.module_utils.auth.Authenticator.get_iam_token")
    @patch("plugins.module_utils.auth.Authenticator.get_refresh_token")
    @patch.object(Monitoring, "modify_config_monitoring")
    @patch.object(AnsibleModule, "exit_json")
    @patch.object(AnsibleModule, "fail_json")
    def test_run_module_successful(self, mock_fail_json, mock_exit_json, mock_modify_config, mock_get_refresh_token, mock_get_iam_token):
        mock_get_iam_token.return_value = "mocked_iam_token"
        mock_get_refresh_token.return_value = "mocked_refresh_token"
        mock_modify_config.return_value = (False, True, "mocked_monitoring_info")

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "mocked_api_key",
            "config": {
                "cluster": "mocked_clusterID",
                "ingestionKey": "mocked_ingestion_key",
                "privateEndpoint": True,
                "instance": "mocked_instance",
                "newInstance": "mocked_new_instance",
            },
        }

        module = MagicMock(spec=AnsibleModule)
        module.params = args
        AnsibleModule.return_value = module

        run_module()

        mock_get_iam_token.assert_called_once()
        mock_get_refresh_token.assert_called_once()
        mock_modify_config.assert_called_once_with(module.params)
        mock_exit_json.assert_called_once_with(changed=True, monitoring_info="mocked_monitoring_info")
        mock_fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
