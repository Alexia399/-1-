a = int(input())

for i in range(a):
    import time

    flag1 = [
	"********",
   "--------",
   "^^^^^^^^"]

    p = len(flag1)
    flag2 = ['$$$$$$$$',
         '&&&&&&&&',
         '________']

    print('\x1b[2J\x1b[H', end = '')

    for picture in flag1:
       print(picture)

    time.sleep(2)

    for i in range(len(flag1)):
        print('\x1b[H', end = '')
        for j in range(i+1, p ):
           print('\x1b[2K')
        time.sleep(1)

    print('\x1b[2J\x1b[H', end = '')

    for picture in flag2:
       print(picture)
    time.sleep(2)

    for i in range(len(flag2)):
        print('\x1b[H', end='')
        for j in range(i+1, len(flag2)):
           print('\x1b[2K')
        time.sleep(1)



    print('\x1b[2J\x1b[H', end = '')