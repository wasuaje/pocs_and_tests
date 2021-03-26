#!/usr/bin/env python

# Created by Simon Wex (simon@zeepmobile.com) on 2008-07-12
# Copyright (c) 2008. All rights reserved.
# Released under MIT License

import base64
import hmac
import sha
import time
import urllib2, urllib
from urllib2 import URLError, HTTPError
SECRET_ACCESS_KEY = 'da39a3ee5e6b4b0d3255bfef95601890afd80709'

kv = {'API_KEY': 'a8042acf-db28-40b3-9bc1-faf74977a1f7',
'Body': 'The brown fox jumped over the lazy dog.',
'Version': '2008-07-18',
'SignatureVersion': '1',
'Timestamp': time.strftime('%a, %d %b %Y %H:%M:%S GMT',time.gmtime())
}

sig = hmac.new(SECRET_ACCESS_KEY, digestmod=sha)

items = kv.items()
# Sort the keys
items.sort()
for key, value in items:
  sig.update(key)
  sig.update(value)
  
authentication="Zeep " +kv["API_KEY"] + ":"+base64.encodestring(sig.digest()).strip()
a=len('user_id7217bodymensaje de prueba')
parameters = urllib.urlencode({'user_id':7217,'body':'mensaje de prueba'})
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {
  "User-Agent":user_agent, 
  "Authorization:":authentication,
  "Date:":kv["Timestamp"],
  "Content-Type:":"application/x-www-form-urlencoded"
}
request = urllib2.Request('https://api.zeepmobile.com/messaging/2008-07-14/send_message', parameters,  header)
request.add_header("Authorization:", authentication)
#print header  

#print dir(request)
#print request.headers
try:
	urllib2.urlopen(request)
except URLError, e:
	print dir(e)
	print str(e.code)+' - '+e.msg
	print e.read()

#the_page = response.read()
#print the_page
