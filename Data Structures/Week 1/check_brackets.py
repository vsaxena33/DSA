# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        elif next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1  # Unmatched closing bracket
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i + 1  # Mismatched closing bracket
            
    if opening_brackets_stack:
        return opening_brackets_stack[0].position + 1  # First unmatched opening
    
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
