def solution(num, k):
    num = str(num)
    for i, n in enumerate(num):
        if int(n) == k:
            return i+1
    return -1
