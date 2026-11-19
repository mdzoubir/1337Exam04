def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1:
        return True
    l = list(arr1) + list(arr1)
    print(l)
    n = len(arr1)
    for i in range(n):
        if l[i:i+n] == arr2:
            return True
    return False



print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))  # Expected: True
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))  # Expected: True
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))  # Expected: False
print(array_rotation_detector([1, 2], [1, 2, 3]))  # Expected: False
print(array_rotation_detector([], []))  # Expected: True