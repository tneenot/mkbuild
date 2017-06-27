#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) @YEAR@ -  @DEVELOPER@
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
__author__ = "@DEVELOPER@"
__version__ = "0.1.00"
__email__ = "@EMAIL@"
__year__ = @YEAR@

# Import
from core.core import *


# Specific command implementation
class SpecificCommand(FacilityCommand):
    def __init__(self):
        super().__init__("<Specific usage command>")


if __name__ == "__main__":
    specific_command = SpecificCommand()
    specific_command.read_args(sys.argv[1:])
