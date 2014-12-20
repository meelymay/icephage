import sys, random, math, string

RULES = [('Only Es','No Es'),
         ('Alliteration','Non-alliteration'),
         ('Forward','Backward'),
         ('Truth','Lies')]

def bit(n, b):
    return n/(2**b)%2

class Player:
    def __init__(self, id, target):
        self.id = id
        self.target = target

    def attr(self, n):
        return bit(self.id, n)

    def target_attr(self, n):
        b = bin(self.target)
        return bit(self.target, n)

def check(s):
    seen = set([])
    i = 0
    while i not in seen:
        seen.add(i)
        i = s[i]
    return len(seen) == len(s)

def gen_arb(n):
    p = range(n)
    ts = []
    for i in range(n):
        t = random.choice(p)
        p.remove(t)
        ts.append(t)
        
    return ts

def gen_ids(n):
    s = gen_arb(n)
    while not check(s):
        s = gen_arb(n)
    return s

def gen_clues(players, rounds):
    mult = 10000
    clues = {}

    available = set()
    for player in players:
        clues[player] = {}
        for round in range(rounds):
            available.add(player*mult+round)

    for player in players:
        for round in range(rounds):
            p_r = random.sample(available, 1)[0]
            receiver = players[p_r/mult]
            about_round = p_r%mult
            target = receiver.target_attr(about_round)
            
            who = receiver.id
            rule = RULES[about_round][target]

            clue = '%s: Your enemy %s.' % (who, rule)

            clues[player][round] = clue
    return clues

if __name__ == "__main__":
    n = int(sys.argv[1])
    s = gen_ids(n)
    players = dict([(i, Player(i, s[i])) for i in range(n)])
    attrs = int(math.ceil(math.log(n, 2)))

    clues = gen_clues(players, attrs)

    out = open(sys.argv[2],'w')

    # header
    out.write('Player,Target')
    for attr in range(attrs):
        attr_name = string.uppercase[attr]
        out.write(','
                  +attr_name+','
                  +'Clue')
    out.write(',Lies,Dessert\n')

    # players
    for p in players.values():
        out.write(str(p.id)+','+str(p.target))
        for i in range(attrs):
            out.write(','
                      +str(p.attr(i))+','
                      +clues[p.id][i])
        # write second knights/knaves column, dessert
        out.write(', , \n')

    out.close()
    
