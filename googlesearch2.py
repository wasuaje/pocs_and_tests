
import sys
sys.path.append('xgoogle')

from xgoogle.search import GoogleSearch, SearchError
try:
  gs = GoogleSearch("wuelfhis asuaje")
  gs.results_per_page = 100
  results = []
  while True:
    tmp = gs.get_results()
    if not tmp: # no more results were found
      print "no more resutl"
      break
    results.extend(tmp)
    for rs in results:
      print "busqueda", rs
  # ... do something with all the results ...
except SearchError, e:
  print "Search failed: %s" % e
