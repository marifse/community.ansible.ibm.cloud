import unittest
from unittest.mock import patch, MagicMock
from plugins.module_utils.auth import Authenticator
from plugins.module_utils.sdk.container.storage import Storage
from plugins.modules.ibm_container_storage_attachment_delete import run_module

class TestIbmContainerStorageAttachmentDelete(unittest.TestCase):
    @patch("plugins.module_utils.auth.Authenticator.get_iam_token")
    @patch.object(Storage, "delete_storage_attachment")
    def test_run_module_successful(self, mock_delete_storage_attachment, mock_get_iam_token):
        mock_get_iam_token.return_value = "mocked_iam_token"
        mock_delete_storage_attachment.return_value = (False, True, "mocked_storage_info")

        # Create a test arguments dictionary similar to what Ansible would pass
        args = {
            "ibmcloud_api_key": "mocked_api_key",
            "resource_group_id": "mocked_resource_group_id",
            "vpcVolumeAttachmentConfig": {
                "cluster": "mocked_cluster",
                "volumeAttachmentID": "mocked_volume_attachment_id",
                "worker": "mocked_worker_id",
            },
        }

        module = MagicMock()
        module.params = args
        run_module()

        mock_get_iam_token.assert_called_once()
        mock_delete_storage_attachment.assert_called_once_with(args["vpcVolumeAttachmentConfig"])
        module.exit_json.assert_called_once_with(changed=True, storage_info="mocked_storage_info")
        module.fail_json.assert_not_called()

if __name__ == "__main__":
    unittest.main()
