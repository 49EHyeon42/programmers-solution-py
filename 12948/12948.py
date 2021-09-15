# TODO: 정규식
def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]