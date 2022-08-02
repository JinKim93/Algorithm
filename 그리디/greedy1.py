# 거스름돈 문제

n = 1260
count = 0

# 큰단위부터 확인
array = [500,100,50,10]

for coin in array:
    count = count + (n // coin) # 해당 화폐로 거슬러 줄수 있는 동전의 개수 
    n = n % coin

print(count)