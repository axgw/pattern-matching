import unittest
from simple_patterns import Lit, Any, Either


class MyTestCase(unittest.TestCase):

    def test_literal_substring_alone_no_match(self):
        # /abc/ does not match "abc"
        assert not Lit("ab").match("abc")

    def test_literal_superstring_no_match(self):
        # /abc/ does not match  "ab"
        assert not Lit("abc").match("ab")

    def test_literal_followed_by_literal_match(self):
        # /a/+/b/ matches "ab"
        assert Lit("a", Lit("b").match("ab"))

    def test_literal_followed_by_literal_no_match(self):
        # /a/+/b/ does not match "ac"
        assert not Lit("a", Lit("b")).match("ac")

    def test_any_matches_empty(self):
        # /*/ matches ""
        assert Any().match("")

    def test_any_matches_entire_string(self):
        # /*/ matches "abc"
        assert Any().match("abc")

    def test_any_matches_as_prefix(self):
        # /*def/ matches "abcdef"
        assert Any(Lit("def")).match("abcdef")

    def test_any_matches_as_suffix(self):
        # /abc*/ matches "abcdef"
        assert Lit("abc", Any()).match("abcdef")

    def test_any_matches_interior(self):
        # /a*c/ matches "abc"
        assert Lit("a", Any(Lit("c"))).match("abc")

    def test_either_followed_by_literal_match(self):
        # /{a,b}c/ matches "ac"
        assert Either(Lit("a"), Lit("b"), Lit("c")).match("ac")

    def test_either_followed_by_literal_no_match(self):
        # /{a,b}c/ doesn't match "ax"
        assert not Either(Lit("a"), Lit("b"), Lit("c")).match("ax")


if __name__ == '__main__':
    unittest.main()
