# """
# if-elif-else
# < Küçüktür
# > Büyüktür
# == Eşit mi
# || or veya
# and &&  ve
# != Eşit Değil
# """
# """ 
# # yas=int(input("Lütfen Yaşınızı Giriniz "))
# # if yas<18:
# #     print("Bu Mekana Giremezsiniz!")
# # else:
# #     print("Mekanımıza Hoşgeldiniz!")
#  """"

sayi1=int(input("Lütfen Birinci Sayıyı Giriniz!"))
sayi2=int(input("Lütfen İkinci Sayıyı Giriniz!"))
if sayi1>sayi2:
    print("{} {} den büyüktür ".format(sayi1,sayi2))
elif sayi1<sayi2:
    print("{} {} den küçüktür ".format(sayi2,sayi1))
else:
    print("{} ve {} eşittir  ".format(sayi1,sayi2))


