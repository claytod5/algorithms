def knapsack(w, weights, values):
    table = [[0 for i in range(w + 1)] for j in range(len(weights) + 1)]

    for i in range(len(weights) + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weights[i - 1] <= j:  # if weight[0, 1, etc] is <= cell's allowed weight
                table[i][j] = max(
                    values[i - 1] + table[i - 1][j - weights[i - 1]], table[i - 1][j]
                )
            else:
                table[i][j] = table[i - 1][j]

    return table[len(weights)][w]


if __name__ == "__main__":
    weights = [1, 3, 4]
    values = [1500, 2000, 3000]
    print(knapsack(4, weights, values))
