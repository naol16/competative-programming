n = int(input())
 
ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
 
if (bx < ax) == (cx < ax) and (by < ay) == (cy < ay):
    print('YES')
else:
    print('NO')
