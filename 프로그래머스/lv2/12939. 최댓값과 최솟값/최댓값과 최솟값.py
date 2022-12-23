def solution(s):
#     # 문자열을 숫자 목록으로 분할
#     numbers = s.split()
    
#     # 목록의 요소를 정수로 변환
#     numbers = [int(x) for x in numbers]
    numbers = list(map(int,s.split()))
    
    # 최소값과 최대값 찾기
    min_val = min(numbers)
    max_val = max(numbers)
    
    # 최소값과 최대값을 문자열로 반환
    return f"{min_val} {max_val}"

    

