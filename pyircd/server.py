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

#pyircd/server.py

import parseconf, checkconf, logger

class Server:
    def __init__(self, confdir):
        self.confdir = confdir
        self.logfile = confdir + "/pyircd.log"
        self.conffile = confdir + "/pyircd.conf"
        
        self.logger = logger.Logger(self.logfile)
        self.logger.info("Started logging")
        
        self.logger.info("Checking config...")
        confchecker = checkconf.ConfigChecker(self.logger, self.confdir, self.conffile)
        confchecker.prepare()
        
        #reinitialize logger so if config is newly created, it doesn't still point to devnull
        self.logger = logger.Logger(self.logfile)
        
        self.logger.info("Parsing config...")
        confparser = parseconf.ConfigParser(self.logger, self.conffile)
        self.conf = confparser.parse()
    
    def loop(self):
        pass