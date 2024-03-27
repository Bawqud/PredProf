File = open('space.txt',encoding = "UTF-8")
St = []
for i in File:
    St.append(i.split(','))

while True:
    flag = False
    zapros = input('Введите название корабля - ')
    if zapros == 'stop':
        break
    else:
        for i in range(len(St)):
            if St[i][0] == zapros:
                buf = St[i][1].split()
                print('Корабль', St[i][0], 'был отправлен с планеты:', St[i][1], 'и его направление движения было:', St[i][3][:-1])
                flag = True
        if not(flag):
            print('error.. er.. ror..')

File.close()