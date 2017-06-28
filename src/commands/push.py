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
class PushCommand(FacilityCommand):
    def __init__(self):
        super().__init__("push a new command into the commands repository of mkbuild.")

    def read_implementation_args(self, args, values):
        override_mode = False
        for arg, value in args:
            if arg in ("-f", "--force"):
                override_mode = True

        if len(values) > 0:
            self.push_command_to(Global.MKBUILD_COMMANDS, override_mode, values[0])

    def full_usage(self, applicationName):
        print("\t", applicationName, "[-f|--force] <command>")

    def other_usage_description(self, applicationName):
        print("\t-f|--force: specifies if the command will override an existing one.")
        print(
        "\t<command>: command to push into the " + Global.MKBUILD_COMMANDS + ". If command exists yet it won't be replaced, except if -f is defining.")

    def get_args_list(self):
        return "f", ["force"]

    def push_command_to(self, mkbuildCommandPath, overrideMode, command):
        valid_copy = False
        if os.path.exists(mkbuildCommandPath + "/" + command) == True:
            if overrideMode == False:
                print("Command", command, "exists yet.")
                sys.exit(1)
            elif overrideMode == True:
                valid_copy = True
        else:
            valid_copy = True

        if valid_copy == True:
            from shutil import copy2
            import stat
            copy2(command, mkbuildCommandPath)
            os.chmod(mkbuildCommandPath + "/" + command,
                     stat.S_IREAD | stat.S_IEXEC | stat.S_IWRITE | stat.S_IXOTH | stat.S_IROTH | stat.S_IWOTH | stat.S_IXGRP | stat.S_IRGRP | stat.S_IWOTH)


# Main
if __name__ == "__main__":
    push_command = PushCommand()
    push_command.read_args(sys.argv[1:])
