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

    def searchForFirstMatch(self, string: str, initial_index):

        node = self.head_node
        for index, letter in enumerate(string):

            node_children = node.children
            if letter in node_children:
                node = node_children[letter]
            else:
                return index + initial_index if node.is_leaf else -1
        return len(string) + initial_index if node.is_leaf else -1

        """
        hey
        1
        3
        """

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

def login_helper(password_trie, password):

    index = 0
    last_index = 0
    while index != len(password):
        index = password_trie.searchForFirstMatch(password[index:], initial_index = index)
        if index == -1:
            return False

        if index == last_index:
            return False
        last_index = index
        
    
    return True


def attempt_login(passwords: list, password: str) -> bool:
    """
    Put passwords into a Trie like structure
    """
    password_trie = Trie()
    for _password in passwords:
        password_trie.insert(_password)

    can_login = login_helper(password_trie, password)
    return can_login

if __name__ == "__main__":
    passwords = ['abra', 'ka', 'dabra']
    password = 'kadabraabraka'

    passwords = ['hello', 'planet']
    password = 'helloworld'

    output = attempt_login(passwords, password)
    print(output)

    n = int(input().strip())
    print(n)
