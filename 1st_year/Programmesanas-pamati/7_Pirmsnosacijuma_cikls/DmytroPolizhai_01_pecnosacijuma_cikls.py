x = -3

# Mūžīgais cikls
while True:  
    y = 2 * x - 1
    print(y)

    x += 0.5
    
    # Do-while nosacījums
    if x <= 1:
        continue
    else:
        break