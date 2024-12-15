num1, a, b = map(int, input().split())
k = ((a + b - 1) % num1+ num1) % num1 + 1
print(k)
 
