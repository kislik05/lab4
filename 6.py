end = int(input())

def myrange(start):
    while start <= end:
        yield start * start
        start += 1

print(list(myrange(0)))
