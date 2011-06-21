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

#pyircd/connection.py

import logger

class Connection:
    def __init__(self, logger, server, conn, addr):
        self.logger = logger
        self.server = server
        self.socket = conn
        self.addr = addr[0]
        self.id = addr[1]
        
        self.logger.info("Connection from %s[%d]" % self.addr, self.id)
    
    def listen(self):
        pass
