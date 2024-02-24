start = int(input())
num = int(input())

def ger(start):
    while start <= num:
        yield start * start
        start += 1

print(list(ger(start)))
