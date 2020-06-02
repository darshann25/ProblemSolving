# Review the following link for the question prompt: https://leetcode.com/problems/compare-version-numbers/

# O(N) time | O(N) space
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1List = [int(x) for x in version1.split('.')]
        v2List = [int(x) for x in version2.split('.')]
        
        if len(v1List) < len(v2List):
            v1List = v1List + [0 for x in range(len(v2List) - len(v1List))]
        elif len(v1List) > len(v2List):
            v2List = v2List + [0 for x in range(len(v1List) - len(v2List))]
            
        for i in range(len(v1List)):
            if v1List[i] > v2List[i]:
                return 1
            elif v1List[i] < v2List[i]:
                return -1
        
        return 0