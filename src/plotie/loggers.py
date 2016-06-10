import logging


def get_logger(separator=';', level=logging.WARN):
    """Initiate a logger

    :param separator: the separator to separate time and information
    :type separator: basestring
    :param level: level of log
    :type level: int
    :return: a logger
    """
    FORMAT = '[%(asctime)s]{0}  %(message)s'.format(separator)
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    return logger


LOG = get_logger(__package__)


def set_log(args):
    """
    Parse the command-line arguments and set the log level.

    Also configures the module logger.
    """
    if args.is_debugging:
        LOG.setLevel(logging.DEBUG)
        LOG.info("Logging level set to DEBUG")
    elif args.is_verbose:
        LOG.setLevel(logging.INFO)
        LOG.info("Logging level set to INFO")
