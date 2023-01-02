def solution(cipher: str, code: int) -> str:
    # 암호를 저장할 문자열 생성
    decrypted = ""

    # 암호화된 문자열을 통해 이동
    for i in range(len(cipher)):
        # 인덱스가 코드의 배수이면 복호화된 암호열에 해당 문자를 추가
        if (i+1) % code == 0:
            decrypted += cipher[i]

    # Return the decrypted cipher string
    return decrypted


#def solution(cipher, code):

    #return cipher[code-1::code]