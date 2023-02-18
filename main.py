# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    bracket_dict = {'(': ')', '[': ']', '{': '}'}
    opening_brackets_stack = []
    for i, c in enumerate(text):
        if c in "([{":
            # Process opening bracket
            opening_brackets_stack.append(Bracket(c, i))

        if c in ")]}":
            # Process closing bracket
            if len(opening_brackets_stack) == 0:
                return i + 1

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, c):
                return i + 1

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[0].position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
