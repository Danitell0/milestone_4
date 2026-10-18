#!/usr/bin/env python3

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    inter = set(lists[0])

    for lst in lists:
        if not lst:
            return []
        lst = set(lst)
        inter = inter.intersection(lst)

    return sorted(list(inter))


print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
# [2, 3]
print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
# [4]
print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
# [1, 2, 3]
print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
# []
print(list_intersection_finder([]))
# []
print(list_intersection_finder([[1, 2, 3], []]))
# []
print(list_intersection_finder([[5]]))
# [5]
