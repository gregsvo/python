"""
You are given a non-empty list of integers (X). For this task, you should return a list 
consisting of only the non-unique elements in this list. To do so you will need to remove 
all unique elements (elements which are contained in a given list only once). When solving 
this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique 
elements and result will be [1, 3, 1, 3].

Input: A list of integers.

Output: The list of integers.

Example:

checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
checkio([1, 2, 3, 4, 5]) == []
checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]

How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).

Precondition:
0 < len(data) < 1000
"""

def checkio(data):
    repeated_items = []
    for item in data:
            if data.count(item) > 1:
                repeated_items.append(item)
    return repeated_items

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")