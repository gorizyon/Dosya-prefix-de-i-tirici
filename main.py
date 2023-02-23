import os

dosyasi_yolu = r"C:\Users\user\Masaüstü\python\server"
eski_prefix = "gaming_"
yeni_prefix = "Cappuccino_"
dosyalar = os.listdir(dosyasi_yolu)
degistirilen_dosya_sayisi = 0
for dosya in dosyalar:
    if dosya.startswith(eski_prefix):
        eski_yol = os.path.join(dosyasi_yolu, dosya)
        yeni_ad = yeni_prefix + dosya[len(eski_prefix):]
        yeni_yol = os.path.join(dosyasi_yolu, yeni_ad)
        os.rename(eski_yol, yeni_yol)
        degistirilen_dosya_sayisi += 1
        print("[+] Doysa Prefixleri Değiştirildi.")
    else:
        print("[-] Dosya Yolu değiştirilemedi. \n Python dosyaları eksik olabilir veya dosya yolun yanlış.")    

print(f"\nToplam {degistirilen_dosya_sayisi} dosya adı değiştirildi.")



devam_et = input("\n\n\nDosya adlarını değiştirdikten sonra programı kapatmak istiyor musunuz? (E/H): ")
if devam_et.upper() == "H":
    input("Program kapatıldı. Çıkmak için bir tuşa basın.")