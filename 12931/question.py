import random

#Question Class
class Question:
    # createNaturalNumber Method
    # * 1 이상 100,000,001 미만의 정수 반환
    def createNaturalNumber(self):
        return random.randint(1, 100000001)
