class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        L = len(energyDrinkA)
        if L == 0:
            return 0
        
        # Initialize DP arrays with 0 values
        dpA = [0] * (L + 1)
        dpB = [0] * (L + 1)
        
        # Start filling the DP table from the end
        for i in range(L - 1, -1, -1):
            dpA[i] = energyDrinkA[i] + max(dpA[i + 1], dpB[i + 2] if i + 2 < L else 0)
            dpB[i] = energyDrinkB[i] + max(dpB[i + 1], dpA[i + 2] if i + 2 < L else 0)
        
        # The result is the maximum value we can get starting from either A or B at index 0
        return max(dpA[0], dpB[0])

