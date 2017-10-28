def binToArray(num):
    num = bin(num)[2:].zfill(6)
    return (num)

for i in range(0, 41):
    print(binToArray(i))