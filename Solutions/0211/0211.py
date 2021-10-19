# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/19 10:35
# File: 0211.py
# Desc: 
class WordDictionary:

    def __init__(self):
        self.dict = dict()

    def addWord(self, word: str) -> None:
        if len(word) not in self.dict.keys(): self.dict[len(word)] = set()
        self.dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        n = len(word)
        if n not in self.dict: return False
        for old_word in self.dict[n]:
            for a, b in zip(word, old_word):
                if a != "." and a != b: break
            else: return True
class WordDictionary:

    def __init__(self):
        self.dict = dict()

    def addWord(self, word: str) -> None:
        if len(word) not in self.dict.keys(): self.dict[len(word)] = set()
        self.dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        n = len(word)
        if n not in self.dict: return False
        for old_word in self.dict[n]:
            for a, b in zip(word, old_word):
                if a != "." and a != b: break
            else: return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

