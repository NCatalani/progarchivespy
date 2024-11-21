import os
import sys
import structlog
from logging import _nameToLevel

# Default values
DEFAULT_LOG_OUTPUT = "stdout"
DEFAULT_LOG_LEVEL = "WARNING"

# Read environment variables
log_output = os.getenv("PROGARCHIVESPY_LOG_OUTPUT", DEFAULT_LOG_OUTPUT).lower()
log_level = os.getenv("PROGARCHIVESPY_LOG_LEVEL", DEFAULT_LOG_LEVEL).upper()

# Determine log destination
if log_output in ["stdout", "/dev/stdout"]:
    log_destination = sys.stdout
elif log_output in ["stderr", "/dev/stderr"]:
    log_destination = sys.stderr
elif log_output in ["null", "/dev/null"]:
    log_destination = open("/dev/null", "w")
else:
    log_destination = open(log_output, "a")

# Configure structlog
structlog.configure(
    processors=[
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(fmt="ISO"),
        structlog.dev.ConsoleRenderer(colors=True),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(_nameToLevel[log_level]),
    logger_factory=structlog.PrintLoggerFactory(file=log_destination),  # Direct output
    cache_logger_on_first_use=False,
)

# Create a logger
logger = structlog.get_logger("progarchivespy")
