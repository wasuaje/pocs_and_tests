import sys
sys.path.append('xgoogle')

from xgoogle.search import GoogleSearch, SearchError
try:
  gs = GoogleSearch("@hotmail.com")
  gs.results_per_page = 150
  results = gs.get_results()
  for res in results:
    print res.title.encode("utf8")
  #  print res.desc.encode("utf8")
   # print res.url.encode("utf8")
   # print
except SearchError, e:
  print "Search failed: %s" % e
