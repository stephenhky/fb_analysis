# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 17:48:13 2013

@author: hok1
"""

'''
Codes adapted from

Toby Segaran, "Programming Collective Intelligence: Building Smart Web 2.0 Applications"
'''


import urllib, md5, webbrowser
from xml.dom.minidom import parseString

apikey='80725761636'
secret='9ec968fd747a6ef6de4588a9000b6036'
FacebookSecureURL='https://api.facebook.com/restserver.php'

def getsinglevalue(node, tag):
    nl = node.getElementsByTagName(tag)
    if len(nl) > 0:
        tagNode = nl[0]
        if tagNode.hasChildNodes():
            return tagNode.firstChild.nodeValue
    return ''

class fbsession:        
    def sendrequest(self, args):
        args['api_key'] = apikey
        args['sig'] = self.makehash(args)
        post_data  = urllib.urlencode(args)
        url = FacebookSecureURL + '?' + post_data
        data = urllib.urlopen(url).read()
        return parseString(data)
        
    def makehash(self, args):
        hasher = md5.new(''.join([x+'='+args[x] for x in sorted(args.keys())]))
        if self.session_secret:
            hasher.update(self.session_secret)
        else:
            hasher.update(secret)
        return hasher.hexdigest()

    def getlogin(self):
        return "http://api.facebook.com/login.php?api_key="+apikey+\
               "&auth_token="+self.token
        
    def createtoken(self):
        res = self.sendrequest({'method': 'facebook.auth.createToken'})
        self.token = getsinglevalue(res, 'token')
        
    def getsession(self):
        doc = self.sendrequest({'method': 'facebook.auth.getSession',
                                'auth_token': self.token})
        self.session_key = getsinglevalue(doc, 'session_key')
        self.session_secret = getsinglevalue(doc, 'secret')
        
    def __init__(self):
        self.session_secret = None
        self.session_key = None
        self.createtoken()
        webbrowser.open(self.getlogin())
        print 'Press enter after logging on:'
        raw_input()
        self.getsession()
