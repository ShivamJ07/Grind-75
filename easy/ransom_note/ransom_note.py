import collections

# First check if length of ransom note is greater than magazine, then it is impossible to create ransom note as not sufficient distinct letter in magazine
# Time complexity
# Space complexity

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