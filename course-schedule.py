# There are a total of n courses you have to take, labeled from 0 to n-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Example 1:

# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
# Note:

# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        #build adj list
        adjList = {}
        visited = set()
        curSet = set()
        def DFS(job):
            if job in curSet:
                return False
            elif job in visited:
                pass
            else:
                curSet.add(job)
                visited.add(job)
                if job in adjList:
                    for dependency in adjList[job]:
                        noCycle_DFS = DFS(dependency)
                        if noCycle_DFS is False:
                            return False
                curSet.remove(job)
            return True

        for dep in prerequisites:
            if dep[0] in adjList:
                adjList[dep[0]].append(dep[1])
            else:
                adjList[dep[0]] = [dep[1]]
        for job in range(numCourses):
            if job in adjList:
                noCycle = DFS(job)
                if not noCycle:
                    return False
            elif job not in visited:
                visited.add(job)
        
        return True