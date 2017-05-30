"""
This mission is simple to solve. You are given a function called "i_love_python" which will only return the phrase - "I love Python!"

Let's write an essay in python code which will explain why you love python (if you don't love it, when we will make an additional mission special for the haters). Publishing the default solution will only earn you 0 points as the goal is to earn points through votes for your code essay.

Input: Nothing.

Output: The string "I love Python!".

Example:

i_love_python() == "I love Python!"
    
How it is used: This mission revolves around code literacy.
"""

def i_love_python():
    """
        Let's explain why do we love Python.
    """
    return "I love Python!"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
