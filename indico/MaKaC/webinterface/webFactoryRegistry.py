# -*- coding: utf-8 -*-
##
## $Id: webFactoryRegistry.py,v 1.8 2008/04/24 16:58:53 jose Exp $
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

from BTrees import OOBTree
import MaKaC.webinterface.simple_event as simple_event
import MaKaC.webinterface.meeting as meeting
from MaKaC.common import DBMgr


class WebFactoryRegistry:
    """
    """
    
    def __init__( self ):
        self._initFactoryRegistry()
        self._confRegistry = None

    def _initFactoryRegistry( self ):
        self._factoryRegistry = {}
        self._factoryRegistry[ simple_event.WebFactory.getId() ] = simple_event.WebFactory
        self._factoryRegistry[ meeting.WebFactory.getId() ] = meeting.WebFactory

    def _getConfRegistry( self ):
        if not self._confRegistry:
            db_root = DBMgr.getInstance().getDBConnection().root()
            if db_root.has_key( "webfactoryregistry" ):
                self._confRegistry = db_root["webfactoryregistry"]
            else:
                self._confRegistry = OOBTree.OOBTree()
                db_root["webfactoryregistry"] = self._confRegistry
        return self._confRegistry
    
    def _getModuleFactory( self, name ):
        comp = __import__( name )
        for compName in name.split(".")[1:]:
            comp = getattr( comp, compName )
        return getattr( comp, "WebFactory" )
        
    def registerFactory( self, conference, factory ):
        """Associates a given conference with a certain webfactory
        """
        self._getConfRegistry()[ conference.getId() ] = factory

    def getFactory( self, conference ):
        """Gives back the webfactory associated with a given conference or None
            if no association exists
        """
        try:
            if self._getConfRegistry().has_key( conference.getId() ):
                return self._getConfRegistry()[ conference.getId() ]
        except:
            pass    
        return None

    def getFactoryById( self, id):
        """Gives back the web factory class corresponding to the specified id
        """
        id = id.strip().lower()
        return self._factoryRegistry.get( id, None )
        
    def getFactoryList( self ):
        """Returns a list containing all the factories in the registry
        """
        return self._factoryRegistry.values()
