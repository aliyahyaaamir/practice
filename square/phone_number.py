"""
Let's just startoff by rebuilding a Trie

So for the phone number question, we can insert numbers and for every node the associated letters that correspond to it

"""

class Node:

    def __init__(self, letter: str):
        self.children = {}
        self.is_leaf = False
        self.letter = letter


class Trie:

    def __init__(self):
        self.root = Node('')
    
    def insert(self, word: str) -> None:

        node = self.root
        for letter in word:
            node_children = node.children

            # Letter exists, let's just advance forward
            if letter in node_children:
                node = node.children[letter]
            else:
                # Need to create a new node
                new_node = Node(letter)
                node.children[letter] = new_node

                node = new_node

        ndoe.is_leaf = True
    
    def search(self, word: str) -> bool:

        node = self.root

        for letter in word:
            node_children = node.children

            if letter in node_children:
                node = node.children[letter]
            else:
                return False
        
        return True if node.is_leaf else False


def letter_combinations(digits) -> list:
    """
    :type digits: str
    :rtype: List[str]
    """
    letters_mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    
    # intuition is that no matter what you have to iterate through the digits array/string
    if digits == '':
        return []

    digit_letter = []
    total_combinations = 1
    
    for digit in digits:
        chars = letters_mapping[digit]
        digit_letter.append(chars)
        total_combinations *= len(chars)
        
    # ans = ['' for i in range(total_combinations)]
    first_set = digit_letter[0]
    comb = first_set
    
    if (len(digit_letter) == 1):
        comb = list(first_set)

    for j in range(1, len(digit_letter)):

        comb = [x + y for x in comb for y in digit_letter[j]]
        print(comb)

    return comb

if __name__ == "__main__":
    
    letter_combinations("23")