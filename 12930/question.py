import string
import random

# Question Class
# * 프로그래머스 문제
class Question:
    # Constructor
    # TODO 단어의 최대 길이, 공백의 최대 길이, 문자열의 최대 길이 넣기
    def __init__(self, max_word_length, max_space_length, max_string_length):
        self.__MAX_WORD_LENGTH = max_word_length
        self.__MAX_SPACE_LENGTH = max_space_length
        self.__MAX_STRING_LENGTH = max_string_length

    # createWord Method
    # * 1개 이상, 단어의 최대 길이 미만의 단어 생성
    # * 문자열 반환
    def __createWord(self):
        answer = []
        for _ in range(random.randrange(1, self.__MAX_WORD_LENGTH)):
            answer.append(random.SystemRandom().choice(string.ascii_letters))
        return ''.join(answer)

    # createSpace Method
    # * 1개 이상, 단어의 최대 길이 미만의 공백 생성
    # * 문자열 반환
    def __createSpace(self):
        answer = []
        for _ in range(random.randrange(1, self.__MAX_SPACE_LENGTH)):
            answer.append(' ')
        return ''.join(answer)

    # createString Method
    # * 1개 이상, 문자열의 최대 길이 미만의 문자열 생성
    # * 문자열 반환
    def createString(self):
        answer = []
        for _ in range(random.randrange(1, self.__MAX_STRING_LENGTH)):
            answer.append(self.__createWord())
            answer.append(self.__createSpace())
        return ''.join(answer)