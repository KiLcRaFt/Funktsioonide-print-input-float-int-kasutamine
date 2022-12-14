from csv import excel
from html.entities import codepoint2name
from math import *
from random import *
from stringprep import c22_specials
# Esimene Ülesande

#print("Puu läbimõõdu arvutamine") 
#try:
#  C=float(input("Anna ümbermõõt: "))
#  if C>0:
#    d=round(C/pi,2)
#    print(f"Puu läbimõõt = {d}")
#  else:
#    print("C peab olema suurem kui 0")
#except:
#    print("Andmetüüp on vale")

# Teine Ülesasnde

#print("Ristküliku diagonaali arvutamine: ")
#try:
#  n=float(input("Ristküliku esimene külg: "))
#  m=float(input("Ristküliku teine külg: "))
#  if m>0 and n>0:
#      d=round(sqrt(n**2+m**2),2)
#      print(f"Ristkülikukujulise maatüki diagonaal {d}")
#  else:
#      print("Viga")
#except:
#  print("m ja n vaja sisestada float formaadis")

# Kolmas Ülesanne

#try:
#    aeg = float(input("Mitu tundi kulus sõiduks? "))
#    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#    if aeg>0 and teepikkus>0:
#        kiirus = teepikkus / aeg
#        print("Sinu kiirus oli " + str(kiirus) + " km/h")
#    else:
#        print("Viga")
#except:
#    print("Viga")

# Neljadal Ülesanne

#print("Aritmeetiline keskmine")
#try:
#    A1=int(input("Esimene arv: "))
#    A2=int(input("Teine arv: "))
#    A3=int(input("Kolmas arv: "))
#    A4=int(input("Neljas arv: "))
#    A5=int(input("Viies arv: "))
#    answer=(A1+A2+A3+A4+A5)/5
#    print(f"Aritmeetiline keskmine on {answer}")
#except:
#    print("Viga")

# Viies Ülesanne

#print( "   @..@ " )
#print("  (----) ")
#print(" ( \__/ )")
#print("  ^^ "" ^^ ")

#6

#a=randint(0,100)
#b=randint(0,100)
#c=randint(0,100)
#print(f"a={a}\nb={b}\nc={c}")
#answer=a+b+c
#print(f"Ümbermõõt on {answer}")

#7

#P=randint(1,6)
#summa=(12.9*1.1)/P
#print(f"{P}-st, Igaüks maksab {summa}")

#8

#print("Kütusekulu arvutamine")
#try:
#    l=float(input("Kütse liitride kogus: "))
#    km=float(input("Läbitud kilomeetrid: "))
#    if l>0 and km>0:
#        kulu=(l/km)*100
#        print(f"Kütusekulu {kulu}")
#    else:
#        print("Viga")
#except:
#    print("Viga")

#9

#try:
#    M=int(input("Skol´ko exal?\n:"))
#    if M>0:
#        M=M/60
#        tee=M*29.9
#        print(f"Skorost´ravna {tee} km")
#    else:
#        print("Viga")
#except:
#    print("Viga")

#10

#print("Ajateisendus")
#try:
#    M=int(input("Sisesta aja minutites: ")) #1h=60min
#    if M>0:
#        H=M//60
#        M=M%60
#        print(f"{H} : {M}")
#    else:
#        print("Viga")
#except:
#    print("Viga")

#Ülesanne "Ema roobot"

#print("Ema roobot")
#a=input("Sisesta: ")
#print(a.isalpha(), a.isdigit())
#if a.isdigit() and int(a)>=1 and int(a)<=5:
#    a=int(a)
#    if a==5:
#        print("Great")
#    elif a==4:
#        print("Good")
#    elif a==3:
#        print("Ok")
#    elif a==2:
#        print("Bad")
#    else:
#        print("Asta lavista baby")
#else:
#    print("Sa valesti vastas")
