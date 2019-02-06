import os

def CreateMonthID(mnth, yr):
    result = yr * 100 + mnth
    return result

def GetMonthQtr(mnth, yr):
    if mnth >= 1 and mnth <=3:
        return [1,3]
    elif mnth >= 4 and mnth <=6:
        return [4,6]
    elif mnth >= 7 and mnth <=9:
        return [7,9]
    elif mnth >= 10  and mnth <=12:
        return [10,12]
    else:
        return 0

def GenerateQtr(mnth,yr):
    qtr = GetMonthQtr(mnth,yr)
    sqtr = qtr[0]
    result = [[0] * 2 for k in range(3)]
    i = 0
    j = 0
    while sqtr <= qtr[1]:
        result[i][j] = yr * 100 + mnth
        result[i][j+1] = yr * 100 + sqtr
        sqtr = sqtr + 1
        i = i + 1        
    return result

def GenerateResult(startyear, endyear):
    result = []
    syr = startyear
    while syr <= endyear:
        smnth = 1
        while smnth <= 12:
            qtr = GenerateQtr(smnth,syr)
            for a,b in qtr:
                aa = ",({0},{1})\n".format(a,b)
                result.append(aa)
            smnth = smnth + 1
        syr = syr + 1
    return result

with open("/home/jasont14/monthid20yr.txt", "w") as f:
    qtr = GenerateResult(2010,2019)
    for a in qtr:
        f.write(a)











