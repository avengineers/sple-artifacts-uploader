from pathlib import Path
from unittest.mock import Mock, call, mock_open, patch

import requests
from py_app_dev.core.docs_utils import validates

from sple_artifacts_uploader.artifact_uploader import ArtifactUploader


@validates("REQ-ARTIFACTS-UPLOADER-1.0")
@patch("loguru._logger.Logger.info")
@patch("sple_artifacts_uploader.artifact_uploader.requests.put")
@patch("builtins.open", new_callable=mock_open, read_data="dummy data")
def test_upload_file_success(mock_file: Mock, mock_put: Mock, mock_info: Mock) -> None:
    """Test the upload_file method for a successful upload."""
    # Arrange
    mock_put.return_value.status_code = 200
    artifact_path = Path("dummy_path")
    destination_url = "http://example.com/upload"
    username = "bibi"
    password = "kartoffelbrei"  # noqa: S105
    uploader = ArtifactUploader()

    # Act
    uploader.upload_file(artifact_path, destination_url, username, password)

    # Assert
    mock_file.assert_called_once_with(artifact_path, "rb")
    mock_put.assert_called_once_with(
        destination_url,
        data=mock_file.return_value,
        auth=(username, password),
        timeout=10,
    )
    expected_calls = [call(f"Uploading artifact from {artifact_path} to {destination_url}"), call("Upload successful!")]
    mock_info.assert_has_calls(expected_calls, any_order=True)


@patch("loguru._logger.Logger.warning")
@patch("sple_artifacts_uploader.artifact_uploader.requests.put")
@patch("builtins.open", new_callable=mock_open, read_data="dummy data")
def test_upload_file_failure(mock_file: Mock, mock_put: Mock, mock_warning: Mock) -> None:
    """Test the upload_file method for a failed upload."""
    # Arrange
    mock_put.return_value.status_code = 400
    artifact_path = Path("dummy_path")
    destination_url = "http://example.com/upload"
    username = "bibi"
    password = "kartoffelbrei"  # noqa: S105
    timeout = 20
    uploader = ArtifactUploader()

    # Act
    uploader.upload_file(artifact_path, destination_url, username, password, timeout)

    # Assert
    mock_file.assert_called_once_with(artifact_path, "rb")
    mock_put.assert_called_once_with(
        destination_url,
        data=mock_file.return_value,
        auth=(username, password),
        timeout=timeout,
    )
    expected_calls = [
        call(f"Failed to upload. Status code: {mock_put.return_value.status_code}"),
    ]
    mock_warning.assert_has_calls(expected_calls, any_order=True)


@patch("loguru._logger.Logger.warning")
@patch("sple_artifacts_uploader.artifact_uploader.requests.put")
@patch("builtins.open", new_callable=mock_open, read_data="dummy data")
def test_upload_file_timeout(mock_file: Mock, mock_put: Mock, mock_warning: Mock) -> None:
    """Test the upload_file method for a timeout exception."""
    # Arrange
    mock_put.side_effect = requests.exceptions.Timeout
    artifact_path = Path("dummy_path")
    destination_url = "http://example.com/upload"
    username = "bibi"
    password = "kartoffelbrei"  # noqa: S105
    uploader = ArtifactUploader()

    # Act
    uploader.upload_file(artifact_path, destination_url, username, password)

    # Assert
    mock_file.assert_called_once_with(artifact_path, "rb")
    mock_put.assert_called_once_with(
        destination_url,
        data=mock_file.return_value,
        auth=(username, password),
        timeout=10,
    )
    expected_calls = [call("Upload failed due to a timeout.")]
    mock_warning.assert_has_calls(expected_calls, any_order=True)


@patch("loguru._logger.Logger.warning")
@patch("sple_artifacts_uploader.artifact_uploader.requests.put")
@patch("builtins.open", new_callable=mock_open, read_data="dummy data")
def test_upload_file_request_exception(mock_file: Mock, mock_put: Mock, mock_warning: Mock) -> None:
    """Test the upload_file method for a request exception."""
    # Arrange
    mock_put.side_effect = requests.exceptions.RequestException("Error")
    artifact_path = Path("dummy_path")
    destination_url = "http://example.com/upload"
    username = "bibi"
    password = "kartoffelbrei"  # noqa: S105
    uploader = ArtifactUploader()

    # Act
    uploader.upload_file(artifact_path, destination_url, username, password)

    # Assert
    mock_file.assert_called_once_with(artifact_path, "rb")
    mock_put.assert_called_once_with(
        destination_url,
        data=mock_file.return_value,
        auth=(username, password),
        timeout=10,
    )
    expected_calls = [call(f"An error occurred during upload: {mock_put.side_effect}")]
    mock_warning.assert_has_calls(expected_calls, any_order=True)
