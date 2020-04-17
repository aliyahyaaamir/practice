from collections import Counter
import heapq

# def popular_n_toys(numToys, topToys, toys, numQuotes, quotes):

    # if numToys == 0 or numQuotes == 0:
    #     return []

    # # Each quote can only contribute to the count once
    # num_occurrences_word = Counter()
    # for quote in quotes:
    #     words = quote.lower().replace('[^a-z0-9]', '').split()
    #     num_occurrences_word.update(set(toys) & set(words))
    
    # num_occurrences_word = Counter(sorted(num_occurrences_word.items(), key=lambda item: (-item[1], item[0])))
    # # We're okay
    # largest = heapq.nlargest(topToys, num_occurrences_word.keys(), key=lambda x: num_occurrences_word[x])
    # return [toy[0] for toy in largest]
from collections import Counter
import heapq

class ToyElement:
    def __init__(self, toy, count):
        self.toy = toy
        self.count = count
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.toy > other.toy
        return self.count < other.count

def popular_n_toys(numToys, topToys, toys, numQuotes, quotes):
    
    if numToys == 0 or numQuotes == 0:
        return []

    # Each quote can only contribute to the count once
    num_occurrences_word = Counter()
    word_list = []
    for quote in quotes:
        word_list += set(quote.lower().replace('[^a-z0-9]', '').split())

    toy_elements = []
    for toy in toys:
        toy_elements.append(ToyElement(toy, word_list.count(toy)))

    # num_occurrences_word = Counter([toy for toy in word_list if toy in toys])
    print([(toy.toy, toy.count) for toy in toy_elements])
    # We're okay
    largest = heapq.nlargest(topToys, toy_elements)
    return largest


if __name__ == "__main__":
    
    """
    If there were ties, I think they said to just go with alphabetical order

    There were edge cases with topToys being greater than numToys, I think it was like just return all toys that show up in quotes
    """

    quotes = ["Anacell provides the best services in the city", "betacellular has awesome services", "Best services provided by anacell, everyone should use anacell"]

    # r_value = popular_n_toys(5, 2, ['anacell', 'betacellular', 'aa', 'deltacellular', 'eurocell'], len(quotes), quotes)


    k = 2
    toys = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
    "I love anacell Best services; Best services provided by anacell in the town",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than eurocell",
    "betacellular is better than deltacellular",
    ]

    r_value = popular_n_toys(5, 2, toys, 5, reviews)