class State(object):
    """Represents [A -> a.b, idx]"""
    def __init__(self, label, rules, dot_idx, position=0):
        self.label = label
        self.rules = rules
        self.dot_idx = dot_idx
        self.position = position

    def __hash__(self):
        return hash(str(self))

    def next(self):
        """Returns the symbol after the dot"""
        if self.dot_idx >= len(self.rules):
            return ""
        return self.rules[self.dot_idx]

    def complete(self):
        """Is [A -> a., idx]"""
        return len(self.rules) == self.dot_idx

    def __eq__(self, other):
        return (self.label == other.label and
                self.rules == other.rules and
                self.dot_idx == other.dot_idx and
                self.position == self.position)

    def __repr__(self):
        rule_string = ''.join(self.rules[:self.dot_idx]) + '.' + ''.join(self.rules[self.dot_idx:])
        return '[%s -> %s, %d, dot_idx: %d]' % (self.label, rule_string, self.position, self.dot_idx)


# Constants
INITIAL_STATE = State('S\'', ['S'], 0,  0)
ACCEPTING_STATE = State('S\'', ['S'], 1, 0)
