#use romeo.txt for this script
hand = open('romeo.txt')
unique = list()
for line in hand :
    rline = line.rstrip()
    wrd = rline.split()
    for i in wrd:
        if i not in unique:
            unique.append(i)
unique.sort()
print(unique)