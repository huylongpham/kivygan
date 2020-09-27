import numpy as np
import requests
import datetime
import random
def layketqua(ngay):
    diachi = 'http://ketqua.net/xo-so-truyen-thong.php?ngay=' + ngay
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


def crawler(songay):
    delta = datetime.timedelta(days=1)
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    if hour >= 18 and minute > 30:
        end_date = datetime.date.today()
    else:
        end_date = datetime.date.today() - delta

    start_date = end_date - datetime.timedelta(days=songay)


    data = []
    while start_date <= end_date:
        ngay = start_date.strftime("%d-%m-%Y")
        ketqua = layketqua(ngay)
        if len(ketqua) != 0:
            data.append(ngay + str(ketqua) + '\n')
        start_date += delta
    if data[len(data) - 1][10:] == data[len(data) - 2][10:]:
        data = data[:-1]
    with open('noteketqua.txt', 'w') as f:
        f.writelines(data)
    return



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
        DE = line[10:12]
        de[cot] = int(DE)
        G1 = line[12:14]
        nhat[cot] = int(G1)
        for i in range(len(ketqua)):
            number += ketqua[i]
            if len(number) == 2:
                # creat lo
                data[int(number), cot] += 1
                datu[count, cot] = int(number)
                count += 1
                # creat caplo
                for i, cap_lo in enumerate(CAPLO):
                    if int(number) in cap_lo:
                        caplo[i, cot] += 1
                # creat caplooo
                for i, cap_looo in enumerate(CAPLOOO):
                    if int(number) in cap_looo:
                        caplooo[i, cot] += 1
                # creat caploo
                for i, cap_loo in enumerate(CAPLOO):
                    if int(number) in cap_loo:
                        caploo[i, cot] += 1
                # creat setlo
                for i, set_lo in enumerate(SETLO):
                    if int(number) in set_lo:
                        setlo[i, cot] += 1
                number = ''
        cot += 1  # set to next column
    return date, data, caplo, de, nhat, datu, setlo, caploo, caplooo


DATA = creatdata()
bangdate = DATA[0]
banglo = DATA[1]
bangcaplo = DATA[2]
bangde = DATA[3]
bangnhat = DATA[4]
daylo = DATA[5]
setlo = DATA[6]
caploo = DATA[7]
caplooo = DATA[8]

limited = len(bangde)

def addngay():
    ngay = datetime.date(bangdate[2, 2], bangdate[1, 2], bangdate[0, 2]) + datetime.timedelta(days=1)
    thu = ngay.weekday() + 2
    ngay = str(ngay).split('-')
    bangdate[0, 1] = int(ngay[2])
    bangdate[1, 1] = int(ngay[1])
    bangdate[2, 1] = int(ngay[0])
    bangdate[3, 1] = thu
addngay()

#--------------------------------------------------

def timdate(ngay, thang, nam):
    x = 0
    for i in range(len(bangdate[0])):
        if bangdate[2, i] == nam:
            if bangdate[1, i] == thang:
                if bangdate[0, i] == ngay:
                    x = i
                    break
    return x


def timngay(ngay, thang, nam):
    x = 0
    for i in range(len(datechance[0])):
        if datechance[2, i] == nam:
            if datechance[1, i] == thang:
                if datechance[0, i] == ngay:
                    x = i
                    break
    return x


def timxeo(number, huong, chieu):
    if chieu == True:
        xeo = number + huong
    else:
        xeo = number - huong
    xeo = xeo % 100
    return xeo


def timbat(number, huong, chieu):
    if chieu == True:
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
    for i in CAPLO:
        if number in i:
            i = list(i)
            i.remove(number)
            break
    return i[0]


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
    while ngaycon < 100 and banglo[numcon, ngaycon] == 0:
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


def timxeoCap(number, huong, chieu):
    if chieu == True:
        xeo = number + huong
    else:
        xeo = number - huong
    xeo = xeo % 50
    return xeo


def timconCap(number, ngay, huong):
    numcon = timxeoCap(number, huong, False)
    ngaycon = ngay + 1
    gancon = 0
    while bangcaplo[numcon, ngaycon] == 0:
        numcon = timxeoCap(numcon, huong, False)
        ngaycon += 1
        gancon += 1
    return numcon, gancon, ngaycon


def tansuatCap(capid, ngay, tail, huong):
    listtail = []
    numcon = capid
    ngaycon = ngay
    while len(listtail) < tail:
        x = timconCap(numcon, ngaycon, huong)
        gan = x[1]
        ngaycon = x[2]
        numcon = x[0]
        listtail.append(gan)
    return listtail

# --------------------------------------------------

