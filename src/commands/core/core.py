# -*- coding: utf-8 -*-

# Copyright (C) 2017 -  Tioben Neenot
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

# ## Metadata
__author__ = "Tioben Neenot"
__version__ = "0.1.00"
__email__ = "tioben.neenot@laposte.net"
__year__ = 2017

# Import
from enum import Enum
import time, os

# ## Globals
MKBUILD_CONFIG_FILE = ".mkbuild"
MKBUILD_CONFIG = dict()
MKBUILD_COMMANDS = ""


# Enumerations
class ErrorType(Enum):
    kNO_ERROR = 0
    kNO_DIR = 1
    kMISSING_ARG = 2


class LogLevel(Enum):
    kDEFAULT = 0
    kFINE = 1
    kFINEST = 2
    kDEPTH = 3


class Global(object):
    LOG_VERBOSE_LEVEL = LogLevel.kDEFAULT
    MKBUILD_CONFIG_FILE = ".mkbuild"
    MKBUILD_CONFIG = dict()
    MKBUILD_COMMANDS = ""


# Functions
def printv(string="", *params, **kwargs):
    """Prints the value according to the verbose mode.
    kwargs contains the verbose mode according to: verbose=<LogLevel>.
    Eg: printv("A text", 2, verbose=LogLevel.kFINE
    """
    verbose = LogLevel.kDEFAULT

    if len(kwargs) >= 1:
        verbose = kwargs['verbose']

    if verbose.value <= Global.LOG_VERBOSE_LEVEL.value:
        print(string, *params)


def create_project_config_file(directory):
    """Create the project configuration file to the directory path"""
    if os.path.isfile(directory + "/" + Global.MKBUILD_CONFIG_FILE) is True:
        return

    config_file = open(directory + "/" + Global.MKBUILD_CONFIG_FILE, "w", encoding="utf-8")
    config_file.write("# Creation date: " + time.asctime() + "\n")
    config_file.write("project = " + directory + "\n")
    config_file.write("author = " + os.environ['USER'] + "\n")
    config_file.close()


def read_project_configuration(directory):
    """Read the project configuration file if exists"""
    if os.path.isfile(directory + "/" + Global.MKBUILD_CONFIG_FILE):
        config_file = open(directory + "/" + Global.MKBUILD_CONFIG_FILE, "r")
        raw_buffer = config_file.read()
        config_file.close()

        buffer = raw_buffer.split("\n")
        for buf_line in buffer:
            if len(buf_line) > 0 and buf_line[0] != '#':
                key, value = buf_line.split("=")
                MKBUILD_CONFIG[key.strip()] = value.strip()

        printv("Project name:", Global.MKBUILD_CONFIG['project'])
