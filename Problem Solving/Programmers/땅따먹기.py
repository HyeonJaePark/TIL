def solution(land):
    n = 4
    
    for i in range(1, len(land)):
        for j in range(n):
            curr_num = land[i][j]
            for k in range(n):
                if j == k:
                    continue
                if curr_num + land[i - 1][k] > land[i][j]:
                    land[i][j] = curr_num + land[i - 1][k]
                    
    return max(land[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))