def timsetxeo(number, huong, chieu):
    if chieu == True:
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
            if gan >= ganmin and gan <= ganmax:
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
#--------------------------------------------------
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
            if gan >= ganmin and gan <= ganmax:
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
        x = tansuatCap(capid, ngay, 100, huong)
        templist = []
        for i in x:
            if i < 2:
                templist.append(i)
            else:
                break
        numlist[0].append(CAPLO[capid])
        numlist[1].append(bangcaplo[capid, ngay])
        numlist[2].append(len(templist))
    getmaxid = numlist[2].index(max(numlist[2]))

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
    NUM = [i for i in range(100)]
    random.shuffle(NUM)
    for number in NUM:
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
    NUM = [i for i in range(50)]
    random.shuffle(NUM)
    for number in NUM:
        x = tansuatCap(number, ngay, 50, huong)
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
#---------------------------------------------

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window
Window.size = (1440/4, 3200/4)



class Mainscreen(Screen):
    def getresult(self):
        crawler(100)
        return


class Ganscreen(Screen):
    ngay = ObjectProperty(None)
    number = ObjectProperty(None)
    ketqua = ObjectProperty(None)
    gan = ObjectProperty(None)
    huong = ObjectProperty(None)
    xeo = ObjectProperty(None)
    kqxeo = ObjectProperty(None)
    indexngay = 2
    def backbut(self):
        self.indexngay += 1
        bienkhaogan = khaogan(self.indexngay, 22, 50)[0]
        self.ngay.text = 'gan ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0])
        self.ketqua.text = str(bienkhaogan[1])
        self.gan.text = str(bienkhaogan[3])
        self.huong.text = str(bienkhaogan[2])
        self.xeo.text = str(bienkhaogan[5])
        self.kqxeo.text = str(bienkhaogan[6])

        return

    def nextbut(self):
        self.indexngay -= 1
        if self.indexngay < 1:
            self.indexngay = 1
        bienkhaogan = khaogan(self.indexngay, 22, 50)[0]
        self.ngay.text = 'gan ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0])
        self.ketqua.text = str(bienkhaogan[1])
        self.gan.text = str(bienkhaogan[3])
        self.huong.text = str(bienkhaogan[2])
        self.xeo.text = str(bienkhaogan[5])
        self.kqxeo.text = str(bienkhaogan[6])

        return


class Twinscreen(Screen):
    ngay = ObjectProperty(None)
    number = ObjectProperty(None)
    ketqua = ObjectProperty(None)
    gan = ObjectProperty(None)
    huong = ObjectProperty(None)
    xeo = ObjectProperty(None)
    kqxeo = ObjectProperty(None)
    indexngay = 2

    def backbut(self):
        self.indexngay += 1
        bienkhaogan = twin(self.indexngay)
        self.ngay.text = 'twin ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0][0])
        self.ketqua.text = str(bienkhaogan[0][1])
        self.gan.text = str(bienkhaogan[3])
        self.huong.text = str(bienkhaogan[2])
        self.xeo.text = str(bienkhaogan[1][0])
        self.kqxeo.text = str(bienkhaogan[1][1])

        return

    def nextbut(self):
        self.indexngay -= 1
        if self.indexngay < 1:
            self.indexngay = 1
        bienkhaogan = twin(self.indexngay)
        self.ngay.text = 'twin ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0][0])
        self.ketqua.text = str(bienkhaogan[0][1])
        self.gan.text = str(bienkhaogan[3])
        self.huong.text = str(bienkhaogan[2])
        self.xeo.text = str(bienkhaogan[1][0])
        self.kqxeo.text = str(bienkhaogan[1][1])

        return

class Maxganscreen(Screen):
    ngay = ObjectProperty(None)
    number = ObjectProperty(None)
    ketqua = ObjectProperty(None)
    gan = ObjectProperty(None)
    huong = ObjectProperty(None)
    xeo = ObjectProperty(None)
    kqxeo = ObjectProperty(None)
    indexngay = 2

    def backbut(self):
        self.indexngay += 1
        bienkhaogan = khaogan(self.indexngay, 30, 50)[0]
        self.ngay.text = 'ganmax ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0])
        self.ketqua.text = str(bienkhaogan[1])
        self.gan.text = str(bienkhaogan[3])
        self.huong.text = str(bienkhaogan[2])
        self.xeo.text = str(bienkhaogan[5])
        self.kqxeo.text = str(bienkhaogan[6])

        return

    def nextbut(self):
        self.indexngay -= 1
        if self.indexngay < 1:
            self.indexngay = 1
        bienkhaogan = khaogan(self.indexngay, 30, 50)[0]
        self.ngay.text = 'ganmax ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0])
        self.ketqua.text = str(bienkhaogan[1])
        self.gan.text = str(bienkhaogan[3])
        self.huong.text = str(bienkhaogan[2])
        self.xeo.text = str(bienkhaogan[5])
        self.kqxeo.text = str(bienkhaogan[6])

        return

