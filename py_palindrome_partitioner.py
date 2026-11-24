def palindrome_partitioner(s: str) -> int:
    # n = len(s)
    # cut = [i - 1 for i in range(n + 1)]
    # for c in range(n):
    #     l, r = c, c
    #     while l >= 0 and r < n and s[l] == s[r]:
    #         cut[r + 1] = min(cut[r + 1], cut[l] + 1)
    #         l -= 1
    #         r += 1
    #     l, r = c, c + 1
    #     while l >= 0 and r < n and s[l] == s[r]:
    #         cut[r + 1] = min(cut[r + 1], cut[l] + 1)
    #         l -= 1
    #         r += 1
    # return cut[n]
    if len(s) <= 0 or s == s[::-1]:
        return 0
    dp = [i for i in range(len(s))]
    for i in range(1, len(s)):
        for j in range(i + 1):
            part = s[j:i+1]
            if part == part[::-1]:
                dp[i] = min(dp[i], dp[j - 1] + 1 if j else 0)
    return dp[-1]

print(palindrome_partitioner("aab"))  # Expected: 1
print(palindrome_partitioner("aba"))  # Expected: 0
print(palindrome_partitioner("abc"))  # Expected: 2