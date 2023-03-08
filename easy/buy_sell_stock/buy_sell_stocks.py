# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

def max_profit(prices: list[int]) -> int:
    # Maintain a track of the current profit, maximum profit and minimum price
    # If a lower price than min price is encountered, that will be new min price as it will maximize any future profits
    # If a profit higher than max profit is encountered, it is the new max profit
    # Time complexity: O(n) - iterating once over list of size n
    # Space complexity: O(1) - only defining a couple of variables to store values, regardless of size of list
    
    min_price = prices[0]
    current_profit = max_profit = 0
    for current_price in prices:
        current_profit = current_price - min_price
        if current_profit > max_profit:
            max_profit = current_profit
        if min_price > current_price:
            min_price = current_price
    
    return max_profit