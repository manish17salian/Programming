class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumGas = sum(gas)
        sumCost = sum(cost)

        if sumGas < sumCost:
            return -1
        
        currGas = 0
        start = 0
        for i in range(len(gas)):
            currGas += gas[i] - cost[i]
            
            if currGas < 0:
                start = i + 1
                currGas = 0
        
        return start

        

        