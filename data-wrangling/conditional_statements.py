"""
Simple example of a conditional statement.

Usage:
    python3 data-wrangling/conditional_statements.py
    python3 conditional_statements.py

Author:
    Sasha Barisic

Date:
    01/10/2024
"""

HD = 85.0
DN = 75.0
CR = 65.0
PS = 50.0


def grade_assignment(mark: float) -> str:
    """Determines the final mark based on input argument.

    Args:
        mark (float): A float representing the mark from a student.

    Returns:
        str: A written statement of the final mark.
    """

    if mark < PS:
        return "Unsatisfactory performance, below the minimum expected level."
    elif mark >= PS and mark < CR:
        return "An acceptable level of performance."
    elif mark >= CR and mark < DN:
        return "A good performance."
    elif mark >= DN and mark < HD:
        return "A superior performance."
    else:
        return "An outstanding performance."


if __name__ == "__main__":
    # print(grade_assignment(49.9))
    print(grade_assignment(57.7))
    print(grade_assignment(65.0))
    print(grade_assignment(82.3))
    print(grade_assignment(95))
