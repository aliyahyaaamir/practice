"""
There are N balls positioned in a row. Each of them is either red or white.
In one move we can swap two adjacent balls.
We want to arrange all the red balls in a consistent segment.
What is the minimum number of swaps needed?

S = 'WRRWWR'

output = 2

'WRRWRW'
'WRRRWW'

My natural instinct really is a stack
You make one pass through get all balls in the stack
Then as you go through it the first time, until you see your first Red add every white ball onto the stack
The number of those W balls represents the min number of moves necessary

See next example

S = 'WWRWWWRWR'

'WWWRWWRWR'
'WWWWRWRWR'
'WWWWWRRWR'
'WWWWWRRRW'

"""


def min_swaps_to_group_red_balls(S: str) -> int:
    stack = []

    seen_red = False
    at_least_two_reds = 0
    for ball in S:
        if seen_red and ball == 'W':
            stack.append(ball)
        if not seen_red and ball == 'R':
            seen_red = True
        if ball == 'R':
            at_least_two_reds += 1
    
    return len(stack) if at_least_two_reds == 2 else -1

if __name__ == "__main__":
    
    S = 'WRRWWR'
    S = 'WWRWWWRWR'
    S = 'WWW'
    # S = 'WWWR'
    # S = 'RW'
    S = 'WWWWWWRRRW'
    min_swaps = min_swaps_to_group_red_balls(S)


    