import datetime
import requests
import numpy as np
import pandas as pd
import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
Window.size = (1080/3, 2040/3)
SETLO = [(5, 50, 0, 55), (1, 10, 11, 0), (2, 20, 22, 0), (3, 30, 33, 0), (4, 40, 44, 0), (6, 60, 66, 0), (7, 70, 77, 0),
         (8, 80, 88, 0), (9, 90, 99, 0),
         (12, 21, 11, 22), (13, 31, 11, 33), (14, 41, 11, 44), (15, 51, 11, 55), (16, 61, 11, 66), (17, 71, 11, 77),
         (18, 81, 11, 88), (19, 91, 11, 99),
         (23, 32, 22, 33), (24, 42, 22, 44), (25, 52, 22, 55), (26, 62, 22, 66), (27, 72, 22, 77), (28, 82, 22, 88),
         (29, 92, 22, 99),
         (34, 43, 33, 44), (35, 53, 33, 55), (36, 63, 33, 66), (37, 73, 33, 77), (38, 83, 33, 88), (39, 93, 33, 99),
         (45, 54, 44, 55), (46, 64, 44, 66), (47, 74, 44, 77), (48, 84, 44, 88), (49, 94, 44, 99),
         (56, 65, 55, 66), (57, 75, 55, 77), (58, 85, 55, 88), (59, 95, 55, 99),
         (67, 76, 66, 77), (68, 86, 66, 88), (69, 96, 66, 99),
         (78, 87, 77, 88), (79, 97, 77, 99),
         (89, 98, 88, 99)]
CAPLOO = [(0, 55, 1, 10), (2, 20, 3, 30), (4, 40, 5, 50), (6, 60, 7, 70), (8, 80, 9, 90),
          (11, 66, 12, 21), (13, 31, 14, 41), (15, 51, 16, 61), (17, 71, 18, 81),
          (19, 91, 22, 77), (23, 32, 24, 42), (25, 52, 26, 62), (27, 72, 28, 82),
          (29, 92, 33, 88), (34, 43, 35, 53), (36, 63, 37, 73), (38, 83, 39, 93),
          (44, 99, 45, 54), (46, 64, 47, 74), (48, 84, 49, 94), (56, 65, 57, 75),
          (58, 85, 59, 95), (67, 76, 68, 86), (69, 96, 78, 87), (79, 97, 89, 98)]
CAPLO = [(00, 55), (1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60),
         (7, 70), (8, 80), (9, 90), (11, 66), (12, 21), (13, 31), (14, 41),
         (15, 51), (16, 61), (17, 71), (18, 81), (19, 91), (22, 77), (23, 32),
         (24, 42), (25, 52), (26, 62), (27, 72), (28, 82), (29, 92), (33, 88),
         (34, 43), (35, 53), (36, 63), (37, 73), (38, 83), (39, 93), (44, 99),
         (45, 54), (46, 64), (47, 74), (48, 84), (49, 94), (56, 65), (57, 75),
         (58, 85), (59, 95), (67, 76), (68, 86), (69, 96), (78, 87), (79, 97),
         (89, 98)]
HUONG = [0, 1, -1, 2, -2, 3, -3, 5, -5, 7, -7, 9, -9, 10, -10, 11, -11, 13,
         -13, 15, -15, 17, -17, 19, -19, 21, -21, 23, -23, 25, -25, 27, -27,
         29, -29, 31, -31, 33, -33, 35, -35, 37, -37, 39, -39, 41, -41, 43,
         -43, 47, -47, 49, -49]
HUCAP = [0, 1, -1, 2, -2, 3, -3, 5, -5, 7, -7, 9, -9, 10, -10, 11, -11, 13,
         -13, 15, -15, 17, -17, 19, -19, 21, -21, 23, -23, 25, -25]
HCAP = [0, 1, -1]
CAPLOOO = []
for a in range(len(CAPLO) - 1):
    CAPLOOO.append((CAPLO[a][0], CAPLO[a][1], CAPLO[a + 1][0], CAPLO[a + 1][1]))
CAPLOOO.append((89, 98, 00, 55))


