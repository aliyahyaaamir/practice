import requests
import json

class TreeNode:
    def __init__(self, val: str):
        self.children = {}
        self.isLeaf = False
        self.val = val
    

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word : str) -> None:

        children = self.root.children
        for letter in word:
            if letter in children:
                children = self.root.children[letter]
            else:
                newNode = TreeNode(letter)
                self.root.children[letter] = newNode
                children = newNode.children
        
        


    def search(self) -> bool:
        pass

if __name__ == "__main__":
    # response = requests.get(('https://api.github.com'))
    # print(response.json())
    # headers = response.headers

    # s = input('->')
    # print(s, len(s))

    # get comfortable trimming strings I guess

    # response = requests.get('https://httpbin.org/stream/20')
    
    # for line in response.iter_lines():

    #     # filter out keep-alive new lines
    #     if line:
    #         decoded_line = line.decode('utf-8')
    #         print(json.loads(decoded_line))
