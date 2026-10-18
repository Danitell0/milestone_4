#!/usr/bin/env python3

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    if not arr1 and not arr2:
        return True

    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True
    return False

print(array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
print(array_rotation_detector([1, 2], [1, 2, 3]))
print(array_rotation_detector([], []))
