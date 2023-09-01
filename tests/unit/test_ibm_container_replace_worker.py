import unittest
from unittest.mock import patch, MagicMock
from plugins.module_utils.auth import Authenticator
from plugins.module_utils.sdk.container.beta import Beta
from plugins.modules.ibm_container_replace_worker import run_module

class TestIbmContainerReplaceWorker(unittest.TestCase):
    @patch("plugins.module_utils.auth.Authenticator.get_iam_token")
    @patch.object(Beta, "replaceWorker")
    def test_run_module_successful(self, mock_replace_worker, mock_get_iam_token):
        mock_get_iam_token.return_value = "mocked_iam_token"
        mock_replace_worker.return_value = (False, True)

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "mocked_api_key",
            "resource_group_id": "mocked_resource_group_id",
            "config": {
                "cluster": "mocked_cluster",
                "update": True,
                "workerID": "mocked_worker_id",
            },
        }

        module = MagicMock()
        module.params = args
        run_module()

        mock_get_iam_token.assert_called_once()
        mock_replace_worker.assert_called_once_with(args["config"])
        module.exit_json.assert_called_once_with(changed=True)
        module.fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
