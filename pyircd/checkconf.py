# pyircd: Simple Python IRC server
# Copyright (C) 2011 Ahmed El-Mahdawy
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#pyircd/checkconf.py

import os

class ConfigChecker:
    def __init__(self, logger, dir, file):
        self.logger = logger
        self.dir = dir
        self.file = file
        
    def writeconf(self):
        f = open(self.file, 'w')
        f.write("#This is an automatically generated pyircd.conf file")
        f.write("port=6667\n")
        f.write("netname=Example IRC Network\n")
        f.write("oper+=oper1:pass1\n")
        f.write("oper+=oper2:pass2\n")
        f.close()
    
    def prepare(self):
        if not os.path.exists(self.dir):
            self.logger.info("Creating pyircd directory...")
            os.mkdir(self.dir)           
        
        if not os.path.isfile(self.file):
            self.logger.info("Writing default config...")
            self.writeconf()