# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:39:02 2013

@author: hok1
"""

import pickle
import mutual_friends as mf

class FriendClusters:
    def __init__(self, selfuid=None, access_token=None, mfpickle_filename=None):
        if mfpickle_filename != None:
            ifile = open(mfpickle_filename, 'rb')
            self.mfwrapper = pickle.load(ifile)
        elif selfuid != None and access_token != None:
            self.mfwrapper = mf.MutualFriendsChecker(selfuid, access_token)
        else:
            self.mfwrapper = None
            
    def grow_friends_cluster(self, friend_uid, bottom_line=10, depth=2):
        frdcluster_set = set([])
        if depth == 0:
            return list(frdcluster_set)
        elif depth >= 1:
            mutfrd_list = self.mfwrapper.get_mutual_friends(friend_uid)
            if len(mutfrd_list) < bottom_line:
                return list(frdcluster_set)
            else:
                frdcluster_set.add(friend_uid)
            if depth > 1:
                for mutfrd_uid in mutfrd_list:
                    mutfrds_of_frd = self.grow_friends_cluster(mutfrd_uid['uid2'],
                                                               bottom_line=bottom_line,
                                                               depth=depth-1)
                    for uid1 in mutfrds_of_frd:
                        frdcluster_set.add(uid1)
        return list(frdcluster_set)
