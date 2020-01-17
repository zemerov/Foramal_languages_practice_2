from State import *


class Parser:
    def __init__(self, grammar_, terminals_):
        self.situation_list = []  # List of states
        self.changed = []  # Need to check changes

        self.grammar = grammar_  # Grammar (dictionary)
        self.grammar[INITIAL_STATE.label] = INITIAL_STATE.rules
        self.terminals = terminals_  # Terminal states
        self.word = ''  # The word to recognize

    def is_terminal(self, tag):
        return tag in self.terminals

    def add_state(self, state, list_idx):
        self.situation_list[list_idx].add(state)

    def __str__(self):
        res = ''

        for i, chart in enumerate(self.situation_list):
            res += '\nSituation list[%d]\n' % i
            for state in chart:
                res += str(state) + '\n'

        return res

    def word_in_grammar(self, word_):
        self.word = word_
        self.situation_list = [set() for x in range(len(word_) + 1)]  # List of states
        self.changed = [True for i in range(len(word_) + 1)]

        self.add_state(
            INITIAL_STATE,
            0
        )

        for i in range(0, len(self.word) + 1):
            self.scan(i - 1, self.word[i - 1])

            while self.changed[i]:
                self.changed[i] = False

                self.predict(i)
                self.complete(i)

        if ACCEPTING_STATE in self.situation_list[-1]:
            return True
        else:
            return False

    def predict(self, list_idx):
        possible_states = set(self.situation_list[list_idx])
        for state in possible_states:
            next_symbol = state.next()
            if not state.complete() and not self.is_terminal(next_symbol):
                for transition in self.grammar[next_symbol]:
                    situation = State(
                            next_symbol,
                            transition,
                            0,
                            position=list_idx
                    )

                    if situation not in self.situation_list[list_idx]:
                        self.situation_list[list_idx].add(situation)
                        self.changed[list_idx] = True

    def scan(self, list_idx, letter):
        for state in self.situation_list[list_idx]:
            if letter == state.next() and self.is_terminal(state.next()):

                assert list_idx + 1 < len(self.situation_list)  # Check list_idx

                self.situation_list[list_idx + 1].add(
                    State(
                        state.label,
                        state.rules,
                        state.dot_idx + 1,
                        position=state.position
                    )
                )

    def complete(self, list_idx):
        if list_idx == 0:
            return

        possible_states = set(self.situation_list[list_idx])

        for complete_state in possible_states:
            if complete_state.complete():
                complete_possible_states = set(self.situation_list[complete_state.position])

                for state in complete_possible_states:
                    if state.next() == complete_state.label and not self.is_terminal(state.next()):
                        situation = State(
                                state.label,
                                state.rules,
                                state.dot_idx + 1,
                                position=state.position
                            )

                        if situation not in self.situation_list[list_idx]:
                            self.situation_list[list_idx].add(situation)
                            self.changed[list_idx] = True
