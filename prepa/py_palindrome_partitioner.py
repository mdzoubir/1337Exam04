def palindrome_partitioner(s: str) -> int:
    if len(s) <= 1 or s == s[::-1]:
        return 0
    dp = [i for i in range(len(s))]
    for i in range(1, len(s)):
        for j in range(i + 1):
            tmp = s[j:i + 1]
            if tmp == tmp[::-1]:
                dp[i] = min(dp[i], dp[j - 1] + 1 if j else 0)
    return dp[-1]

print(palindrome_partitioner("aab"))
print(palindrome_partitioner("aba"))
print(palindrome_partitioner("abc"))
