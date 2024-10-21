def can_make_cookies(mid, list1, list2, magic_powder):
    total_powder_needed = 0
    for i in range(len(list1)):
        required = list1[i] * mid 
        if required > list2[i]: 
            total_powder_needed += required - list2[i] 
        if total_powder_needed > magic_powder:
            return False
    return True  


def max_cookies(list1, list2, magic_powder):
    low, high = 0, 10**9 
    answer = 0
    while low <= high:
        mid = (low + high) // 2
        if can_make_cookies(mid, list1, list2, magic_powder):
            answer = mid  
            low = mid + 1  
        else:
            high = mid - 1 
    return answer

a, b = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

print(max_cookies(list1, list2, b))
