import unittest
from unittest.mock import patch, MagicMock
from plugins.module_utils.auth import Authenticator
from plugins.module_utils.sdk.container.monitoring import Monitoring
from plugins.modules.ibm_container_monitoring_config_remove import run_module

class TestIbmContainerMonitoringConfigRemove(unittest.TestCase):
    @patch("plugins.module_utils.auth.Authenticator.get_iam_token")
    @patch.object(Monitoring, "remove_config_monitoring")
    @patch.object(Authenticator, "get_refresh_token")
    def test_run_module_successful(self, mock_get_refresh_token, mock_remove_config_monitoring, mock_get_iam_token):
        mock_get_iam_token.return_value = "mocked_iam_token"
        mock_get_refresh_token.return_value = "mocked_refresh_token"
        mock_remove_config_monitoring.return_value = (False, True, "mocked_monitoring_info")

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "mocked_api_key",
            "config": {
                "cluster": "mocked_cluster",
                "instance": "mocked_instance",
            },
        }

        module = MagicMock()
        module.params = args
        run_module()

        mock_get_iam_token.assert_called_once()
        mock_get_refresh_token.assert_called_once()
        mock_remove_config_monitoring.assert_called_once_with(args["config"])
        module.exit_json.assert_called_once_with(changed=True, monitoring_info="mocked_monitoring_info")
        module.fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
