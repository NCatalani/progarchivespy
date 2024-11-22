import os
import sys
import structlog
from logging import _nameToLevel

# Default values
DEFAULT_LOG_OUTPUT = "stdout"
DEFAULT_LOG_LEVEL = "WARNING"


def configure_logger() -> structlog.BoundLogger:
    """
    Configures the application's logger.

    Logging output and level can be configured via environment variables:
        - PROGARCHIVESPY_LOG_OUTPUT (default: "stdout")
            Where to output logs. Options are "stdout", "stderr", "null", or a file path.

        - PROGARCHIVESPY_LOG_LEVEL (default: "WARNING")
            Minimum log level to output. Options are the names of the default "logging" module levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).

    Returns:
        structlog.BoundLogger: Configured logger.
    """
    log_output = os.getenv("PROGARCHIVESPY_LOG_OUTPUT", DEFAULT_LOG_OUTPUT).lower()
    log_level = os.getenv("PROGARCHIVESPY_LOG_LEVEL", DEFAULT_LOG_LEVEL).upper()

    if log_output in ["stdout", "/dev/stdout"]:
        log_destination = sys.stdout
    elif log_output in ["stderr", "/dev/stderr"]:
        log_destination = sys.stderr
    elif log_output in ["null", "/dev/null"]:
        log_destination = open("/dev/null", "w")
    else:
        log_destination = open(log_output, "a")

    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.TimeStamper(fmt="ISO"),
            structlog.dev.ConsoleRenderer(colors=True),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(
            _nameToLevel.get(log_level, 30)
        ),
        logger_factory=structlog.PrintLoggerFactory(file=log_destination),
        cache_logger_on_first_use=False,
    )

    return structlog.get_logger("progarchivespy")


logger = configure_logger()
