# Question: https://www.codingninjas.com/studio/problems/asteroid-collision_977232?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

from typing import List

def collidingAsteroids(asteroids: List[int]) -> List[int]:
    stack = []

    for ast in asteroids:
        # When current asteroid is moving right or stack is empty, just add the asteroid to the stack
        if ast > 0 or not stack:
            stack.append(ast)
        else:
            # Handle collisions with right-moving asteroids in the stack
            while stack and stack[-1] > 0:
                # Compare absolute values to decide which asteroid survives
                if stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    stack.pop()
                break
            else:
                # If we get here, no collision occurred or all right-moving asteroids are destroyed
                stack.append(ast)

    return stack

# Test the function
print(collidingAsteroids([3, -6, -4, 1, 5, 7, 3, -6, 5, 6]))