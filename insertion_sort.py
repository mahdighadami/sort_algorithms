#Insertion Sort
def insertion_sort(B):
    for j in range(1, len(B)):
        item = B[j]
        i = j
        while i>0 and item<B[i-1]:
            B[i] = B[i-1]
            i -= 1
        B[i] = item
    return(B)

input_str = input('Enter numbers (Use Comma to separate the numbers)\nExample: 9,-5,6,44,50\nNumbers: ')
input_str = input_str.replace(' ', '')

try:
    B = list(map(int, input_str.split(',')))
    print(insertion_sort(B))
except:
    print("input is not valid")