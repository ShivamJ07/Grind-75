# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.

import math

# binary search - used to locate a target in a sorted array by dividing search interval in half in each iteration
# if target is lower than middle element in search interval, reduce search interval to lower half, discard upper half 
# if target is higher than middle element in search interval, reduce search interval to upper half, discard lower half
# time complexity: O(log n) - logarithmic time complexity since search inteval is halved in each iteration - half as many elements to search so number of iterations would grow at most logarithmically with respect to size of input
# space complexity: O(1) - constant space use since you only require a few variables, you do not need to define any new data structures

def search(nums: list[int], target: int) -> int:
    start, end = 0, len(nums) - 1
    while start <= end:  
        pivot = math.floor((start+end)/2)
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            start = pivot+1
        else:
            end = pivot-1
    return -1
        

