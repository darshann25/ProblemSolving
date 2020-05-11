# Review the following link for the question prompt: https://www.algoexpert.io/questions/Three%20Number%20Sum

# Solution 1 - Brute Force
# Time Complexity - O(n^3)
# Space Complexity - O(1)

# Solution 2 - Sort values and iterate
# Time Complexity - O(n^2)
# Space Complexity - O(n)
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    results = []

    for i in range(len(array) - 2):
        l = i + 1
        r = len(array) - 1

        while l < r:
            total = array[i] + array[l] + array[r]
            result = [array[i], array[l], array[r]]

            if total > targetSum:
                r -= 1
            elif total < targetSum:
                l += 1
            else: # total == targetSum
                results.append(result)
                l += 1
                r -= 1

    return results