def creatdata():
    with open('noteketqua.txt', 'r') as f:
        lines = f.readlines()
    cot = 2
    data = np.zeros((100, len(lines) + cot), dtype=int)
    datu = np.zeros((27, len(lines) + cot), dtype=int)
    date = np.zeros((4, len(lines) + cot), dtype=int)
    de = np.zeros((len(lines) + cot), dtype=int)
    nhat = np.zeros((len(lines) + cot), dtype=int)
    caplo = np.zeros((50, len(lines) + cot), dtype=int)
    caploo = np.zeros((25, len(lines) + cot), dtype=int)
    caplooo = np.zeros((len(CAPLOOO), len(lines) + cot), dtype=int)
    setlo = np.zeros((45, len(lines) + cot), dtype=int)
    for line in reversed(lines):
        # creat date
        ngay = line[:10].split('-')
        date[0, cot] = int(ngay[0])
        date[1, cot] = int(ngay[1])
        date[2, cot] = int(ngay[2])
        date[3, cot] = datetime.date(int(ngay[2]),
                                     int(ngay[1]), int(ngay[0])).weekday() + 2
        # creat lo, caplo
        ketqua = line[10:]
        number = ''
        count = 0
        conde = line[10:12]
        de[cot] = int(conde)
        giainhat = line[12:14]
        nhat[cot] = int(giainhat)
        for i in range(len(ketqua)):
            number += ketqua[i]
            if len(number) == 2:
                # creat lo
                data[int(number), cot] += 1
                datu[count, cot] = int(number)
                count += 1
                # creat caplo
                for _, cap_lo in enumerate(CAPLO):
                    if int(number) in cap_lo:
                        caplo[_, cot] += 1
                # creat caplooo
                for _, cap_looo in enumerate(CAPLOOO):
                    if int(number) in cap_looo:
                        caplooo[_, cot] += 1
                # creat caploo
                for _, cap_loo in enumerate(CAPLOO):
                    if int(number) in cap_loo:
                        caploo[_, cot] += 1
                # creat setlo
                for _, set_lo in enumerate(SETLO):
                    if int(number) in set_lo:
                        setlo[_, cot] += 1
                number = ''
        cot += 1  # set to next column
    return date, data, caplo, de, nhat, datu, setlo, caploo, caplooo


deta = creatdata()


bangdate = deta[0]
banglo = deta[1]
bangcaplo = deta[2]
bangde = deta[3]
bangnhat = deta[4]
daylo = deta[5]
setlo = deta[6]
caploo = deta[7]
caplooo = deta[8]

df = pd.DataFrame(data=banglo)
df.to_csv('banglo.csv', index=False)
df = pd.DataFrame(data=daylo)
df.to_csv('daylo.csv', index=False)
df = pd.DataFrame(data=setlo, index=SETLO)
df.to_csv('setlo.csv')
df = pd.DataFrame(data=caploo, index=CAPLOO)
df.to_csv('caploo.csv')
df = pd.DataFrame(data=caplooo, index=CAPLOOO)
df.to_csv('caplooo.csv')


def addngay():
    ngay = datetime.date(bangdate[2, 2], bangdate[1, 2], bangdate[0, 2]) + datetime.timedelta(days=1)
    thu = ngay.weekday() + 2
    ngay = str(ngay).split('-')
    bangdate[0, 1] = int(ngay[2])
    bangdate[1, 1] = int(ngay[1])
    bangdate[2, 1] = int(ngay[0])
    bangdate[3, 1] = thu


addngay()


def timxeo(number, huong, chieu):
    if chieu is True:
        xeo = number + huong
    else:
        xeo = number - huong
    xeo = xeo % 100
    return xeo


def timbat(number, huong, chieu):
    if chieu is True:
        xeo = number + huong
    else:
        xeo = number - huong
    if xeo < 0:
        xeo = - xeo
        huong = - huong
    if xeo > 99:
        xeo = 99 - (xeo - 99)
        huong = - huong
    return xeo, huong


def timlon(number):
    j = None
    for i in CAPLO:
        if number in i:
            i = list(i)
            i.remove(number)
            j = i[0]
            break
    return j


def timbatcon(number, ngay, huong):
    bat = timbat(number, huong, False)
    numcon = bat[0]
    huong = bat[1]
    ngaycon = ngay + 1
    gancon = 0
    while banglo[numcon, ngaycon] == 0:
        bat = timbat(numcon, huong, False)
        numcon = bat[0]
        huong = bat[1]
        ngaycon += 1
        gancon += 1
    return numcon, gancon, ngaycon


