def array_rotation_detector(arr1: list, arr2: list) -> bool:

    if len(arr1) != len(arr2):
        return False

    if not arr1 and not arr2:
        return True

    for _ in arr1:
        arr1= [arr1[-1]] + arr1[:-1]

        if arr1 == arr2:
            return True
    return False

print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))


        
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False

    if not arr1:
        return True
    l= list(arr1)+ list(arr2)
    for i in range(len(arr1)):
        if l[i:i+len(arr1)] == arr2:
            return True
    return False