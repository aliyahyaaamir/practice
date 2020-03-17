from collections import Counter
import heapq

def popularNToys(numToys, topToys, toys, numQuotes, quotes):

    if numToys == 0 or topToys == 0 or numQuotes == 0:
        return []

    # Faster lookups
    toysSet = set(toys)
    counter = Counter()
    for quote in quotes:
        words = quote.split()
        filtered_words = filter(lambda word: word in toysSet, words)
        counter.update(set(filtered_words))

    popularToys = sorted(counter)
    print(counter)
    # print(popularToys)
    if topToys > numToys:
        return [toy for toy in popularToys]
    
    largest = heapq.nlargest(topToys, counter.items(), lambda toy: toy[1])
    return [toy[0] for toy in largest]


if __name__ == "__main__":
    
    r_strings = popularNToys(5, 2, ['anacell', 'betacellular', 'aa', 'deltacellular', 'eurocell'],\
         3,\
         ['Best services services provided by anacell aa', \
             'betacellular has aa great services', \
                 'anacell provides much better services than all other'])
    
    print(r_strings)