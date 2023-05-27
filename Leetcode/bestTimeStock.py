def maxProfit(prices):
    i = 0
    
    buy = 0
    sell = 1
    
    print(f"Start buy: {prices[buy]}")
    print(f"Start sell: {prices[sell]}")
    while i <= len(prices) - 1 :
        potential_profit = prices[i] - prices[buy]
        profit = prices[sell] - prices[buy]

        if prices[i] < prices[buy] and potential_profit >= profit:
            buy = i
            print(f"buy: {prices[buy]}")
            print(f"sell: {prices[sell]}")
        if prices[i] > prices[sell]:
            sell = i
            print(f"buy: {prices[buy]}")
            print(f"sell: {prices[sell]}")
        if buy >= sell :
            sell = buy + 1
            print(f"buy: {prices[buy]}")
            print(f"sell: {prices[sell]}")
        i+=1

    # if buy < sell and sell <= len(prices) - 1:    
    
    if profit > 0:
        print(f"results: {(profit)}")
        return f"results: {(profit)}"
    else:
        print("Not Found")
        return 0
    # else:
    #     print("Not Found")
    #     return 0












#prices = [7, 1, 5, 3, 6, 4]

prices = [7, 4, 2, 3, 1, 5]

#prices = [7, 6, 5, 4, 3, 1]

#prices = [2,4,1]

#prices = [3, 2, 6, 5, 0, 3]
maxProfit(prices)