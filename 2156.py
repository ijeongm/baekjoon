n = int(input())  # 잔의 개수
s = [int(input()) for _ in range(n)]  #포도주의 양

if n == 1: 
    print(s[0])
elif n == 2: 
    print(s[0] + s[1])
else:
    # dp: 최대 마실 수 있는 포도주 양
    dp = [0] * n
    dp[0] = s[0]  
    dp[1] = s[0] + s[1] 
    dp[2] = max(s[2] + s[0], s[2] + s[1], dp[1]) 
    
    for i in range(3, n):
        dp[i] = max(s[i] + dp[i-2], s[i] + s[i-1] + dp[i-3], dp[i-1])
        
    print(max(dp))
