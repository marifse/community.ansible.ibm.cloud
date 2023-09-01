import unittest
from unittest.mock import patch, MagicMock
from plugins.module_utils.basic import AnsibleModule
from plugins.module_utils.sdk.container.ingressNlbHealthMonitor import IngressNlbHealthMonitor
from plugins.modules.ibm_container_ingress_nlb_health_monitor_info import run_module

class TestIbmContainerIngressNlbHealthMonitorInfo(unittest.TestCase):
    @patch("plugins.modules.ibm_container_ingress_nlb_health_monitor_info.Authenticator.get_iam_token")
    @patch.object(IngressNlbHealthMonitor, "enableDisableHealthCheckMonitorALB")
    @patch.object(AnsibleModule, "exit_json")
    @patch.object(AnsibleModule, "fail_json")
    def test_run_module_successful(self, mock_fail_json, mock_exit_json, mock_enable_disable, mock_get_iam_token):
        mock_get_iam_token.return_value = "mocked_iam_token"
        mock_enable_disable.return_value = (False, True, "mocked_info_nlb")

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "mocked_api_key",
            "resource_group_id": "mocked_resource_group_id",
            "config": {
                "clusterID": "mocked_clusterID",
                "idOrName": "mocked_idOrName",
                "nlbIPArray": ["mocked_ip"],
                "nlbDnsType": "mocked_dns_type",
                "nlbHost": "mocked_nlbHost",
                "nlbMonitorState": "mocked_nlbMonitorState",
                "nlbSslSecretName": "mocked_ssl_secret",
                "nlbStatusMessage": "mocked_status_message",
                "nlbType": "mocked_nlb_type",
                "secretNamespace": "mocked_secret_namespace",
            },
        }

        module = MagicMock(spec=AnsibleModule)
        module.params = args
        AnsibleModule.return_value = module

        run_module()

        mock_get_iam_token.assert_called_once()
        mock_enable_disable.assert_called_once_with(args["config"])
        mock_exit_json.assert_called_once_with(changed=True)
        mock_fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
