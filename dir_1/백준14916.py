N = int(input())

coins = [2, 5]

dp = [-1 for i in range(N+1)]

for coin in coins:
    if coin <= N:
        dp[coin] = 1

for i in range(N):
    if dp[i] == -1:
        continue

    for coin in coins:
        if i+coin <= N:
            if dp[i+coin] == -1:
                dp[i+coin] = dp[i]+1
            else:
                dp[i+coin] = min(dp[i]+1, dp[i+coin])

print(dp[N])