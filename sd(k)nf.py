from math import log2


def main(currentSetOfNumbers, requiredNumberOfNumbers):
    global sdnf, sknf, functionBin
    if len(currentSetOfNumbers) < requiredNumberOfNumbers:
        for i in range(2):
            main(currentSetOfNumbers + str(i), requiredNumberOfNumbers)
        return

    else:
        indexOfCurrentFunctionBit = int(currentSetOfNumbers, 2)
        if functionBin[indexOfCurrentFunctionBit] == '0':
            if len(sknf) != 0:
                sknf += ' * '
            sknf += '('
            for i in range(requiredNumberOfNumbers):
                if currentSetOfNumbers[i] == '1':
                    sknf += '|'
                sknf += chr(97 + i)
                if i != requiredNumberOfNumbers - 1:
                    sknf += '+'
            sknf += ')'
        else:
            if len(sdnf) != 0:
                sdnf += ' + '
            sdnf += '('
            for i in range(requiredNumberOfNumbers):
                if currentSetOfNumbers[i] == '0':
                    sdnf += '|'
                sdnf += chr(97 + i)
                if i != requiredNumberOfNumbers - 1:
                    sdnf += '*'
            sdnf += ')'


functionVector = input()
functionVector = functionVector.upper()
functionBin = bin(int(functionVector, 16))[2:]
functionBin = '0' * (len(functionVector) * 4 - len(functionBin)) + functionBin
n = int(log2(len(functionBin)))
print(n)
sdnf = ''
sknf = ''
print(functionBin)
main('', n)
print(sdnf)
print(sknf)
