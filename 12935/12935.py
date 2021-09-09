import unittest

def solution(arr):
    arr.remove(min(arr))
    if not arr: arr.append(-1)
    return arr

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution([4, 3, 2, 1])
        self.assertEqual(answer, [4, 3, 2])

    def test_Method2(self):
        answer = solution([10])
        self.assertEqual(answer, [-1])

if __name__ == '__main__':
    unittest.main()