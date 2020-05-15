from collections import deque

def BFS(v, p, start, end):
    # min distances to verticles
    d = [0 for i in range(v)]
    # checked verticles list
    mark = []

    # distance to start is zero
    d[start] = 0

    # queue of verticles
    queue = deque()

    # add start point to queue
    queue.append(start)

    while len(queue):
        # get first verticle in queue
        cur = queue.popleft()

        for path in p:
            # check path that start from current verticles and
            # finish in non checked verticle
            if path['start'] == cur and path['end'] not in mark:
                # update distance to end verticle
                d[path['end']] = d[path['start']] + 1
                # add end verticle to queue
                queue.append(path['end'])

                # we found minimum distance to end point
                if path['end'] == end:
                    return d[path['end']]

        # add current verticle to checked list
        mark.append(cur)

    # path to verticle doesn't exist
    return -1


if __name__ == '__main__':
    res = BFS(6, [
            {'start': 0, 'end': 1},
            {'start': 1, 'end': 3},
            {'start': 0, 'end': 2},
            {'start': 3, 'end': 4},
            {'start': 4, 'end': 5},
            {'start': 2, 'end': 5}
        ], 0, 5)

    print('Res:' + str(res))

    
    
