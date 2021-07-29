#Counting Sort
def counting_sort(A):
    m = max(A)
    count = [0] * (m+1)

    for x in A:
        count[x] += 1

    A=[]

    for i in range(m+1):
        A += [i] * count[i]

    return A

input_str = input('Enter "non negetive"!!! numbers (Use Comma to separate the numbers)\nExample: 9,5,6,44,50\nNumbers: ')
input_str = input_str.replace(' ', '')

try:
    A = list(map(int, input_str.split(',')))
    print(counting_sort(A))
except:
    print("input is not valid")
