#Merge Sort
def merge_sort(E):
    if (len(E) < 2):
        return E

    mid = len(E) // 2
    E_prime = E[:mid]
    E_second = E[mid:]
    E_prime = merge_sort(E_prime)
    E_second = merge_sort(E_second)
    i = j = 0
    E = []

    while i < len(E_prime) and j < len(E_second):
        if E_prime[i] <= E_second[j]:
            E += [E_prime[i]]
            i += 1
        else:
            E += [E_second[j]]
            j += 1
    E += E_prime[i:] + E_second[j:]
    return E

input_str = input('Enter numbers (Use Comma to separate the numbers)\nExample: 9,-5,6,44,50\nNumbers: ')
input_str = input_str.replace(' ', '')
E = list(map(int, input_str.split(',')))

try:
    print(merge_sort(E))
except:
    print("input is not valid")