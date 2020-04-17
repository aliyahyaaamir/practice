"""
It makes sense that this is a trie
So the idea is that you insert every word into the trie first
compound words will have multiple is_leaf(s) along the way
Hmm
Well I'll be damned

O(k) to insert and find a word

I don't really see dynamic programming working here, but hey who knows
"""


class Node:
    def __init__(self, letter: str):
        self.letter = letter
        self.children = {}
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.head = Node('')
    
    def insert(self, word: str) -> None:
        node = self.head

        node_children = node.children

        for letter in word:

            if letter in node_children:
                node = node.children[letter]
            else:
                new_node = Node(letter)
                node.children[letter] = new_node
                node = new_node
            
            node_children = node.children
        
        # Set leaf here
        node.is_leaf = True
    
    def traverse(self, node: Node, letter, words):

        if node.is_leaf:
            words.append(letter)
            return words

        for child_letter, child in node.children.items():
            self.traverse(child, letter + child_letter, words)
        
        return words

    def search_prefix(self, prefix: str) -> list:
        node = self.head
        node_children = node.children

        for letter in prefix:
            
            if letter in node_children:
                node = node.children[letter]
                node_children = node.children
            else:
                # not found with prefix; early return
                return []
        
        # at this point we have a node up until the prefix
        # we can keep iterating and get all strings
        # only want at most 3

        words = sorted(self.traverse(node, prefix, []))[:3]
        return words




# def all_combos(words: list, original_list: list, current_word, r_words):
    # if not words:
    #     return r_words.append(current_word)
    # for index, word in enumerate(words):
    #     all_combos(words[index + 1:], words, current_word + word, r_words)
    # return r_words

    # for i in range(len(words)):
    #     for j in range(len(words)):
    #         print(words[i] + words[j])

if __name__ == "__main__":


    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    trie = Trie()

    for word in words:
        trie.insert(word)
    
    # Okay awesome now we have a trie like structure with all the compound words in it
    # Now the idea is to return all the words that have at LEAST two is_leafs along the way (not including the last is_leaf)
    result = trie.traverse(trie.head, '', [])
    
    
    # output = all_combos(words, words, '', [])