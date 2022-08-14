#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@File    :   startup.py
@Time    :   2022/08/14 10:29:51
@Author  :   Aditya Divakaran
@Version :   1.0
@Contact :   adi.develops@gmail.com
@License :   MIT License, Aditya Divakaran
@Desc    :   Startup file that gets env vars, logging settings etc. for the whole project
"""

import os
import sys
import logging

# Valid but pylint acts up
from pydantic import BaseModel  # pylint: disable=no-name-in-module

# Load .env setup
# Note: Remove this setup in case of docker environment
from dotenv import load_dotenv

# Using pydantic for robust casting (1, True, on, true / 0, False, off, false)
class EnvLoader(BaseModel):  # pylint: disable=too-few-public-methods
    """Env Loading Class - Meant to act as a single blueprint for loading env
    variables and having validation checks for each variable loaded through the
    pydantic class

    Args:
        BaseModel (pydantic.BaseModel): Base Class for pydantic
    """

    debug_mode: bool


def __init__():
    """Wrapper for commands to be run during app startup"""
    load_dotenv(".env")

    # Get the initial env to understand if we should run in debug mode
    try:
        debug_mode: bool = EnvLoader(debug_mode=os.environ["DEBUG_MODE"]).debug_mode
    except KeyError as keyerr:
        sys.stderr.write(
            "Env vars could not be set. Please check Env Variables!", keyerr
        )
        sys.exit(1)

    # Set up logging according to mode set
    if debug_mode:
        logging_debug_level = logging.DEBUG
        logging_format = "[%(asctime)s] %(levelname)s \
        [%(name)s - %(filename)s.%(funcName)s:%(lineno)d] %(message)s"
    else:
        logging_debug_level = logging.INFO
        logging_format = "[%(asctime)s] %(levelname)s [%(name)s] %(message)s"

    log_file_path: str = "data/app.log"
    # Note: Path to file handler is relative to root script that's run! Can be set as absolute path
    logging.basicConfig(
        format=logging_format,
        datefmt="%a, %d %b %Y %H:%M:%S",
        level=logging_debug_level,
        handlers=[
            logging.FileHandler(log_file_path, mode="w"),
            logging.StreamHandler(sys.stderr),
        ],
    )

    log = logging.getLogger(__name__)

    _ = log.info("DEBUG Mode") if debug_mode else log.info("DEBUG mode disabled")
