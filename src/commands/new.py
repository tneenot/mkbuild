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
import sys, getopt
from core.core import *


# Functions
def usage_resume(withTab=False):
    prefix = ""
    if withTab == True:
        prefix = "\t"

    print(prefix, APP_NAME + ": create a new project.")


def usage():
    usage_resume()

    print("\nUsage:")
    print("\t", APP_NAME, "[-?|--help] [-v|--version] [--resume] [-g|--git] <project>")

    print("\nParameters:")
    print("\t-?|--help: shows this help.")
    print("\t-v|--version: shows the current version.")
    print("\t--resume: shows only the sum up of the help.")
    print("\t-g|--git: run the git initialization")
    print("\t<project>: name of project.")


def create_project_directory(directory, gitInitialization):
    if os.path.exists(directory):
        raise FileExistsError("This directory projet exists yet: " + directory)

    os.mkdir(directory, 0o765)
    create_project_config_file(directory)

    if gitInitialization == True:
        os.system("git init " + directory)
        # todo: Create standard .gitignore
        # todo: set all current standard files as initial commit


def read_args(argv):
    try:
        args, values = getopt.getopt(argv, "?vg", ["help", "version", "git", "resume"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    git_init = False
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
        elif arg in ("-g", "--git"):
            git_init = True

    if len(values) > 0:
        create_project_directory(values[0], git_init)


def main(args):
    """main function"""
    read_args(args)


if __name__ == "__main__":
    APP_NAME = os.path.basename(sys.argv[0].split('.')[0])
    Global.MKBUILD_COMMANDS = os.getenv("MKBUILD_COMMANDS", "/usr/share/mkbuild/commands/")
    main(sys.argv[1:])
