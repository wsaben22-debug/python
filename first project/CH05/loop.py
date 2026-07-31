for i in range(10):
    if(i<= 0):
        continue
    j = 1
    while 1 :
        print(i, '*', j, '=', i*j, end='\t')
        j = j + 1
        if (j > 9):
            break
    print()
print() #去掉這個會少一個結尾空行