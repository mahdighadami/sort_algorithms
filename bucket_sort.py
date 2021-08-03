#Bucket sort

#you can use bubble_sort or any appropriate sort algorithms instead selection sort for use in bucket sort
def selection_sort(D):
    n = len(D)
    for i in range(n-1):
        index = i
        for j in range(i+1, n):
            if (D[j] < D[index]):
                index = j
        D[index], D[i] = D[i], D[index]
    return(D)


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

#get input and try/exception:
input_str = input('Enter non negative integer numbers (Use Comma to separate the numbers)\nExample: 9,5,6,44,50\nNumbers: ')
input_str = input_str.replace(' ', '')

try:
    F = list(map(int, input_str.split(',')))
    print(bucket_sort(F))
except:
    print("input is not valid")
