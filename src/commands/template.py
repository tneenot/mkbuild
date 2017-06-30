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
import glob

__author__ = "Tioben Neenot"
__version__ = "0.1.00"
__email__ = "tioben.neenot@laposte.net"
__year__ = 2017

# Import
from core.core import *


# Template command implementation
class TemplateCommand(FacilityCommand):
    def __init__(self):
        super().__init__("Create a new file from a template type.")

    def command_usage_description(self, applicationName):
        print("\t-f|--from <template>: give the template name source.")
        print("\t-t|--to <target>: target name of the new file.")
        print("\t-l|--list: list all available template files.")

    def read_command_args(self, args, values):
        template_file_from = None
        template_file_to = None

        for arg, value in args:
            if arg in ("-l", "--list"):
                self.__show_template(self.__get_template_list())
            elif arg in ("-t", "--to"):
                template_file_to = value
            elif arg in ("-f", "--from"):
                template_file_from = Global.MKBUILD_CONFIG["template.dir"] + "/" + value

        if template_file_to != None and template_file_from != None:
            if os.path.exists(template_file_to) == True:
                raise FileExistsError(template_file_to)

            copy_file_and_parse(template_file_from, template_file_to)

    def command_usage_resume(self, applicationName):
        print("\t", applicationName, "[-l|--list] [-f|--from <template> -t|--to <target>]")

    def get_args_list(self):
        return "lf:t:", ["list", "from=", "to="]

    def __get_template_list(self):
        return glob.glob(Global.MKBUILD_CONFIG["template.dir"] + "/*")

    def __show_template(self, files):
        [print("\t", (counter + 1), "-", os.path.basename(files[counter])) for counter in range(0, len(files))]


# Main
if __name__ == "__main__":
    template_command = TemplateCommand()
    template_command.read_args(sys.argv[1:])
