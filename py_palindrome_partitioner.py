def palindrome_partitioner(s: str) -> int:
    n = len(s)
    cut = [i - 1 for i in range(n + 1)]
    for c in range(n):
        l, r = c, c
        while l >= 0 and r < n and s[l] == s[r]:
            cut[r + 1] = min(cut[r + 1], cut[l] + 1)
            l -= 1
            r += 1
        l, r = c, c + 1
        while l >= 0 and r < n and s[l] == s[r]:
            cut[r + 1] = min(cut[r + 1], cut[l] + 1)
            l -= 1
            r += 1
    return cut[n]
