from time import time


def contains(collection, target):
    return target in collection


def bs_contains(ordered, target):
    low = 0
    high = len(ordered)-1
    while low <= high:
        mid = (low + high) // 2
        if target == ordered[mid]:
            return mid
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -(low + 1)


def insert_in_place(ordered, target):
    idx = bs_contains(ordered, target)
    if idx < 0:
        ordered.insert(-(idx + 1), target)
        return

    ordered.insert(idx, target)


def performance():
    n = 1024
    while n < 5000000:
        ordered = list(range(n))
        now = time()

        insert_in_place(ordered, n+1)

        done = time()

        print(n, (done-now) * 1000)
        n *= 2


performance()