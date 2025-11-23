import unittest

from task3 import build_nfa_from_regex


class RegexToNfaTests(unittest.TestCase):
    def assertMatches(self, regex, accepted, rejected):
        nfa = build_nfa_from_regex(regex)
        for word in accepted:
            self.assertTrue(nfa.matches(word), f"{regex} should accept {word!r}")
        for word in rejected:
            self.assertFalse(nfa.matches(word), f"{regex} should reject {word!r}")
        return nfa

    def test_simple_concatenation(self):
        self.assertMatches("012", ["012"], ["01", "", "0122"])

    def test_plus_and_question(self):
        self.assertMatches(
            "0+1+",
            ["01", "0011", "0001111"],
            ["", "0", "1", "10"],
        )
        self.assertMatches(
            "(0|1)2?",
            ["0", "1", "02", "12"],
            ["", "2", "22"],
        )

    def test_star_and_union(self):
        self.assertMatches(
            "(0+|10)*9",
            ["9", "0009", "000109", "10109"],
            ["", "0", "10", "90"],
        )

    def test_question_allows_empty(self):
        nfa = self.assertMatches("3?", ["", "3"], ["33", "4"])
        with self.assertRaises(ValueError):
            nfa.matches("a")

    def test_invalid_regex_rejected(self):
        for expr in ["", "(", "0|", "0??", "0|()"]:
            with self.assertRaises(ValueError):
                build_nfa_from_regex(expr)


if __name__ == "__main__":
    unittest.main()

