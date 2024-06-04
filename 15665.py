n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    check = 0
    for i in range(n):
        if check != nums[i]:
            temp.append(nums[i])
            check = nums[i]
            dfs()
            temp.pop()

dfs()
