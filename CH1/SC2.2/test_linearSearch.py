"""Consider the searching problem:
Input: A sequence of n numbers 〈a1, a2, ... , an〉 stored in array A[1 : n]
and a value x.
Output: An index i such that x equals A[i] or the special value NIL if x
does not appear in A."""

def LinearSearch(ar, x):
    for i in range(len(ar)):
        if x == ar[i]:
            return i
        else:
            i += 1
    return None

def test_search():
    assert LinearSearch([1,2,3],3) == 2

def test_strings():
    assert LinearSearch(['a','string','letter'],'string') == 1

def test_error():
    assert LinearSearch([1,2,3], 'string') == 0