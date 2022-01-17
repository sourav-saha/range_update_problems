import sys

def prefix_sum(arr):
  pa = [0]*len(arr)
  
  for i in range(1, len(arr)):
    if i == 1:
      pa[i] = arr[i]
    else:
      pa[i] = pa[i-1] + arr[i]
      
  return pa
  
  
if __name__ == "__main__":
  m, n = map(int, sys.stdin.readline().strip().split(' '))
  arr = [0]*(m+1) 
  for i in range(n):
    a, b, k = map(int, sys.stdin.readline().strip().split(' '))
    arr[a] += k
    if b < m:
      arr[b+1] -= k 
    
  pa = prefix_sum(arr)
  print(max(pa))
