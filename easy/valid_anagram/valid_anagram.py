# Compare occurences of characters in one string to another
# Create two dictionaries, one for each string, where the key is the character and the value is the number of occurences 
# Time complexity: 0(n) - linear time since we have to access each character in the string and each key in the dictionary - proportional to size of string
# Space complexity: O(n) - linear space use since we are creating dictionaries, space required is proportional to size of string

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_char_count, t_char_count = {}, {}
    for i in range(len(s)):
        s_char_count[s[i]] = s_char_count.get(s[i], 0) + 1
        t_char_count[t[i]] = t_char_count.get(t[i], 0) + 1
    
    for key in s_char_count:
        if s_char_count.get(key) != t_char_count.get(key):
            return False
    
    return True

# dict.get(key, default_value) is better than dict[] as you can return a default value and an error is not raised if the key is not found