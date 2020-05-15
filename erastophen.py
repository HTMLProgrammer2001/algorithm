def erastofen(n):
    simple = {}

    for i in range(0, n + 1):
        simple[i] = 1

    for i in range(2, n + 1):
        if simple[i]:
            j = i * i        
            while j <= n:
                simple[j] = 0
                j += i

    simple = filter(lambda x: x[1], simple.items())
    return list(map(lambda x: x[0], simple))[2:]
                
