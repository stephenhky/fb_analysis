# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:22:22 2013

@author: hok1
"""

import urllib2, urllib

fql_query_prefix = 'https://graph.facebook.com/fql?'

def FQLquery(fql_query, access_token):
    if access_token == '':
        quoted_query = urllib.urlencode({'q': fql_query})
    else:
        quoted_query = urllib.urlencode({'q': fql_query,
                                         'access_token': access_token})
    url = fql_query_prefix + quoted_query
    return urllib2.urlopen(url).read()
    
