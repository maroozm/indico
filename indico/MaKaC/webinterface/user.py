from MaKaC import user
from MaKaC.services.implementation.base import ParameterManager
from MaKaC.services.interface.rpc.common import ServiceError


class UserModificationBase ( object ):
    """ Base class to retrieve an Avatar object from a 'user' parameter.
        It will store the Avatar object in self._targetUser
    """
    
    def _checkParams( self ):
        if 'user' in self._params:
            ph = user.PrincipalHolder()
            self._targetUser = ph.getById(self._params['user'])
        else:
            self._targetUser = None

## TODO: this class is never used....
class UserEditBase ( object ):
    
    def _checkParams(self):
        if 'userData' in self._params:
            pm = ParameterManager(self._params)
            self._userData = pm.extract("userData", pType=dict, allowEmpty = True)
        else:
            raise ServiceError("ERR-E6", '"userData" parameter missing')



class UserListModificationBase ( object):
    """ Base class to retrieve a list of users from a 'userList' parameter.
        The userList parameter will contain dictionaries with the following keys:
        id, title, title, familyName, firstName, affiliation, email, address, telephone, fax, submission
        
        The id can be:
        -a number, in this case it represents an Avatar id (a user in the DB)
        -a string beginning by 'newUser', ex: 'newUser0'. In that case it represents a user not in the DB, whose data was input
        -a string beginning by 'edited', ex: 'edited0'. In that case it represents an Avatar (a user in the DB),
         but whose data was changed.
         
        The class will store the users in the following 3 attributes:
        self._avatars = a list of Avatar objects
        self._newUsers = a list of dictionaries as the ones described before
        self._editedAvatars = a list of tuples (Avatar, dictionary)
    """
    
    @staticmethod
    def retrieveUsers(params, fieldName="userList"):
        pm = ParameterManager(params)
        userList = pm.extract(fieldName, pType=list, allowEmpty = True)
        avatars = []
        newUsers = []
        editedAvatars = []
        ph = user.PrincipalHolder()
    
        for userDict in userList:
            id = userDict['id']
            if id.startswith('newUser'):
                newUsers.append(userDict)
            elif id.startswith('edited'):
                editedAvatars.append((ph.getById(id[6:]), userDict))
            else:
                avatars.append(ph.getById(id))

        return avatars, newUsers, editedAvatars

    def _checkParams( self, params = None, fieldName = "userList" ):
        if params:
            self._params = params
        if fieldName in self._params:
            self._avatars, self._newUsers, self._editedAvatars = UserListModificationBase.retrieveUsers(self._params, fieldName)
        else:
            raise ServiceError("ERR-E5", '"userList" parameter missing')
    
