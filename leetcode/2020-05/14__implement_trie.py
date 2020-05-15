import unittest

# Source: https://leetcode.com/problems/implement-trie-prefix-tree

# Assumptions:
# 1. You may assume that all inputs are consist of lowercase letters a-z.
# 2. All inputs are guaranteed to be non-empty strings.

class Node:
    def __init__(self):
        self.dict = {}  # letters -> nodes
        self.isWord = False

    def link(self, letter:str, node):
        self.dict[letter] = node

    def contains(self, letter:str)->bool:
        return letter in self.dict.keys()

    def get(self, letter:str):
        return self.dict[letter]


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word:str) -> None:
        """
        Inserts a word into the trie.
        """
        currentNode = self.root
        for i, letter in enumerate(word):
            if not currentNode.contains(letter):
                newNode = Node()
                currentNode.link(letter, newNode)
                currentNode = newNode  # Walk to the next node
            else:
                currentNode = currentNode.get(letter)  # Walk to the next node

        # On the final letter, we need to toggle the isWord flag of this node
        currentNode.isWord = True


    def search(self, word:str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currentNode = self.root
        for letter in word:
            if not currentNode.contains(letter):
                return False
            currentNode = currentNode.get(letter)
            # print(f"{letter} | {currentNode.isWord}")

        # The final currentNode must have the isWord flag toggled to return true
        return currentNode.isWord

    def startsWith(self, prefix:str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currentNode = self.root
        for letter in prefix:
            if not currentNode.contains(letter):
                return False
            currentNode = currentNode.get(letter)  # Walk to the next node
        return True


class Test(unittest.TestCase):

    def test(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))   # returns true
        self.assertFalse(trie.search("app"))    # returns false
        self.assertTrue(trie.startsWith("app")) # returns true
        trie.insert("app")
        self.assertTrue(trie.search("app"))     # returns true

unittest.main()
