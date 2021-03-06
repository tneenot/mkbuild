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

# ## Metadata
__author__ = "Tioben Neenot"
__version__ = "0.1.00"
__email__ = "tioben.neenot@laposte.net"
__year__ = 2017

# Import
from enum import Enum
import time, os, sys, getopt
import glob

# ## Globals
MKBUILD_CONFIG_FILE = ".mkbuild"
MKBUILD_CONFIG = dict()
MKBUILD_COMMANDS = ""


# Enumerations
class ErrorType(Enum):
    kNO_ERROR = 0
    kNO_DIR = 1
    kMISSING_ARG = 2


class LogLevel(Enum):
    kDEFAULT = 0
    kFINE = 1
    kFINEST = 2
    kDEPTH = 3


class Global(object):
    LOG_VERBOSE_LEVEL = LogLevel.kDEFAULT
    MKBUILD_CONFIG_FILE = ".mkbuild"
    MKBUILD_CONFIG = dict()
    MKBUILD_COMMANDS = ""


class FacilityCommand(object):
    """Facility class for new command implementation"""

    def __init__(self, usage, command=os.path.basename(sys.argv[0].split('.')[0])):
        self.__usage_text = usage
        self.__app_name = command
        Global.MKBUILD_COMMANDS = os.getenv("MKBUILD_COMMANDS", "/usr/share/mkbuild/commands/")
        Global.MKBUILD_CONFIG["template.dir"] = os.getenv("MKBUILD_TEMPLATE", "/etc/mkbuild.d")
        read_project_configuration()

    def __usage_resume(self, withTab=False):
        tab_string = ""
        if withTab == True:
            tab_string = "\t"

        print(tab_string, self.__app_name + ":", self.__usage_text)

    def usage(self):
        self.__usage_resume()

        print("\nUsage:")
        print("\t", self.__app_name, "[-?|--help] [-v|--version] [--resume]")
        self.command_usage_resume(self.__app_name)

        print("\nParameters:")
        print("\t-?|--help: shows this help.")
        print("\t-v|--version: shows the current version.")
        print("\t--resume: shows only the sum up of the help.")
        self.command_usage_description(self.__app_name)

    def command_usage_resume(self, applicationName):
        """Override this method to define the description resume of the command implementation with specifics parameters"""
        pass

    def command_usage_description(self, applicationName):
        """Override this method to complete command description with the specific description of your command"""
        pass

    def __read_standard_args(self, argv):
        try:
            args, values = getopt.getopt(argv, "?v", ["help", "version", "resume"])
        except getopt.GetoptError:
            try:
                simple_arg, list_args = self.get_args_list()
                args, values = getopt.getopt(argv, simple_arg, list_args)
            except getopt.GetoptError:
                self.usage()
                sys.exit(2)

        for arg, value in args:
            if arg in ("-?", "--help"):
                self.usage()
                sys.exit()
            elif arg in ("-v", "--version"):
                print(self.__app_name, "version", __version__, ". Written by:", __author__ + ". ")
                print(self.__app_name, "is distributed under GPLv3 condition. Copyright (C)", __year__, __author__,
                      ".This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to "
                      "redistribute it under GPLv3 conditions.")
                sys.exit()
            elif arg in ("--resume"):
                self.__usage_resume(True)
                sys.exit()

        return args, values

    def read_args(self, argv):
        args, values = self.__read_standard_args(argv)
        self.read_command_args(args, values)

    def read_command_args(self, args, values):
        """Override this method for specific implementation command arguments reading and specific process running"""
        pass

    def get_args_list(self):
        """Override this method to return the specific arguments list conform to getops"""
        return "", [""]


# Functions
def printv(string="", *params, **kwargs):
    """Prints the value according to the verbose mode.
    kwargs contains the verbose mode according to: verbose=<LogLevel>.
    Eg: printv("A text", 2, verbose=LogLevel.kFINE
    """
    verbose = LogLevel.kDEFAULT

    if len(kwargs) >= 1:
        verbose = kwargs['verbose']

    if verbose.value <= Global.LOG_VERBOSE_LEVEL.value:
        print(string, *params)


def create_project_config_file(directory):
    """Create the project configuration file to the directory path"""
    if os.path.isfile(directory + "/" + Global.MKBUILD_CONFIG_FILE) is True:
        return

    config_file = open(directory + "/" + Global.MKBUILD_CONFIG_FILE, "w", encoding="utf-8")
    config_file.write("# Creation date: " + time.asctime() + "\n")
    config_file.write("project = " + directory + "\n")
    config_file.write("author = " + os.environ['USER'] + "\n")
    config_file.write("email = <your email>\n")
    config_file.close()


def read_project_configuration(directory=os.path.curdir):
    """Read the project configuration file if exists"""
    if os.path.isfile(directory + "/" + Global.MKBUILD_CONFIG_FILE):
        raw_buffer = read_file_content(directory + "/" + Global.MKBUILD_CONFIG_FILE)

        buffer = raw_buffer.split("\n")
        for buf_line in buffer:
            if len(buf_line) > 0 and buf_line[0] != '#':
                key, value = buf_line.split("=")
                Global.MKBUILD_CONFIG[key.strip()] = value.strip()


def read_file_content(file):
    config_file = open(file, "r")
    raw_buffer = config_file.read()
    config_file.close()
    return raw_buffer


def not_implemented_yet(arg=""):
    print(arg, "not implemented yet")


def parse_buffer(buffer):
    """Parse the given buffer with awaiting values."""
    if buffer.find("@PROJECT@") != -1:
        buffer = buffer.replace("@PROJECT@", Global.MKBUILD_CONFIG["project"])

    if buffer.find("@CREATIONDATE@") != -1:
        buffer = buffer.replace("@CREATIONDATE@", time.asctime())

    if buffer.find("@PROJECT.DIR@") != -1:
        buffer = buffer.replace("@PROJECT.DIR@", os.curdir)

    if buffer.find("@DEVELOPER@") != -1:
        buffer = buffer.replace("@DEVELOPER@", Global.MKBUILD_CONFIG['author'])

    if buffer.find("@EMAIL@") != -1:
        buffer = buffer.replace("@EMAIL@", Global.MKBUILD_CONFIG["email"])

    if buffer.find("@YEAR@") != -1:
        buffer = buffer.replace("@YEAR@", str(time.gmtime().tm_year))

    return buffer


def copy_file_and_parse(source, target):
    """Copy file from source to target and parse the target contents according to current configuration"""
    raw_buffer = read_file_content(source)
    final_buffer = parse_buffer(raw_buffer)

    write_file = open(target, "w")
    write_file.write(final_buffer)
    write_file.close()
