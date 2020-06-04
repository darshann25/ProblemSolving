# Review the following link for the question prompt: https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor

# O(d) time | O(n) time
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthOne = getDescendentDepth(descendantOne, topAncestor)
    depthTwo = getDescendentDepth(descendantTwo, topAncestor)

    if depthOne > depthTwo:
        return backtrackAncestralTree(descendantOne, descendantTwo, depthOne-depthTwo)
    else:
        return backtrackAncestralTree(descendantTwo, descendantOne, depthTwo-depthOne)

def getDescendentDepth(descendant, topAncestor):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor
    return depth

def backtrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return higherDescendant
