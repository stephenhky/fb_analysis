# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:37:00 2013

@author: hok1
"""

'''

This method does nto really work....

'''

import fbtools
import FriendsListHolder as frdholder

class DegreeFriendCluster(frdholder.FriendListHolder):
    def check_ndegree_friend(self, uid, degree):
        if degree == 1:
            return self.check_iffriend(uid)
        else:
            friends = fbtools.getFriendNameList(uid, self.access_token)
            for friend_uid in friends:
                isdegreefriend = self.check_ndegree_friend(friend_uid,
                                                           degree-1)
                if isdegreefriend:
                    return True
            return False
            
    def get_ndegree_frienduids(self, uid, degree):
        frienduid_list = []
        for friend_uid in self.friend_uids:
            if self.check_ndegree_friend(friend_uid, degree):
                frienduid_list.append(friend_uid)
        return frienduid_list
