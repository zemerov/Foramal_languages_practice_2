from EarleyParser import Parser
import State

if __name__ == '__main__':
    # Simple test
    grammar = {  # Correct bracket sequence
        "S": [["(", "S", ")", "S"], []],  # [] Defines EPS word
    }

    terminals = ["(", ")", ""]  # You have to define terminals
    word = ["(", "(", ")", ")", "(", ")"]

    earley = Parser(grammar, terminals)

    print("GRAMMAR: ", grammar)
    print("WORD: ", ''.join(word))
    print("'%s' in GRAMMAR: " % ''.join(word), earley.word_in_grammar(word))

    print(earley)
