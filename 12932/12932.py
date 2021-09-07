import unittest

def solution(n):
    answer = []
    while n>0:
        answer.append(n%10)
        n //= 10
    return answer

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution(12345)
        self.assertEqual(answer, [5,4,3,2,1])

if __name__ == '__main__':
    unittest.main()