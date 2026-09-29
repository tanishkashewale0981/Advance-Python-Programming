n = int(input("Enter N: "))

if n <= 0:
    print("Enter a positive number")
else:
    dp = [0] * n

    dp[0] = 0

    if n > 1:
        dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    print("Fibonacci sequence:")
    print(dp)