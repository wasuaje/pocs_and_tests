
from __future__ import print_function

bbs = '01110011001000000110111001101111001000000010000001101001001000000111001101101110001000000110010100100000001000000110100000100000001000000110010100100000011100100010000000100000011100000110110100100000011011110010000001100011'

print("data binaria")
print(bbs)


#octets=[]

#normalmente como se divide en octetos requiere la lista inicilizada
#for i in range(0,len(bbs),8):
#	octets.append(bbs[i:i+8])

#good way con funcion map y lambda
#octets = map(lambda i: bbs[i:i+8],range(0,len(bbs),8))

#bestway
print ("la mejor manera de obtener octetos")
octets = [bbs[i:i+8] for i in range(0,len(bbs),8)]
#print type(octets)
print (octets)

chrs = [chr(int(octect,2)) for octect in octets]

#good
#chrs = filter(lambda c: c != ' ',chrs)

#better
print ("la mejore manera de obtener caracteres ascc the los octetos")
chrs = [c for c in chrs if c!= ' ']
print (chrs)


message = ''.join(chrs)
print (message)
print ("finalmente el mensaje descifrado")
message = ''.join(reversed(chrs))
print (message)

droids = [
  {'name': 'BB-8', 'fav_jedi': 'Rey'},
  {'name': 'R2-D2', 'fav_jedi': 'Luke Skywalker'},
  {'name': 'C-3PO', 'fav_jedi': 'Luke Skywalker'},
]

#old way
matches = []
for i in range(len(droids)):
  for j in range(i + 1, len(droids)):
  	matches.append((droids[i], droids[j]))

#oldway with nwumerate
matches = []
for i, a in enumerate(droids):
  for b in droids[i + 1:]:
  	matches.append((a, b))
#print matches

#new way with list comprehension
matches = [(a, b) for i, a in enumerate(droids) for b in droids[i + 1:]]
scores = ['Great' if a['fav_jedi'] == b['fav_jedi'] else 'Miserable' for a, b in matches]

print (matches)
print (scores)
print ("finally")
print(['{} -> {[name]} + {[name]} '.format( s,*m) for m, s in zip(matches, scores)])
print ( [ (m , s) for m, s in zip(matches, scores) ])

pilots = [
  {'name': 'Luke Skywalker', 'ship_id': 0},
  {'name': 'Darth Vader', 'ship_id': 1},
]
ships = [
  {'id': 0, 'model': 'T-65B X-wing'},
  {'id': 1, 'model': 'TIE Advanced x1'},
]



