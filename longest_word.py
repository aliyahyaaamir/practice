class Node:
    def __init__(self, letter: str, isLeaf: bool = False):
        self.letter = letter
        self.children = {}
        self.isLeaf = isLeaf
    
    def __str__(self):
        return self.letter

    def add_children(self, letter: str, node):
        self.children[letter] = node
        return node
        
    def has_letter(self, letter: str) -> bool:
        return letter in self.children
    
    def get_letter(self, letter: str):
        return self.children[letter] if letter in self.children else None

def longest_word(words: list) -> str:

    """
    Create a Trie structure

    First letter must exist first
    Only adding one letter at a time

    Cannot add more than one letter if the
    prefix includes more letters in the sequence

    """

    sorted_words = sorted(words)

    head_node = Node('')
    
    for word in sorted_words:
        
        node = head_node
        
        num_to_add = 0
        for index, letter in enumerate(word):
            if node.has_letter(letter):
                node = node.get_letter(letter)
            else:
                num_to_add += 1
                # node.isLeaf = False
                # node = node.add_children(letter, Node(letter, True))

        if num_to_add > 1:
            continue
        
        node = head_node
        for index, letter in enumerate(word):
            if node.has_letter(letter):
                node = node.get_letter(letter)
            else:
                num_to_add += 1
                node.isLeaf = False
                node = node.add_children(letter, Node(letter, True))

            
    
    # children = head_node.children
    words = []
    display(head_node, '', words)
    print(words)

longest_words = []

def display(node: Node, string: str, words: list):

    if node.isLeaf:
        print(string + '\n')
        longest_words.append(string)
        return
    
    # children is a dictionary
    words = []
    for letter, node_child in node.children.items():
        display(node_child, string + letter, words)

if __name__ == "__main__":
    words = ["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]
    longest_word(words)