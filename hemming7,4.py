a = input()
flag = 0
if len(a) != 7:
    print('Длина набора не равна 7.')
    flag = 1
else:
    for i in a:
        if int(i) != 0 and int(i) != 1:
            print('Не двоичная запись числа')
            flag = 1
if flag == 0:    
    k = 0   
    r1 = a[0]
    r2 = a[1]
    r3 = a[3]
    modr1 = (a[2] + a[4] + a[6]).count('1') % 2
    modr2 = (a[2] + a[5] + a[6]).count('1') % 2
    modr3 = (a[4] + a[5] + a[6]).count('1') % 2
    if r1 != str(modr1):
        k += 1
    if r2 != str(modr2):
        k += 2
    if r3 != str(modr3):
        k += 4
    if (k > 0):
        if k == 1:
            if a[k-1] == '0':
                a = '1' + a[k:]
            else:
                a = '0' + a[k:]
        elif k == 7:
            if a[k-1] == '0':
                a = a[:k-1] + '1'
            else:
                a = a[:k-1] + '0'
        elif a[k-1] == '0':
            a = a[:k-1] + '1' + a[k:]
        else:
            a = a[:k-1] + '0' + a[k:]
        print(f'Ошибка в бите №{k}')
        print('Правильное сообщение(только информационные биты) -',a[2]+a[4]+a[5]+a[6])
    else:
        print('Ошибок нет, код доставлен верно')
        print(a[2]+a[4]+a[5]+a[6])

print(43+75+107+27+58)

