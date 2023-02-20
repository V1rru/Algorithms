amount_of_comparisons = 0
amount_of_permutations = 0

def quick_sort(n):
    
    global amount_of_comparisons
    global amount_of_permutations

    if len(n) <= 1:
        return n

    root = n[0]
    left = list(filter(lambda x: x < root, n))
    
    amount_of_comparisons += len(left)
    amount_of_permutations += len(left)

    center = [i for i in n if i == root]

    right = list(filter(lambda x: x > root, n))

    amount_of_comparisons += len(right)

    return quick_sort(left) + center + quick_sort(right)

array = []

def file_reader():
    file = open("D:\VS2022 Projects\Sorting Algorithms\Lists\\100 random elements.txt", "r")
    while True:
        line = file.readline().rstrip()
        if not line:
            break
        array.append(int(line))
    file.close()


file_reader()
# print(quick_sort([7, 6, 9, 8, 10, 4, 3, 5]))
print(quick_sort(array))
# print(quick_sort([1, 2, 3, 4, 5, 6, 7, 8]))
print(amount_of_comparisons)
print(amount_of_permutations)

