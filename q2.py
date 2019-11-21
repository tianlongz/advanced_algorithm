import random


avecross = [None] * 50
for run in range(50):
    s = 0
    flagneg = 0
    flagpos = 0
    cross = 0

    # change t here:
    time = 16 * 10000

    for t in range(time):
        decide = random.random()
        if decide >= 0.5:
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
    avecross[run] = cross
print("avecross:", (sum(avecross) / 50) )
