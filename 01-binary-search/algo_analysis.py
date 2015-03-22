from time import time
import random


def performance_sum():
    """Evaluate performance of sum"""

    scores = {}
    trial = 1
    while trial <= 20:
        numbers = [random.randint(1, 9) for i in list(range(2**trial))]
        now = time()
        sum = 0
        for d in numbers:
            sum = sum + d
        done = time()

        scores[trial] = (done-now)
        trial += 1

    for i in scores:
        print(2**i, "\t\t\t\t", scores[i])


def performance_sort():
    """Evaluate performance of sum"""

    scores = {}
    trial = 1
    while trial <= 16:
        numbers = [random.randint(1, 2**(trial*4)) for i in list(range(2**trial))]
        now = time()
        numbers.sort()
        done = time()

        scores[trial] = (done-now)
        trial += 1

    for i in scores:
        print(2**i, "\t\t\t\t", scores[i])


performance_sum()
performance_sort()