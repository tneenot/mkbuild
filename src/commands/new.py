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
from core.core import *


# Specific command implementation
class NewCommand(FacilityCommand):
    def __init__(self):
        super().__init__("create a new project.")

    def read_command_args(self, args, values):
        git_init = False
        for arg, value in args:
            if arg in ("-g", "--git"):
                git_init = True

        if len(values) > 0:
            self.create_project_directory(values[0], git_init)

    def create_project_directory(self, directory, gitInitialization):
        if os.path.exists(directory):
            print("Directory projet exists yet: " + directory)
        else:
            os.mkdir(directory, 0o765)
            create_project_config_file(directory)

        if gitInitialization == True:
            if os.path.exists(directory + "/.git"):
                print("Git directory exists yet")
            else:
                os.system("git init " + directory)
                # todo: Create standard .gitignore
                # todo: set all current standard files as initial commit

    def command_usage_description(self, applicationName):
        print("\t-g|--git: run the git initialization")
        print("\t<project>: name of project.")

    def command_usage_resume(self, applicationName):
        print("\t", applicationName, "[-g|--git] <project>")

    def get_args_list(self):
        return "g", ["git"]


# Main
if __name__ == "__main__":
    new_command = NewCommand()
    new_command.read_args(sys.argv[1:])
