
n = 4
W = 16
p = [40, 30, 50, 10]
w = [2, 5, 10, 5]
max_profit = 0
best_set = [0, 0, 0, 0]


def dfs(index, profit, weight, include):
    global max_profit, best_set

    if weight <= W and profit > max_profit:
        max_profit = profit
        best_set = list(include)

    if promising(index, profit, weight, include):
            include[index + 1] = 0
            dfs(index)

            include[index + 1] = 1
            dfs(index)


def promising(index, profit, weight):
    global max_profit

    if weight >= W:
        return False

    if weight + w[index+1] == W:
        return True
    elif weight + w[index+1] > W:
        return False

    remain_weight = 0
    for i in range(index + 1):
        remain_weight += w[i]
    if weight + remain_weight < W:
        return False

    if estimate(index, profit, weight) <= max_profit:
        return False

    return True


def estimate(index, profit, weight):
    total_weight = weight
    j = index + 1
    while j < n and total_weight < W:
        total_weight += w[j]
        j += 1

    remain_weight = total_weight - weight
    k = j

    result = profit
    while k < n and remain_weight > 0:
        result += p[k] / w[k]
        remain_weight -= 1
    return result


def get_value(index, include):
    value = 0
    for i in range(index + 1):
        value += p[i] * include[i]
    return value

if __name__ == "__main__":
    _include = [0, 0, 0, 0]
    dfs(-1, 0, 0, _include)
    print(max_profit)
    print(best_set)
