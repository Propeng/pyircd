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

#pyircd.py

from pyircd import server
import os

if __name__ == '__main__':
    #TODO: cross-platform config path
    confdir = os.path.expanduser("~/.pyircd")
    
    server = server.Server(confdir)
    server.listen_loop = True
    server.loop()
