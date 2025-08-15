s = "aacabdkacaa"
n = len(s)
dp = [[0] * n for _ in range(n)]

# Base case: single letters are palindromes of length 1
for i in range(n):
    dp[i][i] = 1

# Build the table
for length in range(2, n + 1):  # length of substring
    for i in range(n - length + 1):
        j = i + length - 1
        if s[i] == s[j]:
            if length == 2:
                dp[i][j] = 2
            else:
                dp[i][j] = 2 + dp[i + 1][j - 1]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

# Final answer
print(dp[0][n - 1])  # longest palindromic subsequence length
