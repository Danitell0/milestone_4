#!/usr/bin/env python3

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    new_list = []
    for lst in lists:
        new_list.extend(lst)
    n = len(new_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if new_list[j] > new_list[j + 1]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
                swapped = True
        if not swapped:
            break
    return new_list

print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
# [1, 2, 3, 4, 5, 6]
print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(merge_sorted_lists([[5], [1, 3], [2, 4]]))
# [1, 2, 3, 4, 5]
print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))
# [1, 1, 2, 2, 3, 3]
print(merge_sorted_lists([[], [1, 2, 3]]))
# [1, 2, 3]
print(merge_sorted_lists([[]]))
# []
print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))
# [-5, -3, -1, 0, 2, 4]
print(merge_sorted_lists([[10], [10], [10]]))
# [10, 10, 10]
