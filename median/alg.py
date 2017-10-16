from random import randint
import sys

def check_sorted(i_list):
    for i in range (0, len(i_list)-1):
        if i_list[i] > i_list[i+1] :
            return False
    return True

def check_median(A, p, q, r):
    if q != p + ((r-p)//2) :
        print("1:", p, q, r, p+((r-p)//2), sep=',')
        return False

    for x in A[p:q]:
        if x > A[q]:
            print("2:")
            return False

    for x in A[q+1:r+1]:
        if x < A[q]:
            print("3:")
            return False
    return True

def merge(a_list, b_list):
    c_list = []
    c_len = len(a_list) + len(b_list)
    a_list.insert(len(a_list), sys.maxsize)
    b_list.insert(len(b_list), sys.maxsize)
    for c_i in range(0, c_len):
        if a_list[0] < b_list[0]:
            c_list.insert(c_i, a_list.pop(0))
        else:
            c_list.insert(c_i, b_list.pop(0))
    return c_list

def merge_sort(i_list): 
    if len(i_list)>1:
        mid = len(i_list)//2
        left = i_list[:mid]
        right = i_list[mid:]

        ordered_left = merge_sort(left)
        ordered_right = merge_sort(right)
        return merge(ordered_left, ordered_right)
    else:
        return i_list

def random_partition(A, p, r):
    q = randint(p, r)
    A[q], A[r] = A[r], A[q]
    i = p - 1
    
    for j in range(p, r):
        if A[j] < A[r]:
            i+=1
            A[i], A[j] = A[j], A[i]
    
    i+=1
    A[r], A[i] = A[i], A[r]
    return i, A

def find_nth_element(A, p, r, i):
    if p == r:
        return p, A
    q, A = random_partition(A, p, r)
    if i == q:
        return q, A
    elif i < q:
        return find_nth_element(A, p, q-1, i)
    else:
        return find_nth_element(A, q+1, r, i)

def median_NlogN(A, p, r):
    A[p:r+1] = merge_sort(A[p:r+1])
    q = p + (r-p)//2
    return q, A

def median_N(A, p, r):
   return find_nth_element(A, p, r, p + (r-p)//2)

n = 2000
l = [ randint(0, sys.maxsize) for i in range(n) ]
p = randint(0, n-2)
r = randint(p+1, n-1)

q1, l1 = median_NlogN(l, p, r)
print(p, q1, r)
print( check_median(l1, p, q1, r) )

q2, l2 = median_N(l, p, r)
print(p, q2, r)
print( check_median(l2, p, q2, r) )