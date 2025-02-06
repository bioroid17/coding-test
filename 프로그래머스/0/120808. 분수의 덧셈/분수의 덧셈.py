def find_gcd(answer):
    mod = answer[1] % answer[0]
    if mod == 0:
        return answer[0]
    else:
        return find_gcd([mod, answer[0]])
    

def solution(numer1, denom1, numer2, denom2):
    answer = [numer1 * denom2 + numer2 * denom1, denom1 * denom2]
    sorted_answer = sorted(answer)
    gcd = find_gcd(sorted_answer)
    answer[1] //= gcd
    answer[0] //= gcd
    
    return answer