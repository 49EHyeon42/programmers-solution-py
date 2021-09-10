import unittest

def solution(n):
    count = 0
    while count < 500:
        if n == 1:
            return count
        else:
            if n%2 == 0: n /= 2
            else: n = n*3 + 1
        count += 1
    return -1

# def solution(n):
#     for i in range(0, 500):
#         if n == 1:
#             return i
#         else:
#             n = n / 2 if n % 2 == 0 else n*3 + 1
#     return -1

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution(6)
        self.assertEqual(answer, 8)

    def test_Method2(self):
        answer = solution(16)
        self.assertEqual(answer, 4)
    
    def test_Method2(self):
        answer = solution(626331)
        self.assertEqual(answer, -1)

if __name__ == '__main__':
    unittest.main()