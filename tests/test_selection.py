import unittest

from fuzzingbook.GrammarFuzzer import GrammarFuzzer
from evogfuzz_formalizations.calculator import grammar_alhazen as grammar
from isla.derivation_tree import DerivationTree

from evogfuzz.input import Input
from evogfuzz.tournament_selection import Tournament


class TournamentSelection(unittest.TestCase):
    def test_selection(self):
        fuzzer = GrammarFuzzer(grammar)
        test_inputs = set()
        for idx, _ in enumerate(range(100)):
            inp = Input(
                DerivationTree.from_parse_tree(fuzzer.fuzz_tree())
            )
            inp.fitness = idx
            test_inputs.add(inp)
        for inp in test_inputs:
            print(inp, inp.oracle, inp.fitness)

        selected = Tournament(test_inputs).select_fittest_individuals()
        print("______")
        for inp in selected:
            print(inp, inp.oracle, inp.fitness)


if __name__ == '__main__':
    unittest.main()
