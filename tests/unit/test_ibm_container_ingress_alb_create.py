import unittest
from unittest.mock import MagicMock
from ansible.module_utils.basic import AnsibleModule
from ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_create import run_module

class TestIBMContainerIngressALBCreateModule(unittest.TestCase):

    def setUp(self):
        self.module_args = {
            "ibmcloud_api_key": "your_api_key",
            "resource_group_id": "your_resource_group",
            "config": {
                "cluster": "your_cluster_id",
                "enableByDefault": True,
                "ingressImage": "your_ingress_image",
                "type": "your_alb_type",
                "zone": "your_alb_zone"
            }
        }

    def test_successful_create_alb(self):
        mock_ingress_alb_beta = MagicMock()
        mock_ingress_alb_beta.createAlb.return_value = (False, True, {"alb_info": "your_alb_info"})

        with unittest.mock.patch(
            "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_create.IngressALBBeta",
            return_value=mock_ingress_alb_beta
        ):
            with unittest.mock.patch(
                "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_create.Authenticator.get_iam_token",
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
                        changed=True, alb_info={"alb_info": "your_alb_info"}
                    )

    def test_error_creating_alb(self):
        mock_ingress_alb_beta = MagicMock()
        mock_ingress_alb_beta.createAlb.return_value = (True, False, {"alb_info": "your_alb_info"})

        with unittest.mock.patch(
            "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_create.IngressALBBeta",
            return_value=mock_ingress_alb_beta
        ):
            with unittest.mock.patch(
                "ibm.custom_iks_collection.plugins.modules.ibm_container_ingress_alb_create.Authenticator.get_iam_token",
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
                        msg="Error creating ingress ALB", meta={"alb_info": "your_alb_info"}
                    )

if __name__ == "__main__":
    unittest.main()
