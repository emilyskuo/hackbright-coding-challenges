"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    # Get number of rows and columns

    nrows = len(garden)
    ncols = len(garden[0])

    list_mid_y = []
    list_mid_x = []

    # Check midpoint for rows and cols

    if nrows % 2 != 0:
        list_mid_y.append(nrows // 2)
    else:
        list_mid_y.append((nrows // 2) - 1)
        list_mid_y.append(nrows // 2)

    if ncols % 2 != 0:
        list_mid_x.append(ncols // 2)
    else:
        list_mid_x.append((ncols // 2) - 1)
        list_mid_x.append(ncols // 2)

    # Find the midpoint with the most carrots

    start_x = 0
    start_y = 0
    start_carrots = 0

    # If only one possible midpoint, set starting points and starting carrots
    if len(list_mid_x) == 1 and len(list_mid_y) == 1:
        start_x = list_mid_x[0]
        start_y = list_mid_y[0]
        start_carrots = garden[start_y][start_x]

    # Find start if there's only one possible x start,
    # but multiple y starting points
    elif len(list_mid_x) == 1:
        start_x = list_mid_x[0]
        for y in list_mid_y:
            carrots = garden[y][start_x]
            if carrots > start_carrots:
                start_carrots = carrots
                start_y = y

    # Find start if there's only one possible y start,
    # but multiple x starting points
    elif len(list_mid_y) == 1:
        start_y = list_mid_y[0]
        for x in list_mid_x:
            carrots = garden[start_y][x]
            if carrots > start_carrots:
                start_carrots = carrots
                start_x = x

    # Find start if multiple x and y starting points
    else:
        for y in list_mid_y:
            for x in list_mid_x:
                carrots = garden[y][x]
                if carrots == 0:
                    return 0
                if carrots > start_carrots:
                    start_carrots = carrots
                    start_x = x
                    start_y = y

    # Leveret looks WNES and chooses the spot with the most carrots

    next_carrots = start_carrots
    total_carrots = 0
    current_x = start_x
    current_y = start_y
    next_x = 0
    next_y = 0

    while next_carrots > 0:
        # Add carrots to total carrot count, zero out carrots in garden spot,
        # reset next carrots to 0
        total_carrots += next_carrots
        garden[current_y][current_x] = 0
        next_carrots = 0

        # Find next spot to eat carrots from

        # Check west cell - assume this will be the next move unless NES have
        # more carrots
        if current_x >= 1:
            next_x = current_x - 1
            next_y = current_y
            next_carrots = garden[next_y][next_x]
        # Check north cell, compare to west (aka next)
        if current_y >= 1:
            north_x = current_x
            north_y = current_y - 1
            north_carrots = garden[north_y][north_x]
            if north_carrots > next_carrots:
                next_carrots = north_carrots
                next_x = north_x
                next_y = north_y
        # Check east cell, compare to next
        if current_x < ncols - 1:
            east_x = current_x + 1
            east_y = current_y
            east_carrots = garden[east_y][east_x]
            if east_carrots > next_carrots:
                next_carrots = east_carrots
                next_x = east_x
                next_y = east_y
        # Check south cell, compare to next
        if current_y < nrows - 1:
            south_x = current_x
            south_y = current_y + 1
            south_carrots = garden[south_y][south_x]
            if south_carrots > next_carrots:
                next_carrots = south_carrots
                next_x = south_x
                next_y = south_y
        # Leveret moves into next cell
        current_x = next_x
        current_y = next_y

    return total_carrots


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
