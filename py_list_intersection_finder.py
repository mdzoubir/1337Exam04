def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    mp = {}
    result = []
    le = len(lists)
    for l in lists:
        for i in set(l):
            mp[i] = mp.get(i, 0) + 1
            if mp[i] == le:
                result.append(i)
    return result

print(
    list_intersection_finder([[1, 2, 3, 4], [2, 3, 4, 4, 5], [2, 3, 5]]),
    list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]),
    list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]),
    list_intersection_finder([[1, 2, 3], [4, 5, 6]]),
    list_intersection_finder([[5]]),
    list_intersection_finder([[1, 2, 3], []]),
)
