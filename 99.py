i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%2d"%(i,j,i*j),end=" ")
        j = j + 1
    print("\n")
    i = i + 1
print("------------------------------------------")
i = 9
while i >= 1:
    j = 1
    while j <= i:

        print("%d*%d=%2d"%(i,j,i*j),end=" ")
        j = j + 1
    print("\n")
    i = i - 1

print("------------------------------------------")
for i in range(1,10):
    for k in range(1,i+1):
        print('{}*{}={:2}'.format(i,k,i*k),end=' ')
    print(' ')