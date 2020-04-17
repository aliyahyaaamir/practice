"""
Figure out direction of asteroids

Key thing to consider is index as well

ex. -2, -1, 1, -2

- goes left
+ goes right

Initial idea, iterate through keeping track of the last asteroid
from left to right

-2, no last asteroid -> nothing happens
-1, same polarity as last one -> do nothing
1, going right -> ...actually, need to look ahead

hmm that does not work

maybe consider pairs, def not a dp problem
is it a recursive problem?
1, -2, 1
    1
    -2
    1

    So it is a stack problem huh, go figure

"""

def asteroid_collision(asteroids: list) -> list:

    """
    So it is a stack problem huh, go figure

    [5, 10, -5]

    I guess you just pop on diff polarities

    5
    10 vs -5
    10

    """
    asteroid_stack = []
    for asteroid in asteroids:

        if asteroid > 0:
            asteroid_stack.append(asteroid)
        elif len(asteroid_stack) > 0:
            left = asteroid_stack.pop()
            


        

    

if __name__ == "__main__":
    input = [10, 2, -5]
    output = asteroid_collision(input)
    print(output)