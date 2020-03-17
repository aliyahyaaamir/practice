import collections
from functools import reduce

def replaceWords(roots, sentence):
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = True
    
    for root in roots:
        reduce(dict.__getitem__, root, trie)[END] = root
    
    print(trie)

    # def replace(word):
    #     cur = trie
    #     for letter in word:
    #         if letter not in cur or END in cur: break
    #         cur = cur[letter]
    #     return cur.get(END, word)

    # return " ".join(map(replace, sentence.split()))


if __name__ == "__main__":
    replaceWords(['cat', 'hat'], 'cattle in the hat')
    