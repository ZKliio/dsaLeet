## this is the submitted solution ##
def maxProfit(prices):
    i = 0
    j = 0
    buy = 0
    sell = 1
    if len(prices) < 2:
        print("Not Found")
        return 0
    while prices[sell] - prices[buy] < 0:
        #negative rizz
        if sell < len(prices) - 1:
            buy = sell
            sell +=1
        else:
            print(prices[buy], prices[sell])
            print("Not Found")
            return 0

    #set fixed ptrs
    i = buy
    j = sell
    while sell <= len(prices)-1:
        potentialprofits = prices[sell] - prices[buy]
        currentholdings = prices[j] - prices[i]
        #if thrs a btr sell option
        if potentialprofits < 0:
            buy = sell
            sell += 1
        else:    
            #if thr is a cheaper buy option, dont buy straight away, compare to later prices 
            if potentialprofits > (prices[j] - prices[i]):
                i = buy
                j = sell
                sell+=1   
            
            # continue searching if no higher potentials    
            elif potentialprofits <= (prices[j] - prices[i]):
                sell += 1
    currentholdings = prices[j] - prices[i]
        

    print(prices[i], prices[j])
    print(currentholdings)
    print(prices[j]- prices[i])
    return (prices[j]- prices[i])
















#prices = [7, 1, 5, 3, 6, 4]

#prices = [7, 4, 2, 3, 1, 5]

# prices = [7, 6, 2, 5, 1, 3]

#prices = [7, 6, 5, 4, 3, 1]

# prices = [2,4,1]

#prices = [3, 2, 6, 5, 0, 3]

#prices = [1, 2, 4]
prices = [2,1,2,1,0,1,2]
maxProfit(prices)
