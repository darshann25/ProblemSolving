"""
  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.
  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.
"""

# Solution 1 - Pop and Append while maintaining index
# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    index = 0
    iteration = 0

    while iteration < len(array):
        element = array[index]
        if element == toMove:
            array.append(array.pop(index))
            index -= 1

        iteration += 1
        index += 1

    return array
