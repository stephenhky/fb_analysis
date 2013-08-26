# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:35:46 2013

@author: hok1
"""

import fbtools

class FriendListHolder:
    def __init__(self, selfuid, access_token):
        self.selfuid = selfuid
        self.access_token = access_token
        self.friend_uids = fbtools.getFriendUIDList(selfuid, access_token)
    
    def check_iffriend(self, uid):
        return (uid in self.friend_uids)
