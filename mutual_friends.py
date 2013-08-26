# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:23:34 2013

@author: hok1
"""

import fbtools
import json
import FriendsListHolder as frdholder
from string import Template
    
class MutualFriendsChecker(frdholder.FriendListHolder):
    def __init__(self, selfuid, access_token):
        frdholder.FriendListHolder.__init__(selfuid, access_token)
        self.mutualfrd_pairs = self.get_mutual_friends(self.selfuid)
        
    def get_mutual_friends(self, uid):
        fql_templ = ' SELECT uid1, uid2 FROM friend '+\
                    ' WHERE uid1 IN '+\
                    '(SELECT uid2 FROM friend WHERE uid1= $personuid)' +\
                    'AND uid2 IN '+\
                    '(SELECT uid2 FROM friend WHERE uid1= $personuid)'
        fql_query = Template(fql_templ).substitute(personuid=uid)
        jresults = fbtools.FQLquery(fql_query, self.access_token)
        return json.loads(jresults)['data']
