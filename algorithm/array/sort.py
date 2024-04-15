import unittest
from typing import List


def insert_sort(nums: List[int]) -> List[int]:
    ans = list(nums)  # using nums[:] should be equivalent

    for i in range(1, len(nums)):
        temp = ans[i]
        j = i
        while j > 0:
            if ans[j - 1] <= temp:
                break
            ans[j], j = ans[j - 1], j - 1
        ans[j] = temp

    return ans


class TestSort(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

        self.input_1 = [1, 2, 3, 4]
        self.expected_1 = [1, 2, 3, 4]

        self.input_2 = [4, 3, 2, 1]
        self.expected_2 = [1, 2, 3, 4]

        self.input_3 = [5, 2, 3, 1, 4]
        self.input_3 = [1, 2, 3, 4, 5]

    def test_ok_insert_sort(self):
        ans = insert_sort(self.input_1)
        self.assertEqual(ans, self.expected_1)

        ans = insert_sort(self.input_1)
        self.assertEqual(ans, self.expected_1)

        ans = insert_sort(self.input_1)
        self.assertEqual(ans, self.expected_1)


if __name__ == "__main__":
    unittest.main()
