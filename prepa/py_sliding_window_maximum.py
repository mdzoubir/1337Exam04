def sliding_window_maximum(nums: list[int], k: int) -> list[int]:

    if not nums or k >len(nums) or k <=0:
        return []

    c = k 
    out = []
    for i in range(len(nums) - k +1):

        out.append(max(nums[i:c]))

        c += 1
    return out


print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sliding_window_maximum([1, 2, 3, 4, 5], 2))
print(sliding_window_maximum([5, 4, 3, 2, 1], 1))
print(sliding_window_maximum([1, 2, 3], 3))
