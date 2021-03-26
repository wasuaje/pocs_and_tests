import random
 
num_cards = 6
games_to_play = 100000
 
class Game(object):
    def __init__(self):
        self.tosses = 0
        self.cards = []
 
    def pickCard(self):
        self.tosses += 1
        newcard = random.randint(1, num_cards)
        if not newcard in self.cards:
            self.cards.append(newcard)
 
    def run(self):
        while len(self.cards) < num_cards:
            self.pickCard()
        return self.tosses
 
if __name__ == '__main__':
    tosses = []
    for i in range(games_to_play):
        g = Game()
        tosses.append(g.run())
 
    print 'Cajas necesarias: %.2f' % (float(sum(tosses)) / len(tosses))
