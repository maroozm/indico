# -*- coding: utf-8 -*-
##
## $Id: httpTimeout.py,v 1.1 2009/04/14 11:09:25 dmartinc Exp $
##
## This file is part of CDS Indico.
## Copyright (C) 2002, 2003, 2004, 2005, 2006, 2007 CERN.
##
## CDS Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CDS Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDS Indico; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

""" The HTTPConnectionWithTimeout and HTTPHandlerWithTimeout classes are derived
    from Python 2.5 's httplib.HTTPConnection and urllib2.HTTPHandler respectively.
    They should be used when we want the Indico server to connect to another server
    by HTTP and we want to set up a timeout in case the remote server doesn't answer.
    Python 2.6 has a "timeout" argument in urllib2.urlopen but not in Python 2.5.
    For use of these classes, see the example in the "if __name__ == '__main__':" section.
"""

import httplib, urllib2, socket

class HTTPConnectionWithTimeout(httplib.HTTPConnection):
    """ A custom HTTPConnection class that allows a timeout to be specified.
        This is necessary because a timeout cannot be specified in Python 2.5.
        When we start using Python2.6, this class will be no longer necessary.
        See example in the "if __name__ == '__main__':" section to understand how to use.
    """

    def __init__(self, host, port=None, strict=None, timeout=None):
        """ Constructor
            timeout is specified in seconds with a float number.
        """
        httplib.HTTPConnection.__init__(self, host, port, strict)
        self._timeout = timeout

    def connect(self):
        """ Overrides HTTPConnection.connect
        """

        msg = "getaddrinfo returns an empty list"
        for res in socket.getaddrinfo(self.host, self.port, 0, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                self.sock = socket.socket(af, socktype, proto)
                if self._timeout:
                    self.sock.settimeout(self._timeout)
                self.sock.connect(sa)
            except socket.error, msg:
                if self.sock:
                    self.sock.close()
                self.sock = None
                continue
            break
        if not self.sock:
            raise socket.error, msg

class HTTPHandlerWithTimeout(urllib2.HTTPHandler):
    """ A custom HTTPHandler class that allows a timeout to be specified.
        This is necessary because a timeout cannot be specified in Python 2.5.
        When we start using Python2.6, this class will be no longer necessary.
        See example in the "if __name__ == '__main__':" section to understand how to use.
    """

    def __init__(self, timeout=None):
        """ Constructor
            timeout is specified in seconds with a float number.
        """
        
        urllib2.HTTPHandler.__init__(self)
        self._timeout = timeout

    def http_open(self, req):
        """ Overrides HTTPHandler.http_open
        """

        def makeConnection(host, port=None, strict=None):
            return HTTPConnectionWithTimeout(host, port, strict, timeout = self._timeout)

        return self.do_open(makeConnection, req)
    
class HTTPWithTimeout(httplib.HTTP):
    """ A custom HTTP class that allows a timeout to be specified.
        This is necessary because a timeout cannot be specified in Python 2.5.
        When we start using Python2.6, this class will be no longer necessary.
    """
    _connection_class = HTTPConnectionWithTimeout

    def __init__(self, host='', port=None, strict=None, timeout=None):
        """ Changed from of httplib.HTTP.__init__, added timeout argument to
            self._setup(self._connection_class(host, port, strict, timeout))
        """ 
        if port == 0:
            port = None
        self._setup(self._connection_class(host, port, strict, timeout))
    
def urlOpenWithTimeout(request, timeout):
    opener = urllib2.build_opener(HTTPHandlerWithTimeout(timeout))
    return opener.open(request)
        

# test request with timeout
if __name__ == '__main__':
    request = urllib2.Request("http://www.google.com")
    try:
        file = urlOpenWithTimeout(request,5)
        for l in file.readlines():
            print l
    except Exception, e:
        print e
