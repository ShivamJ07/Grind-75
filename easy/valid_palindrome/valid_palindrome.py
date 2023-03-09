# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

def check_valid_palindrome(s:str) -> bool:
    # Two pointer method, maintain a reference to start and end of string
    # If current character is not alphanumeric, increment pointer, if both characters are alphanumeric, compare and verify they are equal
    # Keep doing this until both pointers meet, i.e. no more characters to compare i.e. start >= end
    # Time complexity: O(n) - linear time since we are iterating over each character in the string in while loop
    # Space complexity: O(1) - constant space use since we are not creating any new data structures, simply declaring a couple of variables
    
    start = 0
    end = len(s) - 1
    while start < end:
        start_char = s[start].lower()
        end_char = s[end].lower()
        if not start_char.isalnum():
            start += 1
            continue
        elif not end_char.isalnum():
            end -= 1
            continue
        else:
            if start_char != end_char:
                return False
            start += 1
            end -= 1

    return True
