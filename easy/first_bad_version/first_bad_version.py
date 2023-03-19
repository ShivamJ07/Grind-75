import math

# Use binary search to efficiently traverse search space since it is essentially a sorted array
# We have to locate the index isBadVersion(index) is true and isBadVersion(index - 1) is false
# Time complexity: O(log n) - search space is halved with each iteration, time taken is logarithmically proportional to number of versions
# Space complexity: O(1) - constant space use, we only have to declare a couple of variables 

def firstBadVersion(n: int) -> int:
    start, end = 1, n
    while start <= end:
        mid = math.floor((start + end)/2)
        current = isBadVersion(mid)
        if not current:
            start = mid + 1
        else:
            current_prev = isBadVersion(mid - 1)
            if not current_prev:
                return mid
            else:
                end = mid - 1