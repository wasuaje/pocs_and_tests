#
# RFC822 Email Address Regex
# --------------------------
#
# Originally written by Cal Henderson
# c.f. http://iamcal.com/publish/articles/php/parsing_email/
#
# Translated to Python by Tim Fletcher, with changes suggested by Dan Kubb.
#
# Licensed under a Creative Commons Attribution-ShareAlike 2.5 License
# http://creativecommons.org/licenses/by-sa/2.5/
#
import re
import MySQLdb

qtext = '[^\\x0d\\x22\\x5c\\x80-\\xff]'
dtext = '[^\\x0d\\x5b-\\x5d\\x80-\\xff]'
atom = '[^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+'
quoted_pair = '\\x5c[\\x00-\\x7f]'
domain_literal = "\\x5b(?:%s|%s)*\\x5d" % (dtext, quoted_pair)
quoted_string = "\\x22(?:%s|%s)*\\x22" % (qtext, quoted_pair)
domain_ref = atom
sub_domain = "(?:%s|%s)" % (domain_ref, domain_literal)
word = "(?:%s|%s)" % (atom, quoted_string)
domain = "%s(?:\\x2e%s)*" % (sub_domain, sub_domain)
local_part = "%s(?:\\x2e%s)*" % (word, word)
addr_spec = "%s\\x40%s" % (local_part, domain)


email_address = re.compile('\A%s\Z' % addr_spec)

FILE="/home/wasuaje/Escritorio/CampaignID124-Failed-20110222113021.TXT"
f = open(FILE, 'r')
i=0
db = MySQLdb.connect(host="10.3.0.130", user="root", passwd="root", db="openemm")
cursor = db.cursor()
recs=cursor.execute("SELECT * FROM admin_tbl")
print recs

for row in cursor:
   print row

#for x in range(recs):
#   print cursor.fetchone()

#if __name__ == '__main__':
#  addresses = f.readlines()
#  #print addresses
#  for address in addresses:
#	#if email_address.match(address) != 'None':
#	#print address
#	address=address.replace('\r\n','')
#	#print address
#	if email_address.match(address):
#		#print "%s : %s" % (repr(address), email_address.match(address))
#		#i+=1
#		pass
#	else:
#		print address
#		i+=1
#print i
#print