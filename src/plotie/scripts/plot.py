#!/usr/bin/env python
import os
import sys
from getpass import getpass
import errno
from lxml.etree import XMLSyntaxError

# Propylon
from mt_models.note import Compilerscomments
from joplin.utils.context_managers import BackendManager
from joplin.exceptions import BackendConnectionError

# Project
from mcc.migrate import Migrater
from mcc.cli.version import get_version
from mcc.cli.parser import parsed_args
from mcc.cli.utils import catch_ctrl_c
from mcc.loggers import set_log
from mcc.common import LOG
from mcc.lrms import LrmsConnection
from mcc import exceptions as exc


@catch_ctrl_c
def main():
    """The main body of the CLI program.
    """
    set_log(parsed_args)
    args = parsed_args

    if args.wants_version:
        sys.stdout.write(get_version() + os.linesep)
    else:
        if args.debug:
            LOG.info(
                "Debug mode"
            )
        else:
            pass

if __name__ == "__main__":
    main()
