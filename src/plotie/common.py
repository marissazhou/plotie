# coding: utf-8
# Python
import re
import logging

# Project
from .loggers import get_logger

# LOG information
REPORT_SEPARATOR = ';'
LOG = get_logger(REPORT_SEPARATOR, level=logging.INFO)
