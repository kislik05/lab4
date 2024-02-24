start = int(input())
end = int(input())

def ger(start, end):
    while start >= end:
        yield start
        start -= 1    

print(list(ger(start, end)))

