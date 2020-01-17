import EarleyParser
import State


def test_acceptable_words():
    for grammar, terminals, word in (
            [
                {"S": [["(", "S", ")", "S"], []]},
                ["(", ")", ""],
                ["(", "(", "(", ")", ")", ")"]
            ],
            [
                {"S": [["(", "S", ")", "S"], []]},
                ["(", ")", ""],
                ["(", ")", "(", ")"]
            ],
            [
                {"S": [["(", "T", ")"], []], "T": [['T', 'a'], []]},
                ["(", ")", "a", "a"],
                ["(", "a", "a", ")"]
            ]
    ):
        earley = EarleyParser.Parser(grammar, terminals)
        assert earley.word_in_grammar(word) == 1


def test_denied_words():
    for grammar, terminals, word in (
            [
                {"S": [["(", "S", ")", "S"], []]},
                ["(", ")", ""],
                ["(", "(", ")", ")", "("]
            ],
            [
                {"S": [["(", "S", ")", "S"], []]},
                ["(", ")", ""],
                ["(", "(", "(", "("]
            ],
            [
                {"S": [["(", "T", ")"], []], "T": [['T', 'a'], []]},
                ["(", ")", "a", "a"],
                ["(", "(", "a", "a", "a"]
            ]
    ):
        earley = EarleyParser.Parser(grammar, terminals)
        assert earley.word_in_grammar(word) == 0


def test_state_representation():
    seg = State.State('S', ['T', 'a'], 0, 0)

    assert seg.__repr__() == '[S -> .Ta, 0, dot_idx: 0]'
