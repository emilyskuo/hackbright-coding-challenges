"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""

    """
    find the overlap with the most amount of authors

    if there's overlap, update the range and count # of authors

    """
    start_date = bio_data[0][1]
    end_date = bio_data[0][2]
    num_authors = 1

    for author in bio_data:
        if author[1] > start_date and author[1] < end_date:
            start_date = author[1]
            num_authors += 1
            if author[2] < end_date:
                end_date = author[2]
        elif author[1] < end_date and author[2] < end_date:
            num_authors += 1
            end_date = author[2]

    return (start_date, end_date)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")