def timcon(number, ngay, huong):
    numcon = timxeo(number, huong, False)
    ngaycon = ngay + 1
    gancon = 0
    while banglo[numcon, ngaycon] == 0:
        numcon = timxeo(numcon, huong, False)
        ngaycon += 1
        gancon += 1
    return numcon, gancon, ngaycon


def tansuat(number, ngay, tail, huong):
    listtail = []
    numcon = number
    ngaycon = ngay
    while len(listtail) < tail:
        x = timcon(numcon, ngaycon, huong)
        gan = x[1]
        ngaycon = x[2]
        numcon = x[0]
        listtail.append(gan)
    return listtail


def timxeocap(number, huong, chieu):
    if chieu is True:
        xeo = number + huong
    else:
        xeo = number - huong
    xeo = xeo % 50
    return xeo


def timconcap(number, ngay, huong):
    numcon = timxeocap(number, huong, False)
    ngaycon = ngay + 1
    gancon = 0
    while bangcaplo[numcon, ngaycon] == 0:
        numcon = timxeocap(numcon, huong, False)
        ngaycon += 1
        gancon += 1
    return numcon, gancon, ngaycon


def tansuatcap(capid, ngay, tail, huong):
    listtail = []
    numcon = capid
    ngaycon = ngay
    while len(listtail) < tail:
        x = timconcap(numcon, ngaycon, huong)
        gan = x[1]
        ngaycon = x[2]
        numcon = x[0]
        listtail.append(gan)
    return listtail


def timsetxeo(number, huong, chieu):
    if chieu is True:
        xeo = number + huong
    else:
        xeo = number - huong
    xeo = xeo % 45
    return xeo


def timsetcon(number, ngay, huong):
    numcon = timsetxeo(number, huong, False)
    ngaycon = ngay + 1
    gancon = 0
    while setlo[numcon, ngaycon] == 0:
        numcon = timsetxeo(numcon, huong, False)
        ngaycon += 1
        gancon += 1
    return numcon, gancon, ngaycon


def khaosetgan(ngay, ganmin, ganmax):
    # listgan = [number],[ketqua],[huong],[gan],[boom],[xeo],[boomxeo],[lon],[boomlon]
    listhuong = [], [], [], []
    listgan = [], [], [], []
    for huong in HCAP:
        for number in range(45):
            gan = timsetcon(number, ngay, huong)[1]
            if gan in range(ganmin, ganmax+1):
                listhuong[0].append(SETLO[number])
                listhuong[1].append(setlo[number, ngay])
                listhuong[2].append(huong)
                listhuong[3].append(gan)
    if len(listhuong[0]) > 0:
        for ganid in range(ganmax, ganmin - 1, -1):
            for i, gan in enumerate(listhuong[3]):
                if gan == ganid:
                    listgan[0].append(listhuong[0][i])
                    listgan[1].append(listhuong[1][i])
                    listgan[2].append(listhuong[2][i])
                    listgan[3].append(listhuong[3][i])
    return listgan, listhuong


def khaogan(ngay, ganmin, ganmax):
    # listgan = [number],[ketqua],[huong],[gan],[boom],[xeo],[boomxeo],[lon],[boomlon]
    listhuong = [], [], [], [], [], [], [], [], []
    listgan = [], [], [], [], [], [], [], [], []
    listnum = [], [], [], [], [], [], [], [], []
    ganzero = [], [], [], [], []
    for huong in HUONG:
        for number in range(100):
            gan = timcon(number, ngay, huong)[1]
            if huong == 0:
                if gan >= 10:
                    ganzero[0].append(number)
                    ganzero[1].append(banglo[number, ngay])
                    ganzero[2].append(timlon(number))
                    ganzero[3].append(banglo[timlon(number), ngay])
                    ganzero[4].append(gan)
            if gan in range(ganmin, ganmax+1):
                listhuong[0].append(number)
                listhuong[1].append(banglo[number, ngay])
                listhuong[2].append(huong)
                listhuong[3].append(gan)
                listhuong[5].append(timxeo(number, huong, True))
                listhuong[6].append(banglo[timxeo(number, huong, True), ngay])
                listhuong[7].append(timlon(number))
                listhuong[8].append(banglo[timlon(number), ngay])
    ganzezo = [], [], [], [], []
    if len(ganzero[0]) > 0:
        for ganid in range(ganmax, 9, -1):
            for i, gan in enumerate(ganzero[4]):
                if gan == ganid:
                    ganzezo[0].append(ganzero[0][i])
                    ganzezo[1].append(ganzero[1][i])
                    ganzezo[2].append(ganzero[2][i])
                    ganzezo[3].append(ganzero[3][i])
                    ganzezo[4].append(ganzero[4][i])
    if len(listhuong[0]) > 0:
        for ganid in range(ganmax, ganmin - 1, -1):
            for i, gan in enumerate(listhuong[3]):
                if gan == ganid:
                    listgan[0].append(listhuong[0][i])
                    listgan[1].append(listhuong[1][i])
                    listgan[2].append(listhuong[2][i])
                    listgan[3].append(listhuong[3][i])
                    listgan[5].append(listhuong[5][i])
                    listgan[6].append(listhuong[6][i])
                    listgan[7].append(listhuong[7][i])
                    listgan[8].append(listhuong[8][i])
        for num in range(100):
            for i, number in enumerate(listhuong[0]):
                if number == num:
                    listnum[0].append(listhuong[0][i])
                    listnum[1].append(listhuong[1][i])
                    listnum[2].append(listhuong[2][i])
                    listnum[3].append(listhuong[3][i])
                    listnum[5].append(listhuong[5][i])
                    listnum[6].append(listhuong[6][i])
                    listnum[7].append(listhuong[7][i])
                    listnum[8].append(listhuong[8][i])
    return listgan, listhuong, listnum, ganzezo


