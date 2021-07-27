"""for satir in range(1,11):
    for sutun in range(1,11):
        print(satir*sutun, '\t', end=" ")
    print("\n")"""

print("""****** ATM UYGULAMASI ******
1)BAKİYE SORGULAMA
2)PARA ÇEKME
3)PARA YATIRMA
ÇIKMAK İÇİN Q'YA BASIN.
""")
bakiye = 3000
while True:
    işlem = input("İŞLEM SEÇİN: ")
    if(işlem=="q"):
        print("YİNE BEKLERİZ...")
        break
    elif(işlem=="1"):
        print("BAKİYENİZ {} TL'DİR.".format(bakiye))
    elif(işlem=="2"):
        miktar=int(input("ÇEKMEK İSTEDİĞİNİZ MİKTARI GİRİN: "))
        bakiye-=miktar
    elif(işlem=="3"):
        para=int(input("YATIRMAK İSTEDİĞİNİZ MİKTARI GİRİN: "))
        bakiye+=para
    else:
        print("GEÇERSİZ İŞLEM")





