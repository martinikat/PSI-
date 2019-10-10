x="Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print(x);

imie = "Mariusz"
nazwisko = "Kołodziejski"

litera1 = x.count(imie[2])
litera2 = x.count(nazwisko[3])

print("W tekscie jest", litera1, "liter 'a' i ", litera2, "liter 'ł'")

print('{} {}'.format('one', 'two'))
print('{:>10}'.format('test'))
print('{:10.5}'.format('xylophone'))
print('{:f}'.format(3.141592653589793))
print('{:{align}{width}}'.format('test', align='^', width='10'))