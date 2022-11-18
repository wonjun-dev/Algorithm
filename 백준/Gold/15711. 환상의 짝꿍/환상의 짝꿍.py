import sys

T = int(sys.stdin.readline())

def get_primes(N):
    nums = [True for _ in range(N+1)]
    nums[0], nums[1] = False, False
    primes = []
    for i in range(1, N+1):
        if nums[i]:
            primes.append(i)
            for j in range(i*i, N+1, i):
                nums[j] = False
    return primes, nums

primes, is_prime = get_primes(int(2*1e6))

def check_prime(N):
    if N > 2*1e6:
        for p in primes:
            if p > N:
                break
            elif N % p == 0:
                return False
        return True
    else:
        return is_prime[N]

for _ in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    total = a + b

    if total > 4 and total % 2 == 0:
        print('YES')
        continue

    if total == 2 or total == 3:
        print('NO')
        continue
    
    if check_prime(total-2):
        print('YES')
    else:
        print('NO')      
    