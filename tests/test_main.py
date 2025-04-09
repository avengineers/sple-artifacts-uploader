from pathlib import Path
from unittest.mock import Mock, patch

import pytest
from py_app_dev.core.exceptions import UserNotificationException
from typer.testing import CliRunner

from sple_artifacts_uploader import __version__
from sple_artifacts_uploader.main import app, main

runner = CliRunner()


def test_version() -> None:
    """Test the version command from the main function."""
    # Arrange + Act
    result = runner.invoke(app, ["--version"])
    # Assert
    assert result.exit_code == 0
    assert "sple_artifacts_uploader" in result.output
    assert __version__ in result.output


def test_upload_file_missing_arguments() -> None:
    """Test the upload-file command with missing arguments."""
    # Arrange + Act
    result = runner.invoke(app, ["upload-file"])
    # Assert
    assert result.exit_code != 0


@patch("sple_artifacts_uploader.artifact_uploader.ArtifactUploader.upload_file")
def test_upload_file_with_arguments(mock_upload_file: Mock) -> None:
    """Test the mocked upload-file command with mandatory arguments."""
    # Arrange
    artifact_path = "test_artifact.txt"
    destination_url = "http://example.com/upload"
    username = "bibi"
    password = "kartoffelbrei"  # noqa: S105
    timeout = 15
    # Act
    result = runner.invoke(
        app,
        [
            "upload-file",
            "--artifact-path",
            artifact_path,
            "--destination-url",
            destination_url,
            "--username",
            username,
            "--password",
            password,
            "--timeout",
            str(timeout),
        ],
    )
    # Assert
    assert result.exit_code == 0
    assert mock_upload_file.called
    mock_upload_file.assert_called_once_with(Path(artifact_path), destination_url, username, password, timeout)


@patch("sple_artifacts_uploader.artifact_uploader.ArtifactUploader.upload_file")
def test_upload_file_default_timeout(mock_upload_file: Mock) -> None:
    """Test the upload-file command with default timeout (10s)."""
    # Arrange
    artifact_path = "test_artifact.txt"
    destination_url = "http://example.com/upload"
    username = "bibi"
    password = "kartoffelbrei"  # noqa: S105
    # Act
    result = runner.invoke(
        app,
        [
            "upload-file",
            "--artifact-path",
            artifact_path,
            "--destination-url",
            destination_url,
            "--username",
            username,
            "--password",
            password,
        ],
    )
    # Assert
    assert result.exit_code == 0
    assert mock_upload_file.called
    mock_upload_file.assert_called_once_with(Path(artifact_path), destination_url, username, password, 10)


@patch("sple_artifacts_uploader.main.app")
def test_main(mock_app: Mock) -> None:
    """Test the main function."""
    # Arrange + Act
    main()
    # Assert
    mock_app.assert_called_once()


@patch("sple_artifacts_uploader.main.app")
def test_main_user_notification_exception(mock_app: Mock) -> None:
    """Test the main function when a UserNotificationException is raised."""
    # Arrange
    mock_app.side_effect = UserNotificationException("Some error in app!")
    # Act
    with pytest.raises(SystemExit) as exc_info:
        main()
    # Assert
    assert exc_info.value.code == 1
