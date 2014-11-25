import sys, math
from collections import defaultdict

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[3], 'w')
    n = int(sys.argv[2])

    rounds = range(int(math.ceil(math.log(n, 2))))
    print "rounds",rounds

    cards = {}
    for player in range(n):
        cards[player] = defaultdict(str)
    
    for line in fin:
        es = line.split(',')
        for round in rounds:
            round_text = es[3+round*5:3+round*5+5]
            try:
                player = int(round_text[2])
                clue_round = round_text[3]
                clue = round_text[4]
                cards[player][clue_round] += ','+clue
            except:
                print round_text
    fin.close()

    for player in cards:
        print player
        for round in cards[player]:
            print '\t',round, cards[player][round]
        print '\n'
            
