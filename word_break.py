"""
Input: s = "leetcode", wordDict = ["leet","code1", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Intuition
Can we simply go through the WordDict and see if we can recreate string S?
The trick here really is that we can reuse words in the list
We're guaranteed that there are no repeat words (not that it matters too much?)

How do we rule out dynamic programming here?


BFS on wordDict?
Where we don't use a visited list (so we can reuse words)

What does that look like?

initialize queue with beginning of word we care about, we could even initialize it to the empty string
then go through adding words that make up the remainder of the word

"leet"
    "code"

    return true

Let's code this up and see


Okay well I tried BFS and Tries and both those solutions crumble for trick strings


So it looks like dynamic programming to the rescue!

Fuck I hope it's not like a generate all combos? (probably not)


Order the strings by length

Append string to current_string




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

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        # Go through Trie
        node = self.head

        for letter in word:
            node_children = node.children
            if letter not in node.children:
                return False
            else:
                node = node.children[letter]

        return True if node.is_leaf else False

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

def dfs(s, trie):
    for index in range(len(s)):
        
        prefix = s[:index]
        suffix = s[index:]

        if trie.search(prefix) and suffix == '':
            return True
        elif trie.search(prefix) and dfs(suffix, trie):
            return True
        elif trie.search(suffix) and prefix == '':
            return True
    return False


# def word_break(s: str, word_dict: list) -> bool:
    
#     trie = Trie()

#     for word in word_dict:
#         trie.insert(word)

#     return dfs(s, trie)




def word_break(s: str, word_dict: list) -> bool:

    first_char = s[0]
    queue = [word for index, word in enumerate(word_dict) if word[0] == first_char]
    visited = []
    while queue:
        word_so_far = queue.pop(0)
        
        if word_so_far in visited:
            continue

        if word_so_far == s:
            return True
        
        # queue up other words in word_dict
        for w_index, word in enumerate(word_dict):
            if word_so_far + word in s:
                queue.append(word_so_far + word)
        visited.append(word_so_far)
    return False
 
# memo = {}

# def helper(current_string: str, string: str, word_dict: list):
#     if current_string in memo:
#         return memo[current_string]

#     if current_string == string:
#         return True

#     return_val = False
#     for word in word_dict:
#         if current_string + word in string:
#             val = helper(current_string + word, string, word_dict)
#             memo[current_string+word] = val
#             return_val = val or return_val

#     return return_val

# def word_break(s: str, word_dict: list) -> bool:
#     return helper('', s, word_dict)


if __name__ == "__main__":
    s = 'leetcode'
    word_dict = ['leet', 'code']

    s = 'applepenapple'
    word_dict = ["apple", "pen"]

    s = 'catsandog'
    word_dict = ["cats", "dog", "sand", "and", "cat"]

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    word_dict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

    result = word_break(s, word_dict)
