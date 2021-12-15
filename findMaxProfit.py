import pdb
numOfTrade = 2
dataSource = [2,3,1,2,9,8,4,2,6,3]

def Profit(dataSource ,numOfTrade):
    sumOfProfit = 0
    for i in range(0, numOfTrade):
        maxProfit = 0
        lowest = dataSource[0]

        buyPt = 0
        sellPt = 0
        start = 0
        
        for x in range(0,len(dataSource)):
            if dataSource[x] < lowest: 
                start = x
                lowest = dataSource[x]
            profit = dataSource[x] - lowest
            
            if profit > maxProfit:
                maxProfit = profit
                buyPt = start
                sellPt = x
        
        sumOfProfit = sumOfProfit + maxProfit
        dataSource.pop(buyPt)
        dataSource.pop(sellPt-1)
   
    return sumOfProfit    

def main():
 
  if numOfTrade <= len(dataSource)/2:
    sumOfProfit = Profit(dataSource,numOfTrade)
    print(" Sum Of Profit is ", sumOfProfit)
  else:
    print(" trades is greater than allowed")

       
if __name__=='__main__':
    main()