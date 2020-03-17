class Node:

    def __init__(self, letter: str, is_leaf: bool = False):
        self.children = dict()
        self.letter = letter
        self.is_leaf = is_leaf
    
    def add_child(self, node, letter: str):
        self.children[letter] = node

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head_node = Node('')
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.

        Want to insert every letter into Trie

        I guess we would technically first want
        to do a search and make sure that the
        word is not already in the Trie
        """
        node = self.head_node
        for letter in word:
            
            node_children = node.children
            if letter in node_children:
                # No insertion necessary
                node = node.children[letter]
            else:
                # make last node before this,
                # not a leaf anymore
                node.is_leaf = False
                new_node = Node(letter, True)
                node.add_child(new_node, letter)
                node = new_node
        
        # make last node a leaf
        node.is_leaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        # Go through Trie
        node = self.head_node

        for letter in word:
            node_children = node.children
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]

        return True if node.is_leaf else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        node = self.head_node
        for letter in prefix:
            
            node_children = node.children
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]
        
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
word = 'apple'
obj.insert(word)
param_2 = obj.search(word)
assert param_2 == True
param_3 = obj.startsWith(prefix = 'ap')
assert param_2 == True
param_4 = obj.search('app')
assert param_4 == False
