# Medium
# https://leetcode.com/problems/course-schedule/

# Time Complexity: O(V + E)
# Space Complexity: O(V)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(adj, used, explored, x):
            explored[x] = True
            used[x] = True
            for w in adj[x]:
                if used[w]:
                    return "cycle"
                else:
                    if dfs(adj, used, explored, w):
                        return "cycle"
                    used[w] = False
            used[x] = False                  

        
        def acyclic(adj):
            explored = [False for _ in range(numCourses)] 
            visited = [False for _ in range(numCourses)]
            for i in range(len(explored)):
                if not explored[i]:
                    if dfs(adj, visited, explored, i) == 'cycle':
                        return False
            return True
        
        adj = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adj[a].append(b)
        return acyclic(adj)