## check-gmail.py -- A command line util to check GMail -*- Python -*-

# ======================================================================
# Copyright (C) 2006 Baishampayan Ghose <b.ghose@ubuntu.com>
# Time-stamp: Mon Jul 31, 2006 20:45+0530
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
# ======================================================================

import urllib,urllib2             # For BasicHTTPAuthentication
from textwrap import wrap # For pretty printing assistance
import feedparser         # For parsing the feed

username = 'wasuaje'
password = 'www4214'
_URL = "https://mail.google.com/gmail/feed/atom"

def auth():
    '''The method to do HTTPBasicAuthentication'''
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # this creates a password manager
    passman.add_password(None, _URL, username, password)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    #opener = urllib.FancyURLopener()
    urllib2.install_opener(opener)
    f = urllib2.urlopen(_URL)
    #f = opener.open(_URL)
    feed = pagehandle.read()
    return feed

def fill(text, width):
    '''A custom method to assist in pretty printing'''
    if len(text) < width:
        return text + ' '*(width-len(text))
    else:
        return text

def readmail(feed):
    '''Parse the Atom feed and print a summary'''
    atom = feedparser.parse(feed)
    print ""
    print atom.feed.title
    print "You have %s new mails" % len(atom.entries)
    # Mostly pretty printing magic
    print "+"+("-"*84)+"+"
    print "| Sl.|"+" Subject"+' '*48+"|"+" Author"+' '*15+"|"
    print "+"+("-"*84)+"+"
    for i in xrange(len(atom.entries)):
        print "| %s| %s| %s|" % (
            fill(str(i), 3),
            fill(wrap(atom.entries[i].title, 50)[0]+"[...]", 55),
            fill(wrap(atom.entries[i].author, 15)[0]+"[...]", 21))
    print "+"+("-"*84)+"+"

if __name__ == "__main__":
    f = auth()  # Do auth and then get the feed
    readmail(f) # Let the feed be chewed by feedparser