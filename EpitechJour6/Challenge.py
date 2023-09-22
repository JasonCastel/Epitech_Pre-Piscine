import time

startingTime = time.time()
def pui():
    pow(42,84)
    pow(42,168)
    duration = time.time()- startingTime
    return duration

print(pui())

