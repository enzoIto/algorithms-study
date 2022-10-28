"""Paths inside a Heap"""
from typing import List


def right(i):
    return 2*i + 1

def left(i):
    return 2*i

"""Max Heapify function. The ideia of this function is to
preserve the Max-Heapify property inside a heap"""
def max_heapify(A: List[int], i: int) -> List:
    l = left(i)
    
    r = right(i)
    "is A.heap_size === len(A)?"
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= len(A) and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i] = A[largest]
        max_heapify(A, largest)
    return A
