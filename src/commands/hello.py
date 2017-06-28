#!/usr/bin/env python3
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

# Meta
__author__ = "Tioben Neenot"
__version__ = "1.0.00"
__email__ = "tioben.neenot@laposte.net"
__year__ = 2017

# Import
from core.core import *


# Specific command implementation
class HelloCommand(FacilityCommand):
    def __init__(self):
        super().__init__("a convenience command for mkbuild testing commands repository access.")


# Main
if __name__ == "__main__":
    hello_command = HelloCommand()
    hello_command.read_args(sys.argv[1:])
