def surrenderTask(coins, s):
    minS = [0]

    for i in range(1, s + 1):
        minS.append(
            1 + min([minS[i - coin] for coin in coins if i - coin >= 0])
        )

    return minS[s]

if __name__ == '__main__':
    res = surrenderTask([1, 2, 5, 10], 7)

    print(res)
