

### Solve with one loop
# The points of interest are the peaks and valleys in the given graph.
# We need to find the largest peak following the smallest valley. 
# We can maintain two variables - minprice and maxprofit corresponding to the smallest valley and maximum profit 
# (maximum difference between selling price and minprice) obtained so far respectively.

def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max_profit = 0
    min_price = float('inf')

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
    return max_profit
        
###  This solution requires two for loops         
#
#         max_profit = 0
#         for i in range(len(prices)-1):
#             # bypass decreasing trend
#             if prices[i] < prices[i+1]: 
#                 for j in range(i+1, len(prices)):
#                     profit = prices[j] - prices[i]
#                     if profit >= max_profit:
#                         # print("i = %d, j = %d, profit = %d" % (i,j,profit))
#                         max_profit = profit
#                         latest = j+1                       
#         return max_profit



                
            
        
        
