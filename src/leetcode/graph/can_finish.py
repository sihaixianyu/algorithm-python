import unittest
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for des, src in prerequisites:
            graph[src].append(des)

        on_path = set()
        visited = set()

        def dfs(src_node, path, visited):
            if src_node in path:
                return False
            if src_node in visited:
                return True

            path.add(src_node)
            visited.add(src_node)

            for des_node in graph[src_node]:
                if dfs(des_node, path, visited):
                    continue
                return False

            path.remove(src_node)
            return True

        for i in range(numCourses):
            if i in visited:
                continue
            if not dfs(i, on_path, visited):
                return False

        return True


class SolutionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_case_0(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        res = self.solution.canFinish(numCourses, prerequisites)
        self.assertEqual(res, True)

    def test_case_1(self):
        numCourses = 2
        prerequisites = [[1, 0], [0, 1]]
        res = self.solution.canFinish(numCourses, prerequisites)
        self.assertEqual(res, False)


if __name__ == "__main__":
    unittest.main()
