import unittest
from typing import Dict
from typing_extensions import Self


class TrieNode:
    def __init__(self) -> None:
        self._children = dict()
        self._is_end = False

    def add_child(self, ch: str, is_end: bool = False) -> None:
        if len(ch) > 1:
            raise ValueError("arg `chr` should be a single character.")

        self._children[ch] = TrieNode()
        self._is_end = is_end

    @property
    def children(self) -> Dict[str, Self]:
        return self._children

    @property
    def is_end(self) -> bool:
        return self._is_end

    @is_end.setter
    def is_end(self, v: bool) -> None:
        self._is_end = v


class Trie:
    def __init__(self) -> None:
        self._root = TrieNode()

    def insert(self, word: str) -> None:
        if word is None or len(word) == 0:
            raise ValueError("arg `word` is a invaild: {}.".format(word))

        curr = self._root
        for ch in word:
            if ch not in curr.children.keys():
                node = TrieNode()
                curr.children[ch] = node
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self._root
        for ch in word:
            if ch not in curr.children.keys():
                return False
            curr = curr.children[ch]

        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self._root
        for ch in prefix:
            if ch not in curr.children.keys():
                return False
            curr = curr.children[ch]

        return True


class TrieTest(unittest.TestCase):
    def test_case_0(self):
        trie = Trie()

        trie.insert("apple")
        trie.search("apple")
        trie.search("app")

        trie.startsWith("app")
        trie.insert("app")
        trie.search("app")


if __name__ == "__main__":
    unittest.main()
