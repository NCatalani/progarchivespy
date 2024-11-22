import os
import pytest
from progarchivespy.common.logger import configure_logger
from unittest.mock import patch, MagicMock


@pytest.fixture
def mock_env():
    """Fixture to reset environment variables after each test."""
    original_env = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.mark.usefixtures("mock_env")
class TestLoggerConfig:
    @pytest.fixture(autouse=True)
    def setup_env(self):
        """Default environment variables for tests."""
        os.environ["PROGARCHIVESPY_LOG_OUTPUT"] = "stdout"
        os.environ["PROGARCHIVESPY_LOG_LEVEL"] = "INFO"

    @patch("sys.stderr", new_callable=MagicMock)
    def test_log_to_stderr(self, mock_stderr):
        """Test logging to stderr."""
        os.environ["PROGARCHIVESPY_LOG_OUTPUT"] = "stderr"
        logger = configure_logger()
        logger.warning("Warning message")
        assert mock_stderr.write.called, "stderr.write should be called"

    @patch("builtins.open", mock_open=True)
    def test_log_to_file(self, mock_open_fn):
        """Test logging to a file."""
        os.environ["PROGARCHIVESPY_LOG_OUTPUT"] = "test.log"
        logger = configure_logger()
        logger.error("Error message")
        mock_open_fn.assert_called_with("test.log", "a")

    @patch("builtins.open", new_callable=MagicMock)
    def test_log_to_null(self, mock_open_fn):
        """Test logging to /dev/null."""
        os.environ["PROGARCHIVESPY_LOG_OUTPUT"] = "null"
        logger = configure_logger()  # Reinitialize logger with new settings
        logger.info("This log should go to null")
        mock_open_fn.assert_called_with("/dev/null", "w")  # Verify /dev/null is used
