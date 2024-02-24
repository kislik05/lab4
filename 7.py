num = int(input())

def ger(start):
    while start <= num:
        if start % 3 == 0 and start % 4 == 0:
            yield start
        start += 1

print(list(ger(0)))
