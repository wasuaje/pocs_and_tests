# -*- coding: utf-8 -*-
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
import sys
import dns.resolver
import os

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

def valid( email_address ):
    # check email parts
    try:
        username, domain = email_address.rsplit('@', 1)
    except ValueError:
        return False
    # check username: allow alphanumeric characters and the dot
    if not username.replace( '.', '' ).isalnum():
        return False
    # check domain
    try:
        dns_response = dns.resolver.query( domain, 'MX')
    except dns.resolver.NoAnswer:
        # this host doesn't have MX records
        return False
    except dns.resolver.NXDOMAIN:
        # no such hostname
        return False
    except dns.exception.Timeout:
        #resposne timeout
        return False
    return True



def write_file(newLine):        
        file = open(outfile, "a")
        file.write(newLine)
        file.close()


#print len(sys.argv)
#print sys.argv[2]
if len(sys.argv) != 3:
   print "Necesita 2 argumentos: 1 archivo a analizar y 1 archivo de salida"
   sys.exit()
else:
    infile=sys.argv[1]
    outfile=sys.argv[2]
    erased = os.remove(outfile)
    
FILE='cambios_canales.csv'
f = open(FILE, 'r')
i=0
addresses = f.readlines()  

for address in addresses:	
    address=address.replace('\r\n','')
    #if email_address.match(address):
    if valid(address):
	pass
    else:
	print address
        write_file("'"+address+"';")
	i+=1

print i
