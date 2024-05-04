def knapsack_greedy(N, W, knapsack):
    # Calculate value-to-weight ratios for all items
    # v - w
    ratios = [(knapsack[i][0] / knapsack[i][1], i) for i in range(N)]
    ratios.sort(reverse=True)
 
    total_value = 0
    total_weight = 0
 
    for ratio, item in ratios:
        if total_weight + knapsack[item][1] <= W:
            total_value += knapsack[item][0]
            total_weight += knapsack[item][1]
 
    return total_value

def knapsack_dynamic(N, W, knapsack):
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
 
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if knapsack[i-1][1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(knapsack[i-1][0] + dp[i-1]
                               [j-knapsack[i-1][1]], dp[i-1][j])
 
    return dp[N][W]