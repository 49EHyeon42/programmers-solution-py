import unittest

def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    return answer / len(arr)

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution([1,2,3,4])
        self.assertEqual(answer, 2.5)

    def test_Method2(self):
        answer = solution([5,5])
        self.assertEqual(answer, 5)

if __name__ == '__main__':
    unittest.main()