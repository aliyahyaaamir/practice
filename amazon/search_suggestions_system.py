"""

This is very clearly a Trie question

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
    

    """
    a,     b, c
    l, j

    """
    def traverse(self, node: Node, letter, words):

        if node.is_leaf:
            words.append(letter)

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


if __name__ == "__main__":
    trie = Trie()
    trie.insert('mobile')
    trie.insert('mouse')
    trie.insert('moneypot')
    trie.insert('monitor')
    trie.insert('mousepad')

    searchword = 'mouse'
    output = []
    for index in range(1, len(searchword) + 1):
        output.append(trie.search_prefix(searchword[:index]))