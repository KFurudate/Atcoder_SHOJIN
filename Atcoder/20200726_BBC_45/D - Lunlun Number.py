k = int(input())

RunRun = [i for i in range(1, 10)]

while True:
    if k <= len(RunRun):
        print(RunRun[k - 1])
        exit()

    for r in RunRun:
        for i in range(-1, 2):
            tmp = r % 10 + i
            if tmp < 0 or 9 < tmp: continue
            tmp = (r * 10) + tmp
            RunRun.append(tmp)
        # print(RunRun)