"""implementation of bubblesort"""

from typing import List

def bubblesort2(arr: List) -> List:
    for i in range(len(arr)):
        for j in range(len(arr)-1,0,-1):
            if arr[j] < arr[j-1]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp

arr = [54,26,93,17,77,31,44,55,20]
bubblesort2(arr)
print(arr)