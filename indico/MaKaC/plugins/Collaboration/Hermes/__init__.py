# -*- coding: utf-8 -*-
##
## $Id: __init__.py,v 1.4 2009/03/06 09:49:52 dmartinc Exp $
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

from MaKaC.plugins import getModules, initModule

pluginType = "Collaboration"
pluginName = "Hermes"
pluginDescription = ""
ignore = True

modules = {}
topModule = None

############

from MaKaC.plugins.Collaboration.Hermes.Site import Components
from MaKaC.plugins.Collaboration.Hermes.Service import Endpoint

# interface

CreateComponent = Components.WCreate
ShowComponent = Components.WShow
ServiceEndpoint = Endpoint

