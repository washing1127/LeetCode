# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/14 14:38
# File: 0208.py
# Desc: 

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = []


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.li.append(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.li


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for i in self.li:
            if i.startswith(prefix): return True
        return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)