def double(ngay):
    listnum = [], []
    listxeo = [], []
    x = khaogan(ngay, 22, 35)[2]
    for num in x[0]:
        if x[0].count(num) > 1 and num not in listnum[0]:
            listnum[0].append(num)
            listnum[1].append(banglo[num, ngay])
    for num in x[5]:
        if x[5].count(num) > 1 and num not in listxeo[0]:
            listxeo[0].append(num)
            listxeo[1].append(banglo[num, ngay])
    return listnum, listxeo


def twin(ngay):
    listnum = [], []
    listxeo = [], []
    listhuong = []
    listgan = []
    x = khaogan(ngay, 22, 35)[1]
    for i, huong in enumerate(x[2]):
        if x[2].count(huong) > 1 and huong not in listnum[0]:
            listnum[0].append(x[0][i])
            listnum[1].append(x[1][i])
            listxeo[0].append(x[5][i])
            listxeo[1].append(x[6][i])
            listhuong.append(huong)
            listgan.append(x[3][i])
    return listnum, listxeo, listhuong, listgan


def capngon(ngay, huong, pick):
    numlist = [], [], []
    for capid in range(50):
        x = tansuatcap(capid, ngay, 100, huong)
        templist = []
        for i in x:
            if i < 2:
                templist.append(i)
            else:
                break
        numlist[0].append(CAPLO[capid])
        numlist[1].append(bangcaplo[capid, ngay])
        numlist[2].append(len(templist))

    mumlist = [], [], []
    for _ in range(5):
        getmaxid = numlist[2].index(max(numlist[2]))
        mumlist[0].append(numlist[0].pop(getmaxid))
        mumlist[1].append(numlist[1].pop(getmaxid))
        mumlist[2].append(numlist[2].pop(getmaxid))

    picklist = [], [], []
    for i, cap in enumerate(mumlist[0]):
        if i == pick - 1:
            picklist[0].append(cap[0])
            picklist[0].append(cap[1])
            picklist[1].append(banglo[cap[0], ngay])
            picklist[1].append(banglo[cap[1], ngay])
    return picklist


def hangngon(ngay, huong, soluong):
    numlist = [], [], []
    listnum = [i for i in range(100)]
    random.shuffle(listnum)
    for number in listnum:
        x = tansuat(number, ngay, 100, huong)
        templist = []
        for i in x:
            if i < 3:
                templist.append(i)
            else:
                break
        numlist[0].append(number)
        numlist[1].append(banglo[number, ngay])
        numlist[2].append(len(templist))

    mumlist = [], [], []
    for _ in range(soluong):
        getmaxid = numlist[2].index(max(numlist[2]))
        mumlist[0].append(numlist[0].pop(getmaxid))
        mumlist[1].append(numlist[1].pop(getmaxid))
        mumlist[2].append(numlist[2].pop(getmaxid))

    lonlist = [], []
    for num in mumlist[0]:
        lonlist[0].append(timlon(num))
        lonlist[1].append(banglo[timlon(num), ngay])

    return mumlist, lonlist


