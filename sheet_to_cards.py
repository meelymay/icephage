import sys

RULES = ["Speak with a %s %s accent.",
         "Always refer to people by %s %s.",
         "When the person to your %s takes a drink, %s.",
         "Statement: %s%s"]

EXTRAS = [{True: "refined", False: "thick"},
          {True: "their name", False: ""},
          {True: "right", False: "left"},
          {True: "", False:""}]

PEOPLE = {}

class Player:
    def __init__(self, line):
        fields = [l.strip() for l in line.split('\t')]
        self.name = fields[0]
        self.id = int(fields[1])
        self.target = int(fields[2])
        self.chars = [fields[i] == '0' for i in range(3,len(fields),3)]
        self.rules = [fields[i] for i in range(5,len(fields),3)]
        self.same = [fields[i] == fields[i+1] for i in range(3, len(fields), 3)]
        if "Instruction" in self.name or "Person" in self.name:
            raise Exception("empty name")
        id = '0' + str(self.id) if self.id < 10 else str(self.id)
        PEOPLE[id] = self

    def __str__(self):
        s = self.name
        s += '\n'+str(self.rules)
        s += '\n'+str(self.same)
        s += '\n'+str(self.chars)

        return s

    def print_card(self, round):
        print self.name + ":"
        for i in range(4):
            print
        extra = EXTRAS[round][self.chars[round]]
        statement = RULES[round] % (extra, self.rules[round])
        for id in PEOPLE:
            statement = statement.replace(str(id), PEOPLE[id].name)
        print statement
        for i in range(4):
            print
        mark = 'O' if self.same[round] else 'X'
        print mark
        for i in range(2):
            print

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

    print PEOPLE

    for player in players:
        for i in range(4):
            # print player
            player.print_card(i)
