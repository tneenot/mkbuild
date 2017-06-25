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
import os, sys, getopt

# Functions
def usage():
    print("'" + APP_NAME + "' is a convenience command for mkbuild testing commands repository access.")

    print("\nUsage:")
    print("\t" , APP_NAME,"[-?|--help] [-v|--version]")

    print("\nParameters:")
    print("\t-?|--help: shows this help.")
    print("\t-v|--version: shows the current version.")

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

def main(args):
    """main function"""
    read_args(args)
    print("Hello world test command")

if __name__ == "__main__":
    APP_NAME = os.path.basename(sys.argv[0].split('.')[0])
    main(sys.argv[1:])

