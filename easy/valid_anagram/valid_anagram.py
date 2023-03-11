def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_char_count, t_char_count = {}, {}
    for i in range(len(s)):
        s_char_count[s[i]] = s_char_count.get(s[i], 0) + 1
        t_char_count[t[i]] = t_char_count.get(t[i], 0) + 1
    
    for key in s_char_count:
        if s_char_count[key] != t_char_count[key]:
            return False
    
    return True