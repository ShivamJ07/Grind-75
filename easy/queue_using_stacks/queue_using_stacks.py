# Use two arrays, s1 and s2
# s1 acts as the primary array, it stores any new elements that are pushed onto the queue
# s2 stores a subset of the older elements in reverse order, this is needed for peek and pop operations
# if s2 is empty, we pop an element from top from s1 and push to s2, so the ordering is reversed, top of s1 becomes bottom of s2, bottom of s1 becomes top of s2
# As a result, the oldest element in s1, the first added, at index 0, will become element at index -1 in s2, so peek and pop can access this element using stack operations

# Space complexity: O(n) - where n is number of elements in the queue, it is distributed among two lists
# Time complexity: Amortized O(1) - For a single pop operation, worst case is O(n) if s2 is empty as we need to pop from s1 and append to s2, so time taken is linearly proportional to number of elements in s1 or n. Best case is O(1) if s2 is non-empty as standard list pop operatio is O(1), so on average, the amortized time complexity is O(1) as each element would only be transferred from s1 to s2 once before it is popped 


class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.sort_stack_to_list()
        return self.s2.pop()
    
    def peek(self) -> int:
        self.sort_stack_to_list()
        return self.s2[-1]
    
    def empty(self) -> bool:
        return not self.s1 and not self.s2
    
    def sort_stack_to_list(self) -> None:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())