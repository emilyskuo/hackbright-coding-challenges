"""
Write a function that prints a string, fitting its characters within char
limit.

It should take in a string and a character limit (as an integer). It should
print the contents of the string without going over the character limit
and without breaking words. For example:

>>> fit_to_width('hi there', 50)
hi there

Spaces count as characters, but you do not need to include trailing whitespace
in your output:

>>> fit_to_width('Hello, world! I love Python and Hackbright',
...              10)
...
Hello,
world! I
love
Python and
Hackbright

Your test input will never include a character limit that is smaller than
the longest continuous sequence of non-whitespace characters:

>>> fit_to_width('one two three', 8)
one two
three
"""


def fit_to_width(string, limit):
    """Print string within a character limit."""

    line = ""

    for char in string:
        if 

    # split_string = string.split(" ")

    # for word in split_string:
    #     line = ""
    #     if len(line) < limit and len((line + " " + word)) < limit:
    #         line = line + " " + word
    #     else:
    #         print(line)
    #         line = ""



    # def create_line(line, split_string):
    #     while len(line) <= limit:
    #         i = 0
    #         word = split_string[i]
    #         if len(line + word) <= limit:
    #             split_string.pop(i)
    #             line = line + word + " "
    #         if i < len(split_string):
    #             i += 1
    #     print(line)
    #     if split_string:
    #         create_line("", split_string)

    # create_line("", split_string)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')
