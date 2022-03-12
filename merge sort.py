import random

arr = random.sample(range(1, 100001), 100000)

def mergesort(a):
    if len(a) <= 1:
        return a

    mid = len(a)//2

    l1 = a[:mid]
    l2 = a[mid:]

    l1 = mergesort(l1)
    l2 = mergesort(l2)


    return merge(l1, l2)

def merge(a, b):
    
    c = []
    while a and b:
        if a[0] > b[0]:
            c.append(b[0])
            b.pop(0)
        else:
            c.append(a[0])
            a.pop(0)
    while a:
        c.append(a[0])
        a.pop(0)
    while b:
        c.append(b[0])
        b.pop(0)
        
    return c

print(mergesort(arr))

#print(sorted(arr))

input()
