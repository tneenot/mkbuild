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
import os
import sys
import time
import glob

from mkbuild.core import *

# ## Metadata
__author__ = "Tioben Neenot"
__version__ = "0.1.00"
__email__ = "tioben.neenot@laposte.net"
__year__ = 2017

# ## Globals
MKBUILD_CONFIG_FILE = ".mkbuild"
MKBUILD_CONFIG = dict()
MKBUILD_COMMANDS = ""


def usage():
    print(APP_NAME, "is a convenience application for project building management")
    print("")
    print(APP_NAME,
          "[-?|--help] [-v|--version] [-p|--project=<project_name> [-m|--scm <scm_type>] -i|-init <working_directory>]")
    print("")
    print("Parameters:")
    print("\t-?|--help: shows this help.")
    print("\t-v|--version: shows the current version.")
    print("\t-p|--project: project's name.")
    print("\t-m|--scm: initial software configuration management type. Use following key is supported: git.")
    print(
        "\t-i|-init: initialize the given working directory as the main project directory. The --project argument must be dekFINEd before this option.")


def create_project_config_file(directoryPath, projectName):
    """Create the project configuration file to the directory path"""
    if os.path.isfile(directoryPath + "/" + MKBUILD_CONFIG_FILE) is True:
        return

    config_file = open(directoryPath + "/" + MKBUILD_CONFIG_FILE, "w", encoding="utf-8")
    config_file.write("# Creation date: " + time.asctime() + "\n")
    config_file.write("project = " + projectName + "\n")
    config_file.write("author = " + os.environ['USER'] + "\n")
    config_file.close()


def init_project_on(directoryPath, projectName, **kwargs):
    """Initialize a project directory for the given path"""
    WORKING_DIR = directoryPath
    printv("Project directory:", WORKING_DIR)
    try:
        os.makedirs(WORKING_DIR)
    except FileExistsError:
        pass

    if os.path.isdir(WORKING_DIR) == False:
        return ErrorType.kNO_DIR

    create_project_config_file(directoryPath, projectName)
    # todo: import all standard models

    if "scm" in kwargs and kwargs['scm'] != None:
        if kwargs['scm'] == "git":
            os.system("git init " + directoryPath)
            # todo: Create standard .gitignore
            # todo: set all current standard files as initial commit


def read_project_configuration():
    """Read the project configuration file if exists"""
    if os.path.isfile(MKBUILD_CONFIG_FILE):
        config_file = open(MKBUILD_CONFIG_FILE, "r")
        raw_buffer = config_file.read()
        config_file.close()

        buffer = raw_buffer.split("\n")
        for buf_line in buffer:
            if len(buf_line) > 0 and buf_line[0] != '#':
                key, value = buf_line.split("=")
                MKBUILD_CONFIG[key.strip()] = value.strip()

        printv("Project name:", MKBUILD_CONFIG['project'])


def search_command_and_run_it(values):
    if len(values) >= 1:
        command = glob.glob(MKBUILD_COMMANDS + "/" + values[0] + ".py")
        if len(command) == 0:
            raise Exception("Command " + values[0] + " not found")

        if len(values) >= 2:
            os.system(command[0] + " " + " ".join(str(s) for s in values[1:]))
        else:
            os.system(command[0])


def read_args(argv):
    try:
        args, values = getopt.getopt(argv, "?vp:m:i:", ["help", "version", "project=", "scm=" "init="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    project_name = None
    scm_type = None
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
        elif arg in ("-p", "--project"):
            project_name = value
        elif arg in ("-m", "--scm"):
            scm_type = value

        elif arg in ("-i", "--init"):
            if project_name == None:
                print("Missing --project argument", "\n", sys.stderr)
                sys.exit(ErrorType.kMISSING_ARG.value)

            return_value = init_project_on(value, project_name, scm=scm_type)
            if return_value is not None:
                sys.exit(return_value.value)

    search_command_and_run_it(values)


def main(args):
    """main function"""
    read_args(args)
    read_project_configuration()


# ### Main method
if __name__ == "__main__":
    WORKING_DIR = os.path.dirname(sys.argv[0])
    MKBUILD_COMMANDS = os.getenv("MKBUILD_COMMANDS", "/usr/share/mkbuild/commands/")
    APP_NAME = os.path.basename(sys.argv[0])
    main(sys.argv[1:])