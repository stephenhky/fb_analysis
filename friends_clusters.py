# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:41:13 2013

@author: hok1
"""

import mutual_friends as mf
import resistancedist as resist
import pickle

frdpairdicttotuple = lambda item: (item[u'uid1'], item[u'uid2'])

class FriendResistanceDistancesWrapper:
    def __init__(self, selfuid=None, access_token=None, pickle_prefix=None):
        if selfuid != None and access_token != None:
            self.selfuid = selfuid
            self.access_token = access_token
            
            self.mfwrapper = mf.MutualFriendsChecker(selfuid, access_token)
            self.friends = self.mfwrapper.friend_uids
            self.mutfrd_pairs_dict = self.mfwrapper.get_all_mutual_friends_pairs()
            self.getResistanceMatrix()
        elif pickle_prefix != None:
            self.friends = pickle.load(open(pickle_prefix+'_friends.fb', 'rb'))
            self.mutfrd_pairs_dict = pickle.load(open(pickle_prefix+'_mutfrd.fb',
                                                      'rb'))
            self.getResistanceMatrix()
            
    def getResistanceMatrix(self):
        pairs = []
        for mflist in self.mutfrd_pairs_dict.values():
            pairs += map(frdpairdicttotuple, mflist)
        self.resistdist = resist.GraphResistanceDistance(nodes=self.friends,
                                                         edges=pairs)
    
    def getResistance(self, uid1, uid2):
        return self.resistdist.getResistance(uid1, uid2)
        
    def pickle_data(self, pickle_prefix):
        pickle.dump(self.friends, open(pickle_prefix+'_friends.fb', 'wb'))
        pickle.dump(self.friends, open(pickle_prefix+'_mutfrd.fb', 'wb'))
