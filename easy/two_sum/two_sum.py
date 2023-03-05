# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Copy list to dictionary where keys are numbers from list and values are the indices 
# Optimizes time efficiency since dictionary lookup is O(1) on average
# Time complexity: O(n) since we have to traverse the list that can contain upto n items
# Space complexity: O(n) since dictionary can contain at most n items

def find_two_sum(nums: list[int], target: int) -> list[int]:
    dict = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in dict:
            print(dict)
            return [index, dict.get(diff)]
        dict[num] = index