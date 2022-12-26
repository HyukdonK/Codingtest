def solution(hp):
    general = hp // 5
    soldier = (hp-(5*general))//3
    normal = (hp-(5*general)-(3*soldier))//1
    
    return general + soldier + normal

# def solution(hp):
#     answer = 0
#     for ant in [5, 3, 1]:
#         d, hp = divmod(hp, ant)
#         answer += d
#     return answer
