import random


avecross = [None] * 50
for run in range(50):
    s = 0
    flagneg = 0
    flagpos = 0
    cross = 0
    time = 4 * 10000
    # count = 0
    for t in range(time):
        decide = random.random()
        if decide >= 0.5:
            # count += 1
            if flagneg == 1:
                flagneg = 0
            if flagpos == 1:
                cross = cross + 1
            s = s + 1
            if s == 0:
              flagpos = 1
        else:
            if flagpos == 1:
                flagpos = 0
            if flagneg == 1:
                cross = cross + 1
            s = s - 1
            if s == 0:
              flagneg = 1

    # print("cross time:", cross)
    avecross[run] = cross
    # print(count)
print("avecross:", (sum(avecross) / 50) )
