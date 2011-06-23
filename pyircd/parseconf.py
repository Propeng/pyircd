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

#pyircd/parseconf.py

import sys

class ConfigParser:
    def __init__(self, logger, conffile):
        self.logger = logger
        self.file = conffile
    
    def parse(self):
        conf = { 'hostname' : None,
                 'port': None,
                 'netname': None,
                 'oper': {},
                }
        f = open(self.file, 'r')
        lines = f.read().splitlines()
        ln = 0
        for line in lines:
            ln += 1
            if line.startswith('#'):
                continue
            else:
                mainsp = line.partition('=')
                if mainsp[1] == '':
                    self.logger.error("Config error at line %d: missing value" % ln, True)
                    sys.exit(1)
                elif mainsp[0].endswith('+'):
                    name = mainsp[0][:-1]
                    subsp = mainsp[2].partition(':')
                    if subsp[1] == '':
                        self.logger.error("Config error at line %d: missing subvalue" % ln, True)
                    conf[name][subsp[0]] = subsp[2]
                else:
                    conf[mainsp[0]] = mainsp[2]
        
        return conf
