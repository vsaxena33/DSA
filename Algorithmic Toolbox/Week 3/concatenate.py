from functools import cmp_to_key

# Custom comparator: sort by which combination forms the larger number
def compare(a, b):
    if a + b > b + a:
        return -1  # a should come before b
    elif a + b < b + a:
        return 1   # b should come before a
    else:
        return 0   # equal

def largest_concatenate(nums):
    nums.sort(key=cmp_to_key(compare))
    result = ''.join(nums)
    return result if result[0] != '0' else '0'

# Input Reading
n = int(input())
nums = input().split()
print(largest_concatenate(nums))
