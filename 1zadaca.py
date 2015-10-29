Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> visina = 165
>>> visina
165
>>> kucni broj = broj = 245
SyntaxError: invalid syntax
>>> kucni_broj = broj = 245
>>> broj
245
>>> kucni_broj
245
>>> nadimak = "Marija"
>>> nadimak
'Marija'
>>> type (nadimak)
<type 'str'>
>>> print "Iva " + "Pavlovic"
Iva Pavlovic
>>> print "Iva " + "Pavlovic " + str( 5485567569578 )
Iva Pavlovic 5485567569578
>>> broj = 23.4
>>> type (broj)
<type 'float'>
>>> broj = int (23.4)
>>> type (broj)
<type 'int'>
>>> broj = 23345
>>> type (broj)
<type 'int'>
>>> broj = float (23345)
>>> type (broj)
<type 'float'>
>>> 23.4/6
3.9
>>> 8*8
64
>>> 2.4**10
6340.338096537597
>>> voce = input ("Koje je tvoje omiljeno voce: ")
Koje je tvoje omiljeno voce: "naranca"
>>> print voce
naranca
>>> udaljenost = input("Koliko si trcao danas: ")
Koliko si trcao danas: 123
>>> print voce + str(udaljenost)
naranca123
>>> 
