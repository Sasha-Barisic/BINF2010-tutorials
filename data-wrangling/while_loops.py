"""
Simple examples of a while loop.

Usage:
    python3 data-wrangling/while_loops.py
    python3 while_loops.py

Author:
    Sasha Barisic

Date:
    01/10/2024
"""


def while_loop_simple() -> None:
    """
    Demonstrates a simple while loop.
    """
    i = 1
    n = 10
    while i < n:
        print(i)
        i += 1


def while_loop_break() -> None:
    """
    Demonstrates a while loop with the break statement.
    """
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1


def while_loop_continue() -> None:
    """
    Demonstrates a while loop with the continue statement.
    """
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)


def while_loop_else() -> None:
    """
    Demonstrates a while loop with the else code block.
    """
    i = 1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")


if __name__ == "__main__":
    # while_loop_simple()
    # while_loop_break()
    # while_loop_continue()
    while_loop_else()
