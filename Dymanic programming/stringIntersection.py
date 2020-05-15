def stringIntersection(str1, str2):
    inter = []

    for i in range(0, len(str1)*len(str2)):
        isSame = str1[i // len(str2)] == str2[i % len(str2)]
        isValid = i // len(str2) >= 1 and i % len(str2) >= 1

        if isValid and isSame:
            inter.append(int(isSame) + inter[i - len(str2) - 1])
        else:
            inter.append(int(isSame))

    maxIndex, maxValue = max(enumerate(inter), key = lambda itera: itera[1])

    return str2[(maxIndex % len(str2)) - maxValue + 1 : maxIndex % len(str2) + 1]
        
