#Seleection  Sort
def selection_sort(D):
    n = len(D)
    for i in range(n-1):
        index = i
        for j in range(i+1, n):
            if (D[j] < D[index]):
                index = j
        D[index], D[i] = D[i], D[index]
    return(D)

input_str = input('Enter numbers (Use Comma to separate the numbers)\nExample: 9,-5,6,44,50\nNumbers: ')
input_str = input_str.replace(' ', '')
D = list(map(int, input_str.split(',')))

try:
    print(selection_sort(D))
except:
    print("input is not valid")
