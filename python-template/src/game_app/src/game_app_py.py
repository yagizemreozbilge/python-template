import random

# Adam asmaca oyununda kullanılacak kelime listesi
kelimeler = ['python', 'bilgisayar', 'mühendislik', 'yazılım', 'algoritma']

# Rastgele bir kelime seç
kelime = random.choice(kelimeler)
kelime_uzunlugu = len(kelime)
tahmin_edilenler = ['_'] * kelime_uzunlugu
yanlis_tahminler = 0
maksimum_hata = 6

print("Adam Asmaca Oyununa Hoşgeldiniz!")
print("Bir kelime seçildi. Kelimeyi tahmin etmeye çalışın.")

while True:
    print("\nKelime: ", ' '.join(tahmin_edilenler))
    harf = input("Bir harf tahmin edin: ").lower()

    if len(harf) != 1 or not harf.isalpha():
        print("Lütfen sadece bir harf girin.")
        continue

    if harf in kelime:
        for i in range(kelime_uzunlugu):
            if kelime[i] == harf:
                tahmin_edilenler[i] = harf
        print(f"Doğru! {harf} harfi kelimenin içinde var.")
    else:
        yanlis_tahminler += 1
        print(f"Yanlış! {harf} harfi kelimenin içinde yok. ({yanlis_tahminler}/{maksimum_hata})")

    if '_' not in tahmin_edilenler:
        print(f"Tebrikler! Kelimeyi buldunuz: {kelime}")
        break

    if yanlis_tahminler == maksimum_hata:
        print(f"Üzgünüm, adam asıldı! Kelime: {kelime}")
        break

print("Oyun bitti.")

