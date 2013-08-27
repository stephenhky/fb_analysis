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
        frdholder.FriendListHolder.__init__(self, selfuid, access_token)
        self.mutualfrd_pairs = self.get_mutual_friends()
        
    def get_mutual_friends_old(self, uid):
        fql_templ = ' SELECT uid1, uid2 FROM friend '+\
                    ' WHERE uid1 IN '+\
                    '(SELECT uid2 FROM friend WHERE uid1= $personuid)' +\
                    'AND uid2 IN '+\
                    '(SELECT uid2 FROM friend WHERE uid1= $personuid)'
        fql_query = Template(fql_templ).substitute(personuid=uid)
        jresults = fbtools.FQLquery(fql_query, self.access_token)
        return json.loads(jresults)['data']
        
    def get_mutual_friends(self):
        fql_templ = 'select uid1, uid2 from friend '+\
                    'where uid1=$uid1'+\
                    ' and uid2 in (select uid2 from friend where uid1=$selfuid)'
        mutualfrd_pairs = []
        for uid in self.friend_uids:
            print 'Finding you mutual friends with '+uid
            fql_query = Template(fql_templ).substitute(uid1=uid,
                                                       selfuid=self.selfuid)
            jresults = fbtools.FQLquery(fql_query, self.access_token)
            for json_item in json.loads(jresults)['data']:
                mutualfrd_pairs.append(json_item)
        return mutualfrd_pairs
    
    def count_mutual_friends(self):
        friend_mfcount_dict = {}
        for pair in self.mutualfrd_pairs:
            friend_uid = pair['uid1']
            if friend_mfcount_dict.has_key(friend_uid):
                friend_mfcount_dict[friend_uid] += 1
            else:
                friend_mfcount_dict[friend_uid] = 1
        friend_mfcounts = []
        for uid in friend_mfcount_dict.keys():
            friend_mfcounts.append({'uid': uid,
                                    'mutualfriends_count': friend_mfcount_dict[uid]})
        return friend_mfcounts
