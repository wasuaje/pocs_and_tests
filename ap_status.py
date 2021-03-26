# -*- coding: utf-8 -*-
import sys
import urllib2
from operator import itemgetter
from BeautifulSoup import BeautifulSoup

class Status (object):
    _url = None

    def __init__ (self, url):
        self._url = url

    def fetch (self):
        return urllib2.urlopen(self._url).read()

    def parse (self):
        html = self.fetch()
        soup = BeautifulSoup(html)
        status = {}
        status['server_info'] = [i.string.strip() for i in soup.findAll('dt')]
        status['requests'] = []
        requests = soup.find('table').findAll('tr')
        keys = [i.string for i in requests.pop(0)]
        for tr in requests:
            req = {}
            for n, td in enumerate(tr):
                req[keys[n]] = td.string
            status['requests'].append(req)
        return status

def main (argv):
    if len(argv) < 2:
        print "Usage %s "%argv[0]
        return 1

    status = Status(argv[1])
    data = status.parse()
    print "SERVER INFORMATION"
    print "=================="
    for v in data['server_info']:
        print v
    print data['server_info']

    print "REQUESTS BY VHOST"
    print "================="
    entries = [i['VHost'] for i in data['requests']]
    requests = sorted([(entries.count(i), i) for i in list(set(entries))], reverse=True)
    print "\n".join(["%d: %s"%(a,b) for a,b in requests])
    print data['requests']

if __name__ == "__main__":
    sys.exit(main(sys.argv))