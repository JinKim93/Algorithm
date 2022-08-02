# 1이 될 때까지 


# n = 25 k=3 
# 1. 25/ 2. 25 -1 3. 24 /3 
n,k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k ) * k
    # result 총연산횟수 (n -target) = 1을 빼는 연산횟수
    result = result + (n - target)
    n = target
    if n < k:
        break
    result = result + 1
    n = n // k

    result = result + (n - 1)
    print(result)
