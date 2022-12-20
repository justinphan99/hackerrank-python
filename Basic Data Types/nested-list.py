if __name__ == '__main__':
    res = []
    scores = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        res.append([name, score])
        scores.append(score)
    scores = sorted(set(scores))
    top2_score = scores[1]
    for val in res:
        if val[1] == top2_score:
            names.append(val[0])
    names = sorted(names)
    for name in names:
        print(name)