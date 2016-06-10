import sys

from mcc.loggers import LOG


def catch_ctrl_c(func):
    """Catch the KeyboardInterrupt exception and handle it gracefully.

    This avoids displaying an unnecessary traceback when the user interrupts
    the program.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            LOG.warn("Interrupted by the user.")
            sys.exit(130)

    return inner
