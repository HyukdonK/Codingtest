def solution(my_string):
    vowels = "aeiouAEIOU"  # 모음을 담은 문자열
    answer = ""  # 최종 결과를 담을 문자열
    for char in my_string:  # my_string의 각 글자를 순회합니다.
        if char not in vowels:  # 글자가 모음이 아닌 경우
            answer += char  # 결과 문자열에 추가합니다.
    return answer  # 결과 문자열을 반환합니다.
