# code reference: https://github.com/ndb796/python-for-coding-test/blob/master/10/5.py

def solution(n, costs):
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        
        return parent[x]

    
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    
    answer = 0
    
    parent = [i for i in range(n + 1)]
    costs.sort(key=lambda x:(x[2], x[0], x[1]))
    
    for cost in costs:
        a, b, c = cost
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c
    
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))