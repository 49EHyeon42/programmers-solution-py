import unittest
from math import gcd

def solution(n, m):
    answer = []     
    value = gcd(n, m)
    answer.append(value)
    answer.append(n*m / value)
    return answer

class SolutionTest(unittest.TestCase):
    def test_Method1(self):
        answer = solution(3, 12)
        self.assertEqual(answer, [3, 12])

    def test_Method2(self):
        answer = solution(2, 5)
        self.assertEqual(answer, [1, 10])

    # TestCase.assert 메소드
    # 1) assertEqual(A, B, Msg) - A, B가 같은지 테스트
    # 2) assertNotEqual(A, B, Msg) - A, B가 다른지 테스트
    # 3) assertTrue(A, Msg) - A가 True인지 테스트
    # 4) assertFalse(A, Msg) - A가 False인지 테스트
    # 5) assertIs(A, B, Msg) - A, B가 동일한 객체인지 테스트
    # 6) assertIsNot(A, B, Msg) - A, B가 동일하지 않는 객체인지 테스트
    # 7) assertIsNone(A, Msg) - A가 None인지 테스트
    # 8) assertIsNotNone(A, Msg) - A가 Not None인지 테스트
    # 9) assertRaises(ZeroDivisionError, myCalc.add, 4, 0) - 특정 에러 확인

    # TestCase 메소드
    # 1) setUp() - TestCase클래스의 매 테스트 메소드가 실행 전 동작
    # 2) tearDown() - 매 테스트 메소드가 실행 후 동작

    # 실행 명령어
    # python -m unittest discover [option]
    # 1. -v : 상세 결과
    # 2. -f : 첫 번째 실패 또는 오류시 중단
    # 3. -s : 시작할 디렉토리
    # 4. -p : 테스트 파일과 일치하는 패턴
    # 5. -t : 프로젝트의 최상위 디렉토리

if __name__ == '__main__':
    # Obey the Python coding convention provided in PEP8
    unittest.main()

# reference
# link : https://www.python.org/dev/peps/pep-0008/
# lknk : http://labs.brandi.co.kr/2018/06/07/kwakjs.html