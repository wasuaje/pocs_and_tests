#!/usr/bin/env python
 
class Atom (object):
 
  "A class to represent a single atom"
  def __init__(self, symbol, mass, position):
    self.symbol = symbol
    self.mass = mass
    self.position = position
 
  def symbol(self):
    return self.symbol
 
  def mass(self):
    return self.mass
 
  def position(self):
    return self.position
 
oAtom = Atom('O', 15.9994, [0.0, 0.0, 0.0])
hAtom1 = Atom('H', 1.0079, [0.0, 1.0, 0.0])
hAtom2 = Atom('H', 1.0079, [1.0, 0.0, 0.0])
 
print 'The mas of the second H atom is', hAtom2.position
