from math import log2


def truthTable(currentSetOfNumbers):
    global n, functionBin
    if len(currentSetOfNumbers) == 0:
        for i in range(n):
            print(chr(97 + i), end=' | ')
        print('F')
        print('-' * (4 * n + 2))
    if len(currentSetOfNumbers) < n:
        for i in range(2):
            truthTable(currentSetOfNumbers + str(i))
        return
    indexOfCurrentBit = int(currentSetOfNumbers, 2)
    for elem in currentSetOfNumbers:
        print(elem, end=' | ')
    print(functionBin[indexOfCurrentBit], ' is for', indexOfCurrentBit)
    print('-' * (4 * n + 2))
    return


print("Введите вектор функции")
functionVector = input()
functionVector = functionVector.upper()
functionBin = bin(int(functionVector, 16))[2:]
functionBin = '0' * (len(functionVector) * 4 - len(functionBin)) + functionBin
print("Binary function is", functionBin)
n = int(log2(len(functionBin)))
truthTable('')
