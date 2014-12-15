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
        return str(bit(self.id, n))

    def target_attr(self, n):
        b = bin(self.target)
        return str(bit(self.target, n))

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

def gen(n):
    s = gen_arb(n)
    while not check(s):
        s = gen_arb(n)
    return s

if __name__ == "__main__":
    n = int(sys.argv[1])
    s = gen(n)
    players = [Player(i, s[i]) for i in range(n)]
    attrs = int(math.ceil(math.log(n, 2)))

    givers = zip(*[gen(n) for i in range(attrs)])

    out = open(sys.argv[2],'w')

    # header
    out.write('Player,Target')
    for attr in range(attrs):
        attr_name = string.uppercase[attr]
        out.write(','
                  +attr_name+','
                  +'Target Type,'
                  +'Giver,'
                  +'Round,'
                  +'Clue')
    out.write(',Lies,Dessert\n')

    # players
    for p in players:
        out.write(str(p.id)+','+str(p.target))
        for i in range(attrs):
            clue = '(%s),'
            out.write(','
                      +p.attr(i)+','
                      +p.target_attr(i)+','
                      +str(givers[p.id][i])+','
                      +random.choice(string.uppercase[:attrs])+','
                      +clue)
        # write second knights/knaves column, dessert
        out.write(', , \n')

    out.close()
    
