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

#pyircd/logger.py

import os, time

class Logger:
    def __init__(self, logfile):
        try:
            self.log = open(logfile, 'a')
        except IOError:
            self.log = open(os.devnull, 'w')
    
    def close(self):
        self.log.close()
    
    def timestr(self):
        return time.strftime('%c')
    
    def info(self, msg):
        logstr = "[%s] I: %s" % (self.timestr(), msg)
        print logstr
        self.log.write(logstr + "\n")
    
    def warning(self, msg):
        logstr = "[%s] W: %s" % (self.timestr(), msg)
        print logstr
        self.log.write(logstr + "\n")
    
    def error(self, msg, fatal=False):
        fatal = ""
        if fatal:
            fatal = "[Fatal] "
        
        logstr = "[%s] E: %s %s" % (fatal, self.timestr(), msg)
        print "--- PYIRCD ERROR ---"
        print logstr
        print "--- PYIRCD ERROR ---"
        self.log.write(logstr + "\n")