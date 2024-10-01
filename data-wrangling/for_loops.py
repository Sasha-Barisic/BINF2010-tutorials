"""
Simple examples of a for loop.

Usage:
    python3 data-wrangling/for_loops.py
    python3 for_loops.py

Author:
    Sasha Barisic

Date:
    01/10/2024
"""

dna = "AACTTGGTTAAATTATGGG"
dna_comp = "TTGAACCAATTTAATACCC"


def for_loop_simple() -> None:
    """
    Demonstrates a simple for loop.
    """

    # Define list of numbers
    num_list = list(range(10))
    print("num_list = ", num_list)

    # Print these numbers one by one
    for n in num_list:
        print("->", n)


def for_loop_string() -> None:
    """
    Demonstrates a for loop over a string.
    """

    for x in dna:
        print("->", x)


def for_loop_list() -> None:
    """
    Demonstrates populating a list using a for loop.
    """

    # Code A
    dna_list = []
    for c in dna:
        dna_list.append(c)
    print("dna_list =", dna_list)

    # Code B - pythonic way
    simple_list = [c for c in dna]
    print("simple_list = ", simple_list)


def for_loop_index() -> None:
    """
    Demonstrates a for loop over a list and accessing its index values.
    """
    # Code A
    i = 0
    for c in dna:
        print("dna[%d] = %s" % (i, c))
        i += 1

    # Code B - pythonic way
    for i, c in enumerate(dna):
        print("dna[%d] = %s" % (i, c))


def for_loop_two_lists() -> None:
    """
    Demonstrates a for loop over two lists at the same time.
    """

    for forward, reverse in zip(dna, dna_comp):
        print(forward, "-", reverse)


def for_loop_range() -> None:
    """
    Demonstrates a for loop over a range.
    """
    for x in range(10):
        print(x)


def for_loop_dict() -> None:
    """
    Demonstrates a for loop over a dictionary.
    """

    exmaple_dict = {"apples": 2, "bread": 1, "mango": 3}

    for key, value in exmaple_dict.items():
        print(f"I need to buy {value} {key}")


if __name__ == "__main__":
    # for_loop_simple()
    # for_loop_string()
    # for_loop_range()
    # for_loop_list()
    # for_loop_index()
    for_loop_dict()
    # for_loop_two_lists()
