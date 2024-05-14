# dp[i]가 i 계단까지 점수의 최댓값을 항상 보장

n=int(input()) # 계단 개수
s=[int(input()) for _ in range(n)] # 계단 점수

dp=[0]*(n)

dp[0]=s[0] # 첫째 계단 수동 계산
dp[1]=s[0]+s[1] # 둘째 계단까지 수동 계산
for i in range(2,n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
    dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
print(dp[-1])