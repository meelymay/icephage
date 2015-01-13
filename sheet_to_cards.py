import sys

class Player:
    def __init__(self, line):
        fields = line.split('\t')
        self.name = fields[0]
        self.rules = [fields[i] for i in range(5,len(fields),3)]
        self.same = [fields[i] == fields[i+1] for i in range(3, len(fields), 3)]
        if not self.name:
            raise Exception("empty name")

    def __str__(self):
        s = self.name
        s += '\n'+str(self.rules)
        s += '\n'+str(self.same)

        return s

def load_rules(f):
    players = []
    for line in f:
        try:
            players.append(Player(line))
        except:
            print "failed",line
    return players

if __name__ == '__main__':
    f = sys.argv[1]
    t = open(f, 'r')
    players = load_rules(t)    
    t.close()

    for player in players:
        print player
