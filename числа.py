f = open('123.txt', 'r')
list1 = []
for i in f:
    list1.append(float(i.strip()))

CSI ="\x1b["
RESET = f"{CSI}0m"
blue = '\x1b[44m'
mean1251 = sum(abs(list1[x]) for x in range(125))/ 125
mean1252 = sum(abs(list1[x]) for x in range(125,250))/ 125

summa = mean1251 + mean1252
otvet1 = mean1251/summa * 100
otvet2 = mean1252/summa *100
print(otvet1, otvet2)
print(f'{blue}{' '*int(otvet1)}{RESET}' + str(otvet1))
print(f'{blue}{' '*int(otvet2)}{RESET}' + str(otvet2))
#c = 0
#for x in range(125):
#    c += abs(list1[x])
#c = c/125
#print(c, mean1251)

f.close()