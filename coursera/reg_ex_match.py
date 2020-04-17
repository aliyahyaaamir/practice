"""
Regular Expression Matching
., *

sample input : 'aa', 'a*'
sample output : true

Naive approach, simply iterate through both the pattern string and input string
Keeping track of the last letter processed for the pattern matching, and only moving ahead on the input when there isn't a match

Steps: 'a' compare to -> a
       'a' compare to -> * (which implies use last letter) Available options are: letter, pattern note: '**' does not make sense



Intuition
Trie based solution kind of yells at me
What would that look like?
Pattern lives in the trie
And you simply iterate through the letters simultaneously with the the trie

        'a'
        '*'

Typically regex expressions use FSMs to represent them


How would we model this?

* (keep retrying the last state)
. (any)


Turns out this son of a bitch is a dynamic programming question
I'll be damned


What is the optimal substructure here

dp[i][j] = does this match with the given pattern and text

'aa'



Looks like this is a backtracking problem
Let's practice and finesse this coursera interview!!
"""

def is_match(string: str, pattern: str) -> bool:
    
    if pattern == '':
        return not string # If text runs out before pattern it is not a match

    first_match = bool(string) and pattern[0] in {string[0], '.'}
    
    if len(pattern) >= 2 and pattern[1] == '*':
        return (first_match and is_match(string[1:], pattern[1:]))\
            or is_match(string[1:], pattern[2:])

    return first_match and is_match(string[1:], pattern[1:])
    




if __name__ == "__main__":
    string = 'aa'
    pattern = 'a*'

    string = 'ab'
    pattern = '.*'

    string = 'aa'
    pattern = 'a'

    string = 'aa'
    pattern = 'aa*'

    is_match = is_match(string, pattern)
    