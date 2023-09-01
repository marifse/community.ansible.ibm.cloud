import unittest
from unittest.mock import MagicMock
from ansible.module_utils.basic import AnsibleModule
from ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_disable import run_module

class TestIBMContainerIngressALBDisableModule(unittest.TestCase):

    def setUp(self):
        self.module_args = {
            "ibmcloud_api_key": "your_api_key",
            "resource_group_id": "your_resource_group",
            "config": {
                "cluster": "your_cluster_id",
                "enable": False,
                "albBuild": "your_alb_build",
                "albID": "your_alb_id",
                "albType": "your_alb_type",
                "authBuild": "your_auth_build",
                "createdDate": "your_created_date",
                "disableDeployment": True,
                "loadBalancerHostname": "your_load_balancer_hostname",
                "name": "your_name",
                "numOfInstances": "your_num_of_instances",
                "resize": False,
                "state": "your_state",
                "status": "your_status",
                "zone": "your_zone"
            }
        }

    def test_successful_disable_alb(self):
        mock_ingress_alb_beta = MagicMock()
        mock_ingress_alb_beta.disableAlb.return_value = (False, True, {"alb_info": "your_alb_info"})

        with unittest.mock.patch(
            "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_disable.IngressALBBeta",
            return_value=mock_ingress_alb_beta
        ):
            with unittest.mock.patch(
                "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_disable.Authenticator.get_iam_token",
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

    def test_error_disabling_alb(self):
        mock_ingress_alb_beta = MagicMock()
        mock_ingress_alb_beta.disableAlb.return_value = (True, False, {"alb_info": "your_alb_info"})

        with unittest.mock.patch(
            "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_disable.IngressALBBeta",
            return_value=mock_ingress_alb_beta
        ):
            with unittest.mock.patch(
                "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_disable.Authenticator.get_iam_token",
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
                        msg="Error disabling ingress ALB", meta={"alb_info": "your_alb_info"}
                    )

if __name__ == "__main__":
    unittest.main()
