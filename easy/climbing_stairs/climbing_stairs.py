# Solution 1 - Dyanmic programming recursive approach, the number of ways to get to destination from step x is summation of number of ways from step x+1 and step x+2, we can perform bottom up recursion, sum node values upto the root. Since we are essentially just solve the same sub problems over and over, we can store precomputed results for a certain node in a dictionary, when solving the same problem again, we can simply access the dictionary instead of performing recursion again 

# def climbStairs(self, n: int) -> int:
#     dict = {}
#     return self.climbStair(n,0, dict)

# def climbStair(self, target:int, current: int, dict) -> int:
#     if current == target:
#         return 1
#     elif current > target:
#         return 0
    
#     if not dict.get(current+1):
#         dict[current+1] = self.climbStair(target, current+1, dict)
#     if not dict.get(current+2):
#         dict[current+2] = self.climbStair(target, current+2, dict)
#     return dict[current+1] + dict[current+2]

# Soltion 2 - number of ways to get to destination from step x is summation of number of ways from step x+1 and step x+2
# Working backwards, if step 5 is the destination, there is one step from step 4: 4-> 5, there are two ways from step 3: 3->4->5 or 3->5, 
# there are three ways from step 2: 2->3 (which leads to 2 ways) or 2->4 (which leads to 1 way) and so, so we are essentially creating a pattern of fibonacci numbers
# Time complexity: O(n) - linear time complexity since we are running a for loop for approximately n iterations
# Space complexity: O(1) - constant space use, only assigning a couple of variables

def climbStairs(self, n: int) -> int:
    left = 1
    right = 1
    for i in range(n-1):
        temp = left
        left = left+right
        right = temp

    return left