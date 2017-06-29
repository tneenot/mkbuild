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

# imports
import getopt
import glob
import sys
from commands.core.core import *


# ## Metadata
__author__ = "Tioben Neenot"
__version__ = "0.1.00"
__email__ = "tioben.neenot@laposte.net"
__year__ = 2017


# Specific command implementation
class MKBuildCommand(FacilityCommand):
    def __init__(self):
        super().__init__("is a convenience application for project building management")

    def command_usage_description(self, applicationName):
        print("\t<command>: command to run (see Commands below)")
        commands = self.__get_command_list(Global.MKBUILD_COMMANDS)
        if len(commands) > 0:
            print("\nCommands:")
            for command in commands:
                os.system(command + " --resume")

    def __get_command_list(self, commandPath):
        return [command for command in glob.glob(commandPath + "/*.py") if command.find("__init__.py", 0) == -1]

    def command_usage_resume(self, applicationName):
        print("\t", applicationName, "<command> [<args>]")

    def read_command_args(self, args, values):
        if len(values) >= 1:
            try:
                commands = self.__get_command_list(Global.MKBUILD_COMMANDS)
                command_idx = commands.index(Global.MKBUILD_COMMANDS + "/" + values[0] + ".py")
                command = commands[command_idx]
            except ValueError:
                print("Command ", values[0], "not found")
                sys.exit(2)

            if len(command) == 0:
                raise Exception("Command " + values[0] + " not found")

            os.putenv("MKBUILD_COMMANDS", Global.MKBUILD_COMMANDS)

            if len(values) >= 2:
                os.system(command + " " + " ".join(str(s) for s in values[1:]))
            else:
                os.system(command)


# Main
if __name__ == "__main__":
    mkbuild_command = MKBuildCommand()
    mkbuild_command.read_args(sys.argv[1:])
