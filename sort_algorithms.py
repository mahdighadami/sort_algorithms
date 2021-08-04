#Counting Sort
def counting_sort(A):
    m = max(A)
    count = [0] * (m+1)

    for x in A:
        count[x] += 1

    A=[]

    for i in range(m+1):
        A += [i] * count[i]

    print(A)

A = [10, 3, 5, 2, 8, 4, 0, 2, 5, 3, 9]
counting_sort(A)



#Insertion Sort
def insertion_sort(B):
    for j in range(1, len(B)):
        item = B[j]
        i = j
        while i>0 and item<B[i-1]:
            B[i] = B[i-1]
            i -= 1
        B[i] = item
    print(B)

B = [5, 2, -3, 4, 6, -7, 1, 9, 12, 5, -6]
insertion_sort(B)



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
    print(C)

C = [5, 12, 3, 4, 7, 1, 0, 6, 19, 8, 13, 4, 2, 10, 16]
bubble_sort(C)



#Seleection  Sort
def selection_sort(D):
    n = len(D)
    for i in range(n-1):
        index = i
        for j in range(i+1, n):
            if (D[j] < D[index]):
                index = j
        D[index], D[i] = D[i], D[index]
    print(D)

D = [-5, 9, 6 , 14, 7, 8, 2, 0]
selection_sort(D)



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

E = [10 , 3, 7, 4, -6, -2, 8, 0, 5]
print(merge_sort(E))



#Bucket sort
#you can write that type of sorting you want, here we are using this, for sorting two digits numbers:
#this function helps you to get number of bucket that "n" argument is there:
def get_bucket(n):
    n = n // 10
    return n
#then we have main function:
def bucket_sort(F):

    max_num = max(F)
    bucket_num = get_bucket(max_num) + 1
    buckets = [[] for i in range(bucket_num)]

    for i in F:
        buckets[get_bucket(i)] += [i]


    for i in range(bucket_num):
        buckets[i] = selection_sort(buckets[i])


    F = []
    for i in range(bucket_num):
        F += buckets[i]


    return F

F = [10 , 36, 7, 4, 56, 22, 8, 0, 72]
print(merge_sort(F))