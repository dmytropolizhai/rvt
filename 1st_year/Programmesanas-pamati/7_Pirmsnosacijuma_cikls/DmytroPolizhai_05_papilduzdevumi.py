n = 21
level = 0

for i in range(1, n + 1):
    level_count = (i * (i + 1) * (2 * i + 1)) / 6
    if level_count > n:
        break
    
    level += 1

print(level)