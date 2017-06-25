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


# Global
VERBOSE_LEVEL = LogLevel.kDEFAULT


# Functions
def printv(string="", *params, **kwargs):
    """Prints the value according to the verbose mode.
    kwargs contains the verbose mode according to: verbose=<LogLevel>.
    Eg: printv("A text", 2, verbose=LogLevel.kFINE
    """
    verbose = LogLevel.kDEFAULT

    if len(kwargs) >= 1:
        verbose = kwargs['verbose']

    if verbose.value <= VERBOSE_LEVEL.value:
        print(string, *params)
