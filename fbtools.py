# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:22:22 2013

@author: hok1
"""

import urllib2, urllib
import json

fql_query_prefix = 'https://graph.facebook.com/fql?'

def FQLquery(fql_query, access_token):
    if access_token == '':
        quoted_query = urllib.urlencode({'q': fql_query})
    else:
        quoted_query = urllib.urlencode({'q': fql_query,
                                         'access_token': access_token})
    url = fql_query_prefix + quoted_query
    return urllib2.urlopen(url).read()

def getName(uid, access_token):
    query = 'select name from user where uid='+str(uid)
    jfriend_data = FQLquery(query, access_token)
    friend_data = json.loads(jfriend_data)
    return friend_data['data'][0]['name']

def getFriendList(uid, access_token):
    fql_query = 'select uid2 from friend where uid1='+str(uid)
    jfriendsuid = FQLquery(fql_query, access_token)
    friendsuid = json.loads(jfriendsuid)['data']
    
    friends = []
    for frienduid in friendsuid:
        uid = frienduid['uid2']
        #friends.append({'uid': uid, 'name': getName(uid, access_token)})
        friends.append({'uid': uid})
        
    return friends
