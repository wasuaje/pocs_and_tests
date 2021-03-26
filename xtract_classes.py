import re

MYFILE = "models.txt"

hdl = open(MYFILE)
data={}

for ln in hdl.readlines():
	matchCls = re.match( r'class (.*)\(.*', ln, re.M|re.I)
	matchFld = re.match( r'(.*) \= models\.(.*)\(.*\)', ln, re.M|re.I)
	matchMth = re.match( r'\s+def\s+(.*)\(', ln, re.M|re.I)

	if matchCls:
		#print matchCls.group(1)
		cls = matchCls.group(1)
		data[cls]={"fields":[],"methods":[]}
	if matchFld:
		#print matchFld.group(1).replace(" ","")
		fld = matchFld.group(1).replace(" ","")+" (%s)" %  matchFld.group(2)
		data[cls]["fields"].append(fld)
	if matchMth:
		#print matchMth.group(1)
		mth = matchMth.group(1)
		data[cls]["methods"].append(mth)

#print data
for cl in data.keys():
	print "################"
	print "Model: %s" % cl
	print "Fields:"
	for fl in data[cl]["fields"]:
		print "\t %s" % fl

	print "Methods:"
	for mt in data[cl]["methods"]:
		print "\t %s" % mt

# print "\nTotal Models:", $cls , "\n";
# print "\nTotal Fields:", $fld , "\n";
# print "\nTotal Methods:", $mth , "\n";

# #print $data{"Auction"}{"methods"};



