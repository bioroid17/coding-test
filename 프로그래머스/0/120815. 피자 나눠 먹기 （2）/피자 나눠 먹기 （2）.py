def find_gcd(a, b):
    mod = a % b
    if mod == 0:
        return b
    else:
        return find_gcd(b, mod)

def solution(n):
    gcd = find_gcd(max(6, n), min(6, n))
    return n // gcd
    