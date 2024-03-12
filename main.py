#zadanie 1.
ciag = input("Podaj ciag znakow: ")
count = 0

for i in range(0,len(ciag)):
    if ciag[i] == ciag[-1]:
        count += 1

print(count)

#zadanie 2.
def czyPalindrom(ciag):
    temp = ""
    for i in range(1,len(ciag) + 1):
        temp += ciag[-i]
    print(temp)
    if ciag == temp:
        return True
    else:
        return False

ciagPalindrom = input("Podaj ciag znakow: ")
print(czyPalindrom(ciagPalindrom))

#zadanie 3.
slownik = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
}

podanyCiag = input("Podaj ciag znakow: ")
suma = 0

for i in range(0,len(podanyCiag)):
    for j in slownik:
        if podanyCiag[i] == j:
            suma += slownik.get(podanyCiag[i])

print(suma)

#zadanie 4.

def szyfrCezara(ciag, n):
    tempCiag = ""
    for i in range(0, len(ciag)):
        if ord(ciag[i]) + n >= 97 and ord(ciag[i]) + n <= 122:
            tempCiag += chr(ord(ciag[i]) + n)
        elif ord(ciag[i]) + n > 122:
            tempCiag += chr(ord(ciag[i]) + n - 26)
        elif ord(ciag[i]) + n < 97:
            tempCiag += chr(ord(ciag[i]) + n + 26)
    return tempCiag

print(szyfrCezara("abrakadabraz", 2))
print(szyfrCezara("cdtcmcfcdtcb",-2))

#zadanie 5.

def strToInt(str):
    temp = ""
    tempcount = 0
    for i in range(0,len(str)):
        if str[i].isdigit() == True:
            temp += str[i]
        elif (str[i] == "-" or str[i] == "+") and i == 0:
            temp += str[i]
        elif str[i] == "e":
            if int(str[str.index("e") + 1 : len(str)]) < 0:
                return int(str[0:str.index("e")])
            else:
                return int(str[0:str.index("e")]) * 10 ** int(str[str.index("e") + 1: len(str)])
        else:
            break

    if temp == "" or temp == "+":
        return 0
    return int(temp)

print(strToInt("+12"))
print(strToInt("0001"))
print(strToInt("991-234-23"))
print(strToInt("+zonk"))
print(strToInt(""))
print(strToInt("-12e5"))
print(strToInt("-12e-5"))
print(strToInt("-13krowa"))


#zadanie 6.
def czyAnagram(t1 , t2):
    t1 = t1.lower().replace(" ", "")
    t2 = t2.lower().replace(" ", "")

    if len(t1) != len(t2):
        return False

    t1 = sorted(t1)
    t2 = sorted(t2)

    for i in range(0, len(t1)):
        if t1[i] != t2[i]:
            return False

    return True

print(czyAnagram("kolej", "olejk"))
print(czyAnagram("kolej", "kole"))
print(czyAnagram("kolej", "K O L E J"))
print(czyAnagram("Gregory House", "Huge ego, sorry"))



#zadanie 7.

def HTMLColor2RGB(color):
    color = color.strip("#")
    rgb = []
    for i in (0, 2, 4):
        num = int(color[i:i + 2], 16)
        rgb.append(num)

    return rgb

print(HTMLColor2RGB("#FF0050"))
print(HTMLColor2RGB("#001020"))
