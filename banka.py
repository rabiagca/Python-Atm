print("Bankamıza hoşgeldiniz!!!  Yapmak istediğiniz işlemi seçiniz")
while True:
 print("1-Hesap Bakiyesi öğrenme")
 print("2-Para çekmek")
 print("3-Para yatırmak")
 print("4-Çıkış")
 secim=int(input("Seçim yapınız: "))

 bakiye=250

 if secim==1:
     print("Hesap Bakiyesi: ",bakiye)
     continue

 elif secim==2:
     cekilen_tutar=int(input("Çekmek istediğiniz tutarı giriniz: "))
     if cekilen_tutar>bakiye:
         print("Hesap Bakiyesi yetersiz")
     elif bakiye>=cekilen_tutar:
         kalan_bakiye=bakiye-cekilen_tutar
         print("İlk önce kartı sonra paranızı alınız. Kalan Bakiye: " , kalan_bakiye)
         continue

 elif secim==3:
     yatirilan_tutar=int(input("Yatırmak istediğiniz tutarı giriniz: "))
     yeni_bakiye=bakiye+yatirilan_tutar
     print("Toplam hesap bakiyesi: " , yeni_bakiye)
     continue
         
 elif secim==4:
     print("Bizi tercih ettiğinz için teşekkür ederiz.")
     break
         