# Medium
# https://leetcode.com/problems/is-graph-bipartite/

# Time Complexity: O(V + E)
# Space Complexity; O(V) 
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        import queue
        def bfs(adj, s, visited, color):
            visited[s] = True
            q = queue.Queue()
            q.put(s)
            color[s] = 1
            while q.qsize() > 0:
                start = q.get()
                for w in adj[start]:
                    if not visited[w]:
                        q.put(w)
                        visited[w] = True
                        color[w] = 0 if color[start] else 1

        visited = [False for _ in range(len(graph))]
        color = [None for _ in range(len(graph))]
        for i in range(len(graph)):
            if not visited[i]:
                bfs(graph, i, visited, color)
                
        for i in range(len(graph)):
            for j in graph[i]:
                if color[i] == color[j]:
                    return 0
        return 1