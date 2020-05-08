def deikstry(v, p, start, end):
    # list of checked elements
    checked = []
    # list of minimum distances
    d = [float('Inf') for i in range(0, v)]
    d[start] = 0
    # current element that we check
    cur = start
    
    while len(checked) < v - 1:
        for path in p:
            if path['start'] == cur:
                # rewrite end distance
                d[path['end']] = min([d[path['end']], d[cur] + path['weight']])

        # add current element to checked
        checked.append(cur)

	# find unchecked element with minimum distance
        cur = min([item for item in enumerate(d) if item[0] not in checked],
                  key = lambda x: x[1])[0]
	    
    return d[end]

if __name__ == '__main__':
    res = deikstry(v = 4,
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