class Foursetscreen(Screen):
    ngay = ObjectProperty(None)
    number = ObjectProperty(None)
    ketqua = ObjectProperty(None)
    gan = ObjectProperty(None)
    huong = ObjectProperty(None)

    indexngay = 2

    def backbut(self):
        self.indexngay += 1
        bienkhaogan = khaosetgan(self.indexngay, 4, 15)[0]
        self.ngay.text = 'fourset ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0])
        self.ketqua.text = str(bienkhaogan[1])
        self.gan.text = str(bienkhaogan[3])
        self.huong.text = str(bienkhaogan[2])


        return

    def nextbut(self):
        self.indexngay -= 1
        if self.indexngay < 1:
            self.indexngay = 1
        bienkhaogan = khaosetgan(self.indexngay, 4, 15)[0]
        self.ngay.text = 'fourset ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0])
        self.ketqua.text = str(bienkhaogan[1])
        self.gan.text = str(bienkhaogan[3])
        self.huong.text = str(bienkhaogan[2])

        return

class Topscreen(Screen):
    ngay = ObjectProperty(None)
    number = ObjectProperty(None)
    ketqua = ObjectProperty(None)
    tail = ObjectProperty(None)
    lon = ObjectProperty(None)
    kqlon = ObjectProperty(None)
    indexngay = 2

    def backbut(self):
        self.indexngay += 1
        bienkhaogan = hangngon(self.indexngay, 0, 3)
        self.ngay.text = 'top ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0][0])
        self.ketqua.text = str(bienkhaogan[0][1])
        self.tail.text = str(bienkhaogan[0][2])
        self.lon.text = str(bienkhaogan[1][0])
        self.kqlon.text = str(bienkhaogan[1][1])
        return

    def nextbut(self):
        self.indexngay -= 1
        if self.indexngay < 1:
            self.indexngay = 1
        bienkhaogan = hangngon(self.indexngay, 0, 3)
        self.ngay.text = 'top ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0][0])
        self.ketqua.text = str(bienkhaogan[0][1])
        self.tail.text = str(bienkhaogan[0][2])
        self.lon.text = str(bienkhaogan[1][0])
        self.kqlon.text = str(bienkhaogan[1][1])
        return

class Topupscreen(Screen):
    ngay = ObjectProperty(None)
    number = ObjectProperty(None)
    ketqua = ObjectProperty(None)
    tail = ObjectProperty(None)
    lon = ObjectProperty(None)
    kqlon = ObjectProperty(None)
    indexngay = 2

    def backbut(self):
        self.indexngay += 1
        bienkhaogan = hangngon(self.indexngay, 1, 3)
        self.ngay.text = 'topup ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0][0])
        self.ketqua.text = str(bienkhaogan[0][1])
        self.tail.text = str(bienkhaogan[0][2])
        self.lon.text = str(bienkhaogan[1][0])
        self.kqlon.text = str(bienkhaogan[1][1])
        return

    def nextbut(self):
        self.indexngay -= 1
        if self.indexngay < 1:
            self.indexngay = 1
        bienkhaogan = hangngon(self.indexngay, 1, 3)
        self.ngay.text = 'topup ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0][0])
        self.ketqua.text = str(bienkhaogan[0][1])
        self.tail.text = str(bienkhaogan[0][2])
        self.lon.text = str(bienkhaogan[1][0])
        self.kqlon.text = str(bienkhaogan[1][1])

class Topdownscreen(Screen):
    ngay = ObjectProperty(None)
    number = ObjectProperty(None)
    ketqua = ObjectProperty(None)
    tail = ObjectProperty(None)
    lon = ObjectProperty(None)
    kqlon = ObjectProperty(None)
    indexngay = 2

    def backbut(self):
        self.indexngay += 1
        bienkhaogan = hangngon(self.indexngay, -1, 3)
        self.ngay.text = 'topdown ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0][0])
        self.ketqua.text = str(bienkhaogan[0][1])
        self.tail.text = str(bienkhaogan[0][2])
        self.lon.text = str(bienkhaogan[1][0])
        self.kqlon.text = str(bienkhaogan[1][1])
        return

    def nextbut(self):
        self.indexngay -= 1
        if self.indexngay < 1:
            self.indexngay = 1
        bienkhaogan = hangngon(self.indexngay, -1, 3)
        self.ngay.text = 'topdown ngay: ' + str(bangdate[0:3, self.indexngay])
        self.number.text = str(bienkhaogan[0][0])
        self.ketqua.text = str(bienkhaogan[0][1])
        self.tail.text = str(bienkhaogan[0][2])
        self.lon.text = str(bienkhaogan[1][0])
        self.kqlon.text = str(bienkhaogan[1][1])

class Screenmanager(ScreenManager):
    pass

my = Builder.load_file('my.kv')

class MyApp(App):
    def build(self):

        return my

if __name__ == '__main__':
    MyApp().run()