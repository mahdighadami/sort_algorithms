#Bubble Sort
def bubble_sort(C):
    n = len(C)
    for i in range(n-1):
        bubble_found = False
        for j in range(n-1, i, -1):
            if C[j] < C[j-1]:
                C[j] , C[j-1] = C[j-1] , C[j]
                bubble_found = True
        if not bubble_found:
            break
    return(C)

input_str = input('Enter numbers (Use Comma to separate the numbers)\nExample: 9,-5,6,44,50\nNumbers: ')
input_str = input_str.replace(' ', '')

try:
    C = list(map(int, input_str.split(',')))
    print(bubble_sort(C))
except:
    print("input is not valid")