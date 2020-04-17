from collections import Counter
import heapq
import re

class ToyElement:
    def __init__(self, toy, count):
        self.toy = toy
        self.count = count
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.toy > other.toy
        return self.count < other.count

def popularNToys(numToys, topToys, toys, numQuotes, quotes):
    
    if numToys == 0 or numQuotes == 0 or topToys == 0:
        return []

    # Each quote can only contribute to the count once
    word_list = []
    for quote in quotes:
        word_list += set(quote.lower().replace('[^a-z0-9]', '').split())

    num_occurrences_word = Counter([toy for toy in word_list if toy in toys])
    
    # We're okay
    largest = heapq.nsmallest(topToys, iterable=num_occurrences_word.keys(), key=lambda x: (-num_occurrences_word[x], x))
    return largest