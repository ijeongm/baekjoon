n = int(input())  # 잔의 개수
s = [int(input()) for _ in range(n)]  #포도주의 양

if n == 1: # 잔이 1개
    print(s[0])
elif n == 2: # 잔이 2개
    print(s[0] + s[1])
else:
    # dp: 최대 마실 수 있는 포도주 양
    dp = [0] * n
    dp[0] = s[0]  # 첫번째 잔의 양을 저장
    dp[1] = s[0] + s[1]  # 첫번째,두번째 잔의 양을 합쳐 저장
    dp[2] = max(s[2] + s[0], s[2] + s[1], dp[1])  # 세번째잔: 세 가지 중 최대값 저장
    
    # 네번째 잔부터 마지막 잔까지의 최대값을 계산
    for i in range(3, n):
        dp[i] = max(s[i] + dp[i-2], s[i] + s[i-1] + dp[i-3], dp[i-1])
        
    print(max(dp))
