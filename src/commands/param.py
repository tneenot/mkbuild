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
__version__ = "0.1.00"
__email__ = "tioben.neenot@laposte.net"
__year__ = 2017

# Import
from core.core import *


# Specific command implementation
class ParametersCommand(FacilityCommand):
    def __init__(self):
        super().__init__("fix, list or update parameters for files into projects")

    def command_usage_resume(self, applicationName):
        print("\t", applicationName, "[-l|--list] | [-u|--update <file>]")

    def get_args_list(self):
        return "lu:", ["list", "update="]

    def command_usage_description(self, applicationName):
        print("\t-l|--list: list all parameters from ", Global.MKBUILD_CONFIG_FILE, " for the current project.")
        print("\t-u|--update <file>: update parameters into given file. File can be specified with wildcards.")

    def read_command_args(self, args, values):
        for arg, value in args:
            if arg in ("-l", "--list"):
                for key, value in Global.MKBUILD_CONFIG.items():
                    print("\t", key, "=", value)
            if arg in ("-u", "--update"):
                file_list = glob.glob(value)
                for file in file_list:
                    copy_file_and_parse(file, file)


# Main
if __name__ == "__main__":
    parameters = ParametersCommand()
    parameters.read_args(sys.argv[1:])
