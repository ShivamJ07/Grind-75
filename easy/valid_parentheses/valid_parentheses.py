# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'

def check_valid_parens(s:str) -> bool:
    # Store paren mappings in a dictionary with closing paren as key and opening paren as value
    # Store all opening parens in a stack, once a closing paren is hit, verify it matches the top of the opening paren stack
    # Time complexity: O(n) since we have to traverse a string of n characters
    # Space complexity: 0(n) since we may have to create a stack of upto n characters (if all characters were opening parens)

    paren_mapping = {'}':'{', ')':'(', ']':'['}
    tokens = []
    for char in s:
        # if char is a closing paren
        if char in paren_mapping:
            top_token = tokens.pop() if tokens else '_'
            if top_token != paren_mapping[char]:
                return False
        # if char is a opening paren
        else:
            tokens.append(char)

    return not tokens

# An empty list returns false, if all opening parens matched -> list empty, return true, else false
# .pop() modifies the list and returns last element if no index is specified