from EarleyParser import Parser
import State

if __name__ == '__main__':
    # Simple test
    grammar = {
        "S": [["(", "S", ")", "S"], []],
    }

    terminals = ["(", ")", ""]  # ['Det', 'Noun', 'Verb', 'Aux', 'Prep', 'Proper-Noun']
    word = ["(", "(", ")", ")", "(", ")"]

    earley = Parser(grammar, terminals)

    print("GRAMMAR: ", grammar)
    print("WORD: ", ''.join(word))
    print("'%s' in GRAMMAR: " % ''.join(word), earley.word_in_grammar(word))

    print(earley)

    print(State.State('S', ['T', 'a'], 0, 0))
