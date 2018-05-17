import pdb


def promising(index, weights, target_weight, cur_weight, total_of_remain):
    if cur_weight + total_of_remain < target_weight:
        return False
    if cur_weight == target_weight:
        return True
    if cur_weight + weights[index + 1] > target_weight:
        return False
    return True


def solve(index, weights, target_weight, items, cur_weight, total_of_remain):
    # if index >= len(weights):
    #     return

    #print(items, cur_weight)
    if promising(index, weights, target_weight, cur_weight, total_of_remain):
        if cur_weight == target_weight:
            print('weights: ', weights)
            print('teims: ', items)
        else:
            # if choose this index item
            solve(index + 1,
                  weights,
                  target_weight,
                  items + [index + 1],
                  cur_weight + weights[index + 1],
                  total_of_remain - weights[index + 1])

            # else
            solve(index + 1,
                  weights,
                  target_weight,
                  items,
                  cur_weight,
                  total_of_remain - weights[index + 1])


if __name__ == '__main__':
    # weights = [3, 4, 5, 7]
    # weights = sorted(weights)
    # items = []
    # cur_weight = 0
    # target_weight = 13
    # total_of_remain = sum(weights)
    #
    # solve(index=-1, weights=weights, target_weight=target_weight,
    #       items=items, cur_weight=cur_weight, total_of_remain=total_of_remain)


    def promising2(i,weight, total):
        if i == 3:
            #pdb.set_trace()
        return ((weight+total >= W) and (weight == W or weight+w[i+1] <=W))

    def s_s(i, weight, total, include):
        if(promising2(i, weight, total)==True):
            if(weight == W):
                print("sol",include )
            else:
                include[i+1]=1
                s_s(i+1, weight+w[i+1],total-w[i+1],include)
                include[i+1]=0
                s_s(i+1,weight,total-w[i+1],include)

    n = 4
    w = [3, 4, 5, 6]
    W = 13
    print("items =", w, "W =", W)
    include = n*[0]
    total=0
    for k in w:
        total+=k
    s_s(-1,0,total,include)
