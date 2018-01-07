
import numpy

def sort(A, left, right):
    if left >= right:
        return
    m = partition(A, left, right)
    sort(A, left, m - 1)
    sort(A, m + 1, right)


def partition(A, left, right):
    key = A[right]
    i = left - 1
    for j in range(left, right):
        if A[j] <= key:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[right] = A[right], A[i + 1]        
    return i + 1


def ungarded_partition(A, first, last):
    pivot = numpy.median([A[first], A[first+(last-first)/2], A[last-1]])
    while True:
        while A[first] < pivot:
            first += 1
        last -= 1
        while A[last] > pivot:
            last -= 1
        if first < last:
            A[first], A[last] = A[last], A[first]
            first += 1
        else:
            return first, pivot

if __name__ == '__main__':
    '''
    while True:
        lst = map(int, raw_input().split())
        sort(lst, 0, len(lst) - 1)
        print(lst)
    '''

    A = [2, 1, 8, 7, 3, 5, 6, 4]
    m = ungarded_partition(A, 0, len(A))
    print((A, m))
