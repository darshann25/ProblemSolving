"""
  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.

  You can assume that there will only be one pair of numbers with the smallest
  difference.
"""
# Solution 1 - Sort both arrays and iterate
# O(nlog(n)) + O(mlog(m)) time | O(!) space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    smallest = []
    smallestDiff = 9223372036854775807

    a1 = 0
    a2 = 0

    while a1 < len(arrayOne) and a2 < len(arrayTwo):
        diff = arrayOne[a1] - arrayTwo[a2]
        values = [arrayOne[a1], arrayTwo[a2]]

        if abs(diff) < smallestDiff:
            smallestDiff = abs(diff)
            smallest = values

        if diff < 0:
            a1 += 1
        elif diff > 0:
            a2 += 1
        else: # diff == 0
            break

    return smallest

