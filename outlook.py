

import urllib2


# set authentification
auth = urllib2.HTTPBasicAuthHandler()
auth.add_password('correo.eluniversal.com', 'https://correo.eluniversal.com/exchange','wasuaje', '123456')


# don't use proxy
prox = urllib2.ProxyHandler({})


# installation
opener = urllib2.build_opener(prox, auth)
urllib2.install_opener(opener)


# start
url = urllib2.urlopen('https://correo.eluniversal.com/Exchange/')
print url.readlines()
