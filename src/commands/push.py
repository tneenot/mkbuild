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
import os, sys, getopt
from core.core import *


# Functions
def usage_resume(withTab=False):
    prefix = ""
    if withTab == True:
        prefix = "\t"

    print(prefix, APP_NAME + ": push a new command into the commands repository of mkbuild.")


def usage():
    usage_resume()

    print("\nUsage:")
    print("\t", APP_NAME, "[-?|--help] [-v|--version] [--resume] [-f|--force] <command>")

    print("\nParameters:")
    print("\t-?|--help: shows this help.")
    print("\t-v|--version: shows the current version.")
    print("\t--resume: shows only the sum up of the help.")
    print("\t-f|--force: specifies if the command will override an existing one.")
    print(
        "\t<command>: command to push into the " + Global.MKBUILD_COMMANDS + ". If command exists yet it won't be replaced, except if -f is defining.")


def push_command_to(mkbuildCommandPath, overrideMode, command):
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


def read_args(argv):
    try:
        args, values = getopt.getopt(argv, "?vf", ["help", "version", "force", "resume"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    override_mode = False
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
        elif arg in ("--resume"):
            usage_resume(True)
            sys.exit()
        elif arg in ("-f", "--force"):
            override_mode = True

    if len(values) > 0:
        push_command_to(Global.MKBUILD_COMMANDS, override_mode, values[0])


def main(args):
    """main function"""
    read_args(args)


if __name__ == "__main__":
    APP_NAME = os.path.basename(sys.argv[0].split('.')[0])
    Global.MKBUILD_COMMANDS = os.getenv("MKBUILD_COMMANDS", "/usr/share/mkbuild/commands/")
    main(sys.argv[1:])
