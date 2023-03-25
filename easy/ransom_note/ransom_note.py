import collections

# First check if length of ransom note is greater than magazine, then it is impossible to create ransom note as not sufficient distinct letter in magazine
# Create a dictionary where the key is a letter and value is number of times that letter appeared in magazine
# Iterate over every character in ransomNote, if it does not exist in dict return false, else reduce character count by 1 since the character was used 
# Time complexity: O(m+n) - time taken is a linear function of both length of magazine string (m) and length of ransom note string (n). We must iterate over all characters in magazine to count occurences and possibly over all characters in ransom note as well
# Space complexity: O(1) - space taken by a dictionary depends on number of key value pairs, since both strings are composed of letters, there can be atmost 26 key value pairs i.e. constant space use, it will not change even with very large strings

def canConstruct(ransomNote: str, magazine: str) -> bool:
    if  len(ransomNote) > len(magazine):
        return False
    dict = collections.Counter(magazine)
    # for char in magazine:
    #     char_num = dict.get(char)
    #     dict[char] = 1 if not char_num else 1 + char_num
    for char in ransomNote:
        # This also catches the case where dict[char] is 0 as if not 0 is true
        if not dict.get(char):
            return False
        else:
            dict[char] -= 1
    return True