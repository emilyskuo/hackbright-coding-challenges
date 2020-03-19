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

    print(list_mid_y)
    print(list_mid_x)

    # Find the midpoint with the most carrots

    start_x = 0
    start_y = 0
    start_carrots = 0

    # If only one possible midpoint, set starting points and starting carrots
    if len(list_mid_x) == 1 and len(list_mid_y) == 1:
        start_x = list_mid_x[0]
        start_y = list_mid_y[0]
        start_carrots = garden[start_x][start_y]

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

    print(start_y)
    print(start_x)
    print(start_carrots)



if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
