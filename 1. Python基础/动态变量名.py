for i in range(1,3):
    locals()['x'+str(i)] = 100 + i
print(x1, x2)