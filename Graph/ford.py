def ford(v, p, start, end):
    # create distance list with infinite values by default
    d = [float('Inf') for i in range(0, v)]

    # set start value to zero
    d[start] = 0

    for i in range(0, v):
        # check path
        for path in p:
            # write new distance to the verticle
            d[path['end']] = min([d[path['end']],
                                  d[path['start']] + path['weight']])

    # return list with minimum distances
    return d

if __name__ == '__main__':
    res = ford(v = 4,
             p = [
                 {'start': 0, 'end': 3, 'weight': 10},
                 {'start': 3, 'end': 2, 'weight': 5},
                 {'start': 2, 'end': 1, 'weight': 6},
                 {'start': 1, 'end': 2, 'weight': 1},
                 {'start': 3, 'end': 1, 'weight': 2}
             ],
             start = 0,
             end = 2)

    print(res)
                
