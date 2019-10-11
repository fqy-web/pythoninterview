'''
# 1 暴力枚举法
# 定义股票根据开盘日卖出的函数
# 传入参数为开盘价数组S
def stockPrice(S):
    sellDay = 0    # 卖出日
    buyDay = 0     # 买入日
    maxProfit = 0    # 最大收益

    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            if S[j] - S[i] > maxProfit:
                maxProfit = S[j] - S[i]
                buyDay = i
                sellDay = j
            else:
                pass
    # return (i, j, maxProfit)
    print("buyDay:{}  sellDay:{}  maxProfit:{}".format(buyDay + 1,
        sellDay + 1, maxProfit))

S = [10, 4, 8, 7, 9, 6, 2, 5, 3]
# S = [1, 2, 5, 4, 2, 10,]
stockPrice(S)
'''

'''
# 2 分而治之法
def findMaxProfit(S):
    # 返回格式为[buyDay, sellDay, maxProfit]
    if len(S) < 2:
        return [0, 0, 0]
    if len(S) == 2:
        if S[1] - S[0] > 0:
            return [0, 1, S[1] - S[0]]
        else:
            return [0, 0, 0]

    firstHalf = findMaxProfit(S[0: len(S)//2])
    secondHalf = findMaxProfit(S[len(S)//2: len(S)])
    finalResult = firstHalf
    if secondHalf[2] > firstHalf[2]:
        secondHalf[0] += len(S)//2
        secondHalf[1] += len(S)//2
        finalResult = secondHalf

    # 考虑在前一部分买入，后一部分卖出，分别找出最小最大开盘价
    lowestPrice = S[0]
    highestPrice = S[len(S)//2+1]
    buyDay = 0
    sellDay = len(S) // 2 + 1

    # 找出最小开盘价
    for i in range(len(S)//2):
        if S[i] < lowestPrice:
            lowestPrice = S[i]
            buyDay = i

    # 找出最大开盘价
    for i in range((len(S)//2), len(S)):
        if S[i] > highestPrice:
            highestPrice = S[i]
            sellDay = i

    if highestPrice - lowestPrice > finalResult[2]:
        finalResult[0] = buyDay
        finalResult[1] = sellDay
        finalResult[2] = highestPrice - lowestPrice

    return finalResult

    # return finalResult

S = [1, 2, 9, 4, 5, 6, 7, 10,]
print(findMaxProfit(S))
'''

# 最优解法 时间复杂度为O(n)
# 假定第i日买入，需要找出第i日后的最大值
# 假定第i日卖出，则需要找出i-11日前的最小值
# 循环则是range(len(S)),大小比较则需要反向
S = [1, 2, 9, 4, 5, 6, 7, 11, 10, 3]
maxPrice = S[-1]
buyDay = 0
sellDay = -1
maxProfit = 0
for i in range(-1,-len(S)-1,-1):
    if S[i] > maxPrice:
        maxPrice = S[i]
        sellDay = i
    if maxPrice - S[i] > maxProfit:
        maxProfit = maxPrice - S[i]
        buyDay = i
print(buyDay+len(S)+1, sellDay+len(S)+1, maxProfit)