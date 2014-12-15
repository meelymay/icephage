import sys, math, string
from collections import defaultdict

if __name__ == '__main__':
    fin = open(sys.argv[1], 'r')
    fout = open(sys.argv[3], 'w')
    n = int(sys.argv[2])

    rounds = range(int(math.ceil(math.log(n, 2))))

    cards = {}
    for player in range(n):
        cards[player] = defaultdict(str)

    traits = {}
    clues = {}
    for player in range(n):
        clues[player] = {}
        traits[player] = {}

    for line in fin:
        es = line.split('\t')
        recipient = es[1]
        for round in rounds:
            round_text = es[3+round*5:3+round*5+5]
            try:
                receiver_trait = int(round_text[0])
                player = int(round_text[2])
                clue_round = round_text[3]
                clue = round_text[4]

                # card from the table
                cards[player][clue_round] += ','+recipient+': '+clue.strip()
            except:
                pass
        if len(es) > 3+len(rounds)*5:
            try:
                cards[int(es[1])][string.uppercase[len(rounds)-1]] += ','+es[-1].strip()
            except:
                pass
    fin.close()

    # instructions for writing clue
    how = 
    clues[recipient][round] = "(%s) %s,%s,%s" % (how, round, rule, opposite)

    for player in cards:
        fout.write(str(player))
        for round in string.uppercase[:len(rounds)]:
            clues = cards[player][round].split(',')
            for clue in clues:
                fout.write('\t'+clue)
        fout.write('\n')
            
