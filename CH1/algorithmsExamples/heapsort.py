"""Paths inside a Heap"""
from typing import List


def right(i):
    return 2*i + 1

def left(i):
    return 2*i

"""Max Heapify function. The ideia of this function is to
preserve the Max-Heapify property inside a heap"""
def max_heapify(A: List[int], N: int,i: int) -> None:
    
    largest = i
    l = left(i)
    r = right(i)

    if l < N and A[l] > A[largest]:
        largest = l
    if r < N and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, N, largest)
