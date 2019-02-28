import sys
from loguru import logger

from const import (
    __version__,
    REQUIRED_PYTHON_VER
)


def validate_python() -> None:
    """Validate that the right Python version is running."""
    if sys.version_info[:3] < REQUIRED_PYTHON_VER:
        logger.debug("Visual Census requires at least Python {}.{}.{}".format(
            *REQUIRED_PYTHON_VER
        ))
        sys.exit(1)


def main():
    """Start Visual Census."""
    validate_python()
    from visualcensus.backend.raspi.tasks import task_remoter
    task_remoter.start()


if __name__ == "__main__":
    sys.exit(main())
