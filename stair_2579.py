n=int(input()) # 계단 개수
s=[int(input()) for _ in range(n)] # 계단 점수

dp=[0]*(n)

if (len(s)<=2): # 계단 2개 이하
    print(sum(s))
else: # 계단 3개 이상
    dp[0]=s[0] # 첫째 계단 계산
    dp[1]=s[0]+s[1] # 둘째 계단까지 계산
    for i in range(2,n): # 3번째 계단부터
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])