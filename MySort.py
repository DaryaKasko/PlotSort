import random
import datetime
import prettytable
import matplotlib.pyplot as plt

N = int(input(print("Введите количество элементов: \n")))
min = int(input(print("ведите минимальный элемент списка: \n")))
max = int(input(print("ведите максимальный элемент списка: \n")))

A = []

for i in range(N):
    A.append(random.randint(min, max))
print(A)

B = A.copy()
print(B)


"""x = []
for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random()*(max - min)+min)))
"""


def MergeSort(A):                    #Сортировка слиянием
    if len(A) > 1:
        mid = len(A) // 2
        C = A[:mid]
        D = A[mid:]
        MergeSort(C)
        MergeSort(D)
        i = 0
        j = 0
        k = 0
        while i < len(C) and j < len(D):
                if C[i] < D[j]:
                    A[k] = C[i]
                    i += 1
                else:
                    A[k] = D[j]
                    j += 1
                k = k + 1
        while i < len(C):
            A[k] = C[i]
            i += 1
            k += 1
        while j < len(D):
            A[k] = D[j]
            j += 1
            k += 1

MergeSort(A)
print(A)

# поиск наименьшего элемента в списке
def MinElem(A):
    min = A[0]
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
    print(min)

def SelectSort(A):
    min = A[0]
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
    for k in range(len(A)):
        min, A[k] = A[k], min
    j = 1
    for j in range(len(A)-1):
        a = A[j]
        A[j] = min
        A[i] = a

    print(A)
SelectSort(A)