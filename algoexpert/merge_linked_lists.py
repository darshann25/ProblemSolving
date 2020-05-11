# Review the following link for the question prompt: https://www.algoexpert.io/questions/Merge%20Linked%20Lists

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(N) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    
	headResult = LinkedList(-1)
	currResult = headResult
	
	while headOne or headTwo:
		if headOne is None:
			currResult.next = headTwo
			break
		if headTwo is None:
			currResult.next = headOne
			break
		
		if headOne.value <= headTwo.value:
			currResult.next = headOne
			headOne = headOne.next
		else:
			currResult.next = headTwo
			headTwo = headTwo.next
		
		currResult = currResult.next
		currResult.next = None
	
	return headResult.next
