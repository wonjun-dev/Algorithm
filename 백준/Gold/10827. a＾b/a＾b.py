import sys

a, b = sys.stdin.readline().strip().split()
fp = len(a.split('.')[-1])

a = int(a.replace('.', ''))
b = int(b)

fp = fp * b
num = str(a ** b)

if len(num) < fp:
    num = '0' * (fp-len(num)+1) + num
num = num[:-fp] + '.' + num[-fp:]

print(num)