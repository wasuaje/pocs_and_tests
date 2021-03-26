#!/usr/bin/python

foo=range(1,1001)
foo= "".join(str(foo)).replace("[","").replace("]","").replace(",","\n")
print foo

