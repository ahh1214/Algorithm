def solution(phone_book): #전화번호부에 적힌 번호 담긴 배열
    
    a = sorted(phone_book)
    
    for p1, p2 in zip(a, a[1:]):
        if p2.startswith(p1):
            return False
    
    return True