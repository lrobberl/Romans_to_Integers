value = {"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}

def romanToInt(s):
    number = 0
    i = 0
    numLen = len(s)
    while i < numLen:
        if i < numLen-1 and value[s[i]] < value[s[i+1]]:
            number += value[s[i+1]] - value[s[i]]
            i += 2
        else:
            number += value[s[i]]
            i += 1
    return number

# main
while 1:
    romanNumber = input("Roman number: ")
    if romanNumber == "stop":
        break
    print("Integer number: %d" % romanToInt(romanNumber))








