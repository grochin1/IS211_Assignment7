import random

class Player:
    def __init__(self, score=0):
        self.score = score

    def getData(self):
        return self.score


p1 = Player(0)
print (p1.getData())

p1.score = p1.score + 5

p1.getData()


class Dice:
    # def __init__(self):
    # self.score = score

    def roll(self):
        r = random.randrange(1, 7)
        return r


d1 = Dice()
print (d1.roll())

import random

random.seed(a=0)


class play:

    def show_instructions(self):
        print " Welcome to the game of Pig. To win, be the"
        print " player with the most points at the end of the"
        print "game. The game ends at the end of a round where"
        print "at least one player has 100 or more points"
        print
        print " On each turn, you may roll the die as many times"
        print " as you like to obtain more points. However, if"
        print " you a 1, your turn is over, and you do not"
        print " obtain any points that turn."
        print

    def take_turn(self, player):
        point = 0
        keep_rolling = 1
        print " its your turn player ", player
        raw_input("press enter to begin")
        while keep_rolling == 1:
            r = d1.roll()
            print " you got a", r
            if r == 1:
                point = 0
                keep_rolling = 0
            else:
                point += r
                print " your total is", point
                y = raw_input("do you want to continue? r=yes roll h= no / halt and you are player " + str(player))
                if y == "r":
                    keep_rolling = 1
                else:
                    keep_rolling = 0
        print "your turn is over"
        return point


play1 = play()

# play1.take_turn(1)
# play1.show_instructions()

def main():
    play1.show_instructions()
    p1 = Player(0)
    p2 = Player(0)
    while p1.score<25 and p2.score<25:
        print " Player points for p1 are: " +str(p1.score)
        print " Player points for p2 are: " +str(p2.score)
        r = play1.take_turn(1)
        p1.score += r
        print "Player points for p1 are: " +str(p1.score)
        print "Player points for p2 are: " +str(p2.score)
        r = play1.take_turn(2)
        p2.score += r
        print " The game is still on - lets keep rolling"
#         print " Player points for p1:" +str(p1)
#         print " Player points for p2:" +str(p2)
    if p1.score>p2.score:
        print " Player one is the winner"
    elif p2.score>p1.score:
        print "player two is the winner"
    else:
        print " Tie game"

def main():
    play1.show_instructions()
    p1 = Player(0)
    p2 = Player(0)
    while p1.score<25 and p2.score<25:
        print " Player points for p1 are: " +str(p1.score)
        print " Player points for p2 are: " +str(p2.score)
        r = play1.take_turn(1)
        p1.score += r
        print "Player points for p1 are: " +str(p1.score)
        print "Player points for p2 are: " +str(p2.score)
        r = play1.take_turn(2)
        p2.score += r
        print " The game is still on - lets keep rolling"
#         print " Player points for p1:" +str(p1)
#         print " Player points for p2:" +str(p2)
    if p1.score>p2.score:
        print " Player one is the winner"
    elif p2.score>p1.score:
        print "player two is the winner"
    else:
        print " Tie game"


main()
play1.take_turn(1)
play1.take_turn(2)
