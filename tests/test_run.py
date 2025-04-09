import sys
from pathlib import Path
from unittest.mock import patch


# some test to achieve coverage in _run.py, suggested by Copilot
def test_run_module():
    """Test that the run_module function is called with the correct arguments."""
    # Arrange
    sys.path.insert(0, Path(__file__).parent.parent.as_posix())
    # Act
    with patch("runpy.run_module") as mock_run_module:
        import sple_artifacts_uploader._run  # noqa: F401

        # Assert
        mock_run_module.assert_called_once_with("sple_artifacts_uploader.main", run_name="__main__")
