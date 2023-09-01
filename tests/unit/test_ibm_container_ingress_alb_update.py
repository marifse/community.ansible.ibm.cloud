import unittest
from unittest.mock import MagicMock
from ansible.module_utils.basic import AnsibleModule
from ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_update import run_module

class TestIBMContainerIngressALBUpdateModule(unittest.TestCase):

    def setUp(self):
        self.module_args = {
            "ibmcloud_api_key": "your_api_key",
            "resource_group_id": "your_resource_group",
            "config": {
                "cluster": "your_cluster_id",
                "albBuild": "your_alb_build",
                "albList": ["alb_id_1", "alb_id_2"]
            }
        }

    def test_successful_update_alb(self):
        mock_ingress_alb_beta = MagicMock()
        mock_ingress_alb_beta.updateAlb.return_value = (False, True)

        with unittest.mock.patch(
            "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_update.IngressALBBeta",
            return_value=mock_ingress_alb_beta
        ):
            with unittest.mock.patch(
                "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_update.Authenticator.get_iam_token",
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

    def test_error_updating_alb(self):
        mock_ingress_alb_beta = MagicMock()
        mock_ingress_alb_beta.updateAlb.return_value = (True, False)

        with unittest.mock.patch(
            "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_update.IngressALBBeta",
            return_value=mock_ingress_alb_beta
        ):
            with unittest.mock.patch(
                "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_update.Authenticator.get_iam_token",
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
                        msg="Error updating ingress alb"
                    )

if __name__ == "__main__":
    unittest.main()