def hangcapngon(ngay, huong, soluong):
    numlist = [], [], []
    listnum = [i for i in range(50)]
    random.shuffle(listnum)
    for number in listnum:
        x = tansuatcap(number, ngay, 50, huong)
        templist = []
        for i in x:
            if i < 3:
                templist.append(i)
            else:
                break
        numlist[0].append(number)
        numlist[1].append(bangcaplo[number, ngay])
        numlist[2].append(len(templist))
    mumlist = [], [], [], []
    for _ in range(soluong):
        getmaxid = numlist[2].index(max(numlist[2]))
        mumlist[0].append(numlist[0].pop(getmaxid))
        mumlist[1].append(numlist[1].pop(getmaxid))
        mumlist[2].append(numlist[2].pop(getmaxid))
    for i in mumlist[0]:
        mumlist[3].append(CAPLO[i])
    return mumlist


def hanggan(ngay, soluong):
    x = khaogan(ngay, 22, 35)[0]
    mumlist = [], [], []
    for i in range(soluong):
        mumlist[0].append(x[0][i])
        mumlist[1].append(x[1][i])
    return mumlist


def nitendo(ngay):
    listnite = [], []
    for number in range(100):
        if number in daylo[0:28, ngay + 2]:
            if timxeo(number, 1, True) in daylo[0:28, ngay + 1] and timxeo(number, -1, True) in daylo[0:28, ngay + 1]:
                listnite[0].append(number)
                listnite[1].append(banglo[number, ngay])
    return listnite


def khaosetfour():
    textfourgan = ''
    for i in range(100, 0, -1):
        x = khaosetgan(i, 4, 10)[0]
        textfourgan += '\n' + 'Ngày: ' + str(bangdate[0, i]) + '/' + str(bangdate[1, i]) + '/' + str(
          bangdate[2, i]) + ' ĐB: ' + str(bangde[i]) + '\n' + 'sum: ' + str(len(x[3])) + '\n' + 'gan: ' + str(
          x[3][:10]) + '\n' + 'result: ' + str(x[1][:10]) + '\n' + 'hướng: ' + str(x[2][:10]) + '\n' + 'cặp: ' + str(
          x[0][:5]) + '\n'
    return textfourgan


def toptext(huong):
    texttop = ''
    for i in range(100, 0, -1):
        x = hangngon(i, huong, 3)
        if bangde[i] in x[0][0]:
            dbstat = ' hit N '
        elif bangde[i] in x[1][0]:
            dbstat = ' hit L '
        else:
            dbstat = ' fail '
        texttop += '\n' + 'Ngày: ' + str(bangdate[0, i]) + '/' + str(bangdate[1, i]) + '/' + str(
          bangdate[2, i]) + dbstat + ' ĐB: ' + str(bangde[i]) + '\n' + str(x) + '\n'
    return texttop


def twintext():
    texttwin = ''
    for i in range(100, 0, -1):
        x = twin(i)
        if bangde[i] in x[0][0]:
            dbstat = ' hit '
        elif bangde[i] in x[1][0]:
            dbstat = ' hit '
        else:
            dbstat = ' fail '
        texttwin += '\n' + 'Ngày: ' + str(bangdate[0, i]) + '/' + str(bangdate[1, i]) + '/' + str(
          bangdate[2, i]) + dbstat + ' ĐB: ' + str(bangde[i]) + '\n' + str(x) + '\n'
    return texttwin


def khaogantext(ganmin):
    textkhaogan = ''
    for i in range(100, 0, -1):
        x = khaogan(i, ganmin, 50)[0]
        if bangde[i] in x[0]:
            dbstat = ' hit N '
        elif bangde[i] in x[5]:
            dbstat = ' hit X '
        elif bangde[i] in x[7]:
            dbstat = ' hit L '
        else:
            dbstat = ' fail '
        textkhaogan += '\n' + 'Ngày: ' + str(bangdate[0, i]) + '/' + str(bangdate[1, i]) + '/' + str(
          bangdate[2, i]) + dbstat + ' ĐB: ' + str(bangde[i]) + ' sum: ' + str(len(x[0])) + '\n' + 'Number: ' + str(
          x[0]) + '\n' + 'result: ' + str(x[1]) + '\n' + 'hướng: ' + str(x[2]) + '\n' + 'gan: ' + str(
          x[3]) + '\n' + 'xeo: ' + str(x[5]) + '\n' + 'result xeo: ' + str(x[6]) + '\n' + 'lộn: ' + str(
          x[7]) + '\n' + 'result lộn: ' + str(x[8]) + '\n'
    return textkhaogan


