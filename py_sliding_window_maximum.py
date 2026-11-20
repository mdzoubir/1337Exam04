def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0 or k > len(nums):
        return []
    dq = []
    res = []
    for i, n in enumerate(nums):
        while dq and nums[dq[-1]] <= n:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.pop(0)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res



print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Expected: [3, 3, 5, 5, 6, 7]
print(sliding_window_maximum([1, 2, 3, 4, 5], 2))  # Expected: [2, 3, 4, 5]
print(sliding_window_maximum([5, 4, 3, 2, 1], 1))  # Expected: [5, 4, 3, 2, 1]
print(sliding_window_maximum([1, 2, 3], 3))  # Expected: [3]
print(sliding_window_maximum([1, 2, 3], 4))  # Expected: []
print(sliding_window_maximum([], 2))  # Expected: []
print(sliding_window_maximum([1, 2, 3], 0))  # Expected: []
