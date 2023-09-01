import unittest
from unittest.mock import patch, MagicMock
from plugins.module_utils.basic import AnsibleModule
from plugins.module_utils.sdk.container.ingressNlbHealthMonitor import IngressNlbHealthMonitor
from plugins.modules.ibm_container_ingress_nlb_health_monitor_list import run_module

class TestIbmContainerIngressNlbHealthMonitorList(unittest.TestCase):
    @patch("plugins.module_utils.auth.Authenticator.get_iam_token")
    @patch.object(IngressNlbHealthMonitor, "listHealthCheckMonitorALB")
    @patch.object(AnsibleModule, "exit_json")
    @patch.object(AnsibleModule, "fail_json")
    def test_run_module_successful(self, mock_fail_json, mock_exit_json, mock_list, mock_get_iam_token):
        mock_get_iam_token.return_value = "mocked_iam_token"
        mock_list.return_value = (False, True, "mocked_alb_config")

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "mocked_api_key",
            "resource_group_id": "mocked_resource_group_id",
            "config": {
                "idOrName": "mocked_idOrName",
            },
        }

        module = MagicMock(spec=AnsibleModule)
        module.params = args
        AnsibleModule.return_value = module

        run_module()

        mock_get_iam_token.assert_called_once()
        mock_list.assert_called_once_with(args["config"])
        mock_exit_json.assert_called_once_with(changed=True, new_config="mocked_alb_config")
        mock_fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
