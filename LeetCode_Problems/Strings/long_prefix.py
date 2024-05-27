
from typing import List
"""
 Question: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # HELP ME GOD.
        if not strs or len(strs) <= 0:
            return ""
        
        prefix = ""
        
        for i in range(len(strs[0])):
            for val in strs:
                if i >= len(val) or val[i] != strs[0][i]:
                    return prefix
                
            prefix += strs[0][i]
            
        return prefix 

value = ["flower","flow","floight"]
model = Solution()
result = model.longestCommonPrefix(value)
print(result)
