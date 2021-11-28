"""
问题描述
https://www.codewars.com/kata/523a86aa4230ebb5420001e1
"""


# !/usr/bin/python
# -*- coding: UTF-8 -*-

def anagrams(word, words):
    new_words = words[:]
    for i in range(0, len(words)):
        if len(word) != len(words[i]):
            new_words.remove(words[i])
        else:
            for j in range(97, 123):
                if int(chr(j) in word) ^ int(chr(j) in words[i]) == 1:
                    if words[i] in new_words:
                        new_words.remove(words[i])
    return new_words


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
