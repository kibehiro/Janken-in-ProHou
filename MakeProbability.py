def makeprobability(hairetsu):
    probability = []
    for k in range(len(hairetsu)):  # probabilityに確率を入れる
        probability.append(hairetsu[k] / sum(hairetsu))

    return probability