def zerotext():
    textzero = ''
    for i in range(100, 0, -1):
        x = khaogan(i, 30, 50)[3]
        if bangde[i] in x[0]:
            dbstat = ' hit N '
        elif int(bangde[i]) in x[2]:
            dbstat = ' hit L '
        else:
            dbstat = ' fail '
        textzero += '\n' + 'Ngày: ' + str(bangdate[0, i]) + '/' + str(bangdate[1, i]) + '/' + str(
            bangdate[2, i]) + dbstat + ' ĐB: ' + str(bangde[i]) + ' sum: ' + str(len(x[0])) + '\n' + 'Number: ' + str(
            x[0]) + '\n' + 'result: ' + str(x[1]) + '\n' + 'gan: ' + str(x[4]) + '\n' + 'lộn: ' + str(
            x[2]) + '\n' + 'result lộn: ' + str(x[3]) + '\n'
    return textzero


class Mainscreenmanager(ScreenManager):
    dateindex = 2
    
    def print_forward(self):
        ketqua = daylo[0:27, self.dateindex]
        self.ids.ngay.text = "Ngày: " + str(bangdate[0, self.dateindex]) + '/' + str(
          bangdate[1, self.dateindex]) + '/' + str(bangdate[2, self.dateindex])
        for i, x in enumerate(self.ids.values()):
            if i in range(1, 28):
                x.text = str(ketqua[i-1])
        if self.dateindex > 2:
            self.dateindex -= 1
        else:
            self.dateindex = 2
        return

    def print_backward(self):
        ketqua = daylo[0:27, self.dateindex]
        self.ids.ngay.text = "Ngày: " + str(bangdate[0, self.dateindex]) + '/' + str(
          bangdate[1, self.dateindex]) + '/' + str(bangdate[2, self.dateindex])
        for i, x in enumerate(self.ids.values()):
            if i in range(1, 28):
                x.text = str(ketqua[i-1])
        self.dateindex += 1
        return
    
    def layketqua(self, kqngay):
        diachi = 'http://ketqua.net/xo-so-truyen-thong.php?ngay=' + kqngay
        response = requests.get(diachi)
        data = response.text
        listketqua = ''
        count = 0
        for i in range(len(data)):
            if data[i:i + 11] == 'data-sofar=':
                if count > 0:
                    x = data[i:i + 18]
                    x = x.split('"')
                    result = x[1]
                    listketqua += result[-2:]
                count += 1
        return listketqua
    
    def crawler(self):
        with open('noteketqua.txt', 'r') as f:
            data = f.readlines()
            delta = datetime.timedelta(days=1)
            suptime = datetime.timedelta(hours=18, minutes=30)
            end_date = datetime.datetime.now()
            start_date = datetime.datetime(int(data[len(data) - 1][6:10]),
                                           int(data[len(data) - 1][3:5]),
                                           int(data[len(data) - 1][0:2])) + delta + suptime
        while start_date <= end_date:
            kqngay = start_date.strftime("%d-%m-%Y")
            ketqua = self.layketqua(kqngay)
            if len(ketqua) != 0:
                data.append(kqngay + str(ketqua) + '\n')
            start_date += delta
        if data[len(data) - 1][10:] == data[len(data) - 2][10:]:
            data = data[:-1]
        with open('noteketqua.txt', 'w') as f:
            f.writelines(data)
        return
    
    def showgan(self):
        self.ids.ganinput.text = khaogantext(22)
    
    def showmax(self):
        self.ids.maxinput.text = khaogantext(30)
    
    def showfour(self):
        self.ids.fourinput.text = khaosetfour()
    
    def showtop(self):
        self.ids.topinput.text = toptext(0)
    
    def showtopup(self):
        self.ids.topupinput.text = toptext(1)
    
    def showtopdown(self):
        self.ids.topdowninput.text = toptext(-1)
    
    def showtwin(self):
        self.ids.twininput.text = twintext()

    def showzero(self):
        self.ids.zeroinput.text = zerotext()


class MainApp(App):
    pass


MainApp().run()
