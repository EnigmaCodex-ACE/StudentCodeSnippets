# Easy

# https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self, text='', isWord=False):
        self.text = text
        self.children = {}
        self.isWord = isWord

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_node(self, text):
        curr = self.root
        prefix = ''
        for letter in text:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            else:
                prefix += letter
            curr = curr.children[letter]
        curr.isWord = True
        return prefix
    
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 1:
            import math
            root = Trie()
            common_prefix = [root.add_node(string) for string in strs]
            # print(common_prefix)
            mini = math.inf
            out = ''
            for i in range(1, len(common_prefix)):
                if common_prefix[i] == '':
                    return ''
                elif len(common_prefix[i]) < mini:
                    mini = len(common_prefix[i])
                    out = common_prefix[i]
            return out
        elif len(strs) == 1:
            return strs[0]
        return ''     