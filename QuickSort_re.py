def quick_sort(n):
    
    if len(n) <= 1:
        return n

    root = n[0]
    left = list(filter(lambda x: x < root, n))
    center = [i for i in n if i == root]
    right = list(filter(lambda x: x > root, n))

    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([7, 6, 9, 8, 10, 4, 3, 5]))