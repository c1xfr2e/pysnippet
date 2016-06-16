
def insert_sort(array):
    for i in range(1, len(array)):
        # insert array[i] into array[0,i-1] which is already sorted
        j = i - 1
        tmp = array[i]
        while j >= 0 and tmp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = tmp

    return array


A = [2, 8, 7, 1, 5, 3, 6, 4]


def partition(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j] <= x:
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[r] = L[r], L[i + 1]
    return i + 1

A = [3,34,1,15,21,6,11,8,12]
q = partition(A, 0, len(A) - 1)
print A
print q


S = ['A', 'C', 'B', 'A', 'A', 'C', 'B', 'C', 'C', 'C', 'B']
M = 'B'


def move3(S, M):
    lt = 0
    gt = len(S) - 1
    i = 0
    while i <= gt:
        if S[i] < M:
            S[lt], S[i] = S[i], S[lt]
            lt += 1
            i += 1
        elif S[i] > M:
            S[gt], S[i] = S[i], S[gt]
            gt -= 1
        else:
            i += 1

move3(S, M)
print S
