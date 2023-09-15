from math import log2


def main(s, n):
    global sdnf, sknf, functionBin
    if len(s) < n:
        for i in range(2):
            main(s + str(i), n)
        return

    else:
        indexOfCurrentFunctionBit = int(s, 2)
        if functionBin[indexOfCurrentFunctionBit] == '0':
            if len(sknf) != 0:
                sknf += ' * '
            sknf += '('
            for i in range(n):
                if s[i] == '1':
                    sknf += '|'
                sknf += chr(97 + i)
                if i != n - 1:
                    sknf += '+'
            sknf += ')'
        else:
            if len(sdnf) != 0:
                sdnf += ' + '
            sdnf += '('
            for i in range(n):
                if s[i] == '0':
                    sdnf += '|'
                sdnf += chr(97 + i)
                if i != n - 1:
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
