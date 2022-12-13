

def lilysHomework(arr):
    return min(minSwapsAsc(arr), minSwapsDesc(arr))
 
def minSwapsDesc(arr):
    positions = [
   
    n = len(arr)
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if visited[i] or positions[i] == i:
            continue
       
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = positions[j]
            cycle_size += 1
       
        if cycle_size > 0:
            ans += (cycle_size - 1)x[0] for x in sorted(enumerate(arr), key=lambda x: x[1], reverse=True)]