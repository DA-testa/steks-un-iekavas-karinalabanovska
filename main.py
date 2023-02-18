# python3

from collections import namedtuple

# Define a named tuple to represent brackets
Bracket = namedtuple("Bracket", ["char", "position"])

# Define a function to check if two brackets match
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

# Define the main function to find and return the first mismatched bracket
def find_mismatch(text):
    # Create a dictionary to map opening brackets to their corresponding closing brackets
    bracket_dict = {'(': ')', '[': ']', '{': '}'}
    # Create a stack to keep track of opening brackets
    opening_brackets_stack = []
    # Loop through each character in the text
    for i, c in enumerate(text):
        # If the character is an opening bracket, add it to the stack
        if c in "([{":
            opening_brackets_stack.append(Bracket(c, i))
        # If the character is a closing bracket, check if it matches the last opening bracket on the stack
        elif c in ")]}":
            # If there are no opening brackets on the stack, return the index of the closing bracket as the first mismatch
            if len(opening_brackets_stack) == 0:
                return i + 1
            # Otherwise, pop the top opening bracket from the stack and check if it matches the closing bracket
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, c):
                return i + 1
    # If there are no mismatches in the closing brackets, check for the first unmatched opening bracket
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[0].position + 1

# Define the main function to take user input and call the find_mismatch function
def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

# Call the main function if this script is being run directly
if __name__ == "__main__":
    main()
