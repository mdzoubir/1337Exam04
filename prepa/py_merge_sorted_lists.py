def merge_sorted_list(lists: list[list[int]]) -> list[int]:

    return sorted([i for li in lists for i in li])


print(merge_sorted_list([[1, 3, 5], [2, 4, 6]]))
print(merge_sorted_list([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
print(merge_sorted_list([[5], [1, 3], [2, 4]]))
print(merge_sorted_list([[1, 1, 2], [2, 3, 3]]))
print(merge_sorted_list([[], [1, 2, 3]]))
print(merge_sorted_list([[]]))
print(merge_sorted_list([[-5, -1, 0], [-3, 2, 4]]))
print(merge_sorted_list([[10], [10], [10]]))