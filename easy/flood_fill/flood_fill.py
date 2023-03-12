# Recursive approach - depth first searh 
# Keep modifying color of current cell until you either reach the end of the board or the color of the current cell is different from original
# Time complexity: O(n) - at worst, you have to iterate over every cell in the board, directly proportional to size of board
# Space complexity: O(n) - each function call is for one cell, the maximum depth of the call stack would be proportional to size of the board, for example, consider if all cells had the same color, 

def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    
    current_color = image[sr][sc]

    if color == current_color:
        return image
    
    return fill(image, sr, sc, current_color, color)

def fill(image: list[list[int]], sr: int, sc: int, current_color: int, color: int) -> list[list[int]]:
    if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != current_color:
        return
    
    image[sr][sc] = color
    
    fill(image, sr-1, sc, current_color, color)
    fill(image, sr+1, sc, current_color, color)
    fill(image, sr, sc-1, current_color, color)
    fill(image, sr, sc+1, current_color, color)
    return image