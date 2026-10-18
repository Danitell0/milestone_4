#!/usr/bin/env python3

def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    network = [["." for _ in range(dim)]for _ in range(dim)]

    for space, star in stars:
        if 0 <= space < dim and 0 <= star < dim:
            network[space][star] = '*'

    return ["".join(i) for i in network]

print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
# ['*..', '.*.', '..*']
print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
#['.*.', '***', '.*.']
print(constellation_mapper([], 2))
# ['..', '..']
print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
# ['*.', '.*']
print(constellation_mapper([(0, 0), (5, 5)], 3))
# ['*..', '...', '...']
print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))
# ['...', '***', '...']
