class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        inorder = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            inorder[crs] += 1
            graph[pre].append(crs)

        q = deque()
        for n in range(numCourses):
            if inorder[n] == 0:
                q.append(n)

        finish = 0

        res = []
        while q:
            node = q.popleft()
            finish += 1
            res.append(node)

            for nei in graph[node]:
                inorder[nei] -= 1

                if inorder[nei] == 0:
                    q.append(nei)

        return res if finish == numCourses else []