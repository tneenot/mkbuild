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


# Functions
def get_command_list(commandPath):
    return [command for command in glob.glob(commandPath + "/*.py") if command.find("__init__.py", 0) == -1]


def usage():
    print("'" + APP_NAME + "' is a convenience application for project building management")

    print("\nUsage:")
    print("\t", APP_NAME, "[-?|--help] [-v|--version] <command> <options>")

    print("\nParameters:")
    print("\t-?|--help: shows this help.")
    print("\t-v|--version: shows the current version.")
    commands = get_command_list(Global.MKBUILD_COMMANDS)
    if len(commands) > 0:
        print("\nCommands:")
        for command in commands:
            os.system(command + " --resume")


def retreive_command_and_run(values):
    if len(values) >= 1:
        command = ""
        try:
            commands = get_command_list(Global.MKBUILD_COMMANDS)
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


def read_args(argv):
    try:
        args, values = getopt.getopt(argv, "?v", ["help", "version"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for arg, value in args:
        if arg in ("-?", "--help"):
            usage()
            sys.exit()
        elif arg in ("-v", "--version"):
            print(APP_NAME, "version", __version__, ". Written by:", __author__ + ". ")
            print(APP_NAME, "is distributed under GPLv3 condition. Copyright (C)", __year__, __author__,
                  ".This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to "
                  "redistribute it under GPLv3 conditions.")
            sys.exit()

    return values


def main(args):
    """main function"""
    values = read_args(args)
    read_project_configuration()
    retreive_command_and_run(values)


# ### Main method
if __name__ == "__main__":
    WORKING_DIR = os.path.dirname(sys.argv[0])
    Global.MKBUILD_COMMANDS = os.getenv("MKBUILD_COMMANDS", "/usr/share/mkbuild/commands/")
    APP_NAME = os.path.basename(sys.argv[0].split('.')[0])
    main(sys.argv[1:])
