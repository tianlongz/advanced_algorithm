import random

iters = 100
samplesize = 800

votes = [None] * samplesize
avevote = 0
samplelist = [-1] * 1000000
for i in range(520000):
    samplelist[i] = 1
for run in range(iters):
    votes = random.choices(samplelist, k = samplesize)
    if sum(votes) > 0:
        avevote += 1
print("avevote:", avevote)