import os
import random

def file_write(file_name, text):
    text = "0-)" + text + "\n"
    with open(file_name, 'wb') as myFile:
        myFile.write(text.encode('utf-8'))
    return 0

def file_read(file_name, print_to_console=True):
    MAX_FILE_SIZE = 4096
    content = ''

    if not os.path.exists(file_name):
        print("File operation failed, There is no record")
        return None

    with open(file_name, 'rb') as myFile:
        content = myFile.read(MAX_FILE_SIZE).decode('utf-8')

    if print_to_console:
        print(content)

    return content

def file_append(file_name, text):
    if not os.path.exists(file_name):
        print("File operation failed")
        return -1

    with open(file_name, 'rb') as myFile:
        lines = myFile.readlines()

    last_line = lines[-1].decode('utf-8') if lines else "0-)\n"
    line_number = int(last_line.split('-)')[0]) + 1
    new_line = f"{line_number}-){text}\n"

    with open(file_name, 'ab') as myFile:
        myFile.write(new_line.encode('utf-8'))

    return 0

def file_edit(file_name, line_number_to_edit, new_line):
    if not os.path.exists(file_name):
        print("File operation failed")
        return -1

    with open(file_name, 'rb') as myFile:
        lines = myFile.readlines()

    if line_number_to_edit > 0 and line_number_to_edit <= len(lines):
        lines[line_number_to_edit - 1] = f"{line_number_to_edit}-){new_line}\n".encode('utf-8')
    else:
        print("You can only edit existing lines")
        return -1

    with open(file_name, 'wb') as myFile:
        myFile.writelines(lines)

    print("Data successfully edited")
    return 0

def file_line_delete(file_name, line_number_to_delete):
    if not os.path.exists(file_name):
        print("File operation failed")
        return -1

    with open(file_name, 'rb') as myFile:
        lines = myFile.readlines()

    if line_number_to_delete > 0 and line_number_to_delete < len(lines):
        del lines[line_number_to_delete - 1]
        for i in range(line_number_to_delete - 1, len(lines)):
            line_content = lines[i].decode('utf-8')
            pos = line_content.find('-)')
            line_number = int(line_content[:pos])
            lines[i] = f"{line_number - 1}{line_content[pos:]}\n".encode('utf-8')
    else:
        print("You can only erase existing lines")
        return -1

    with open(file_name, 'wb') as myFile:
        myFile.writelines(lines)

    print("Data successfully deleted")
    return 0

def user_register(new_username, new_password, new_recovery_key, user_file):
    login_info = f"{new_username}/{new_password}/{new_recovery_key}"
    with open(user_file, 'wb') as myFile:
        myFile.write(login_info.encode('utf-8'))
    return 0

def user_login(username, password, user_file):
    if not os.path.exists(user_file):
        print("\nThere is no user info, Please register first.\n")
        return -1

    with open(user_file, 'rb') as myFile:
        data = myFile.read().decode('utf-8')

    username_read, password_read, recovery_key_read = data.split('/')

    if username == "None" and password == "None":
        username = input("\nPlease enter username:")
        password = input("\nPlease enter password:")

    if username == username_read and password == password_read:
        print("\nLogin Succesfull")
        return 0
    else:
        print("\nWrong username or password")
        return -1

def user_change_password(recovery_key, new_password, user_file):
    if not os.path.exists(user_file):
        print("\nThere is no user info, Please register first.\n")
        return -1

    with open(user_file, 'rb') as myFile:
        data = myFile.read().decode('utf-8')

    username_read, password_read, recovery_key_read = data.split('/')

    if recovery_key == "None":
        recovery_key = input("\nPlease enter your recovery key:")

    if recovery_key == recovery_key_read:
        print("\nRecovery Key Approved\n")
        if new_password == "None":
            new_password = input("\nPlease enter a new password:")

        new_login_info = f"{username_read}/{new_password}/{recovery_key_read}"
        with open(user_file, 'wb') as myFile:
            myFile.write(new_login_info.encode('utf-8'))

        print("\nPassword changed successfully")
        return 0
    else:
        print("\nWrong Recovery Key")
        return -1

def adam_asmaca_grafik(hata_sayisi):
    grafik = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        =========
        """
    ]
    print(grafik[hata_sayisi])

def oyun_oyna():
    kelimeler = ['python', 'bilgisayar', 'mühendislik', 'yazılım', 'algoritma']
    kelime = random.choice(kelimeler)
    kelime_uzunlugu = len(kelime)
    tahmin_edilenler = ['_'] * kelime_uzunlugu
    tahmin_edilen_harfler = set()
    yanlis_tahminler = 0
    maksimum_hata = 6

    print("Adam Asmaca Oyununa Hoşgeldiniz!")
    print("Bir kelime seçildi. Kelimeyi tahmin etmeye çalışın.")

    while True:
        adam_asmaca_grafik(yanlis_tahminler)
        print("\nKelime: ", ' '.join(tahmin_edilenler))
        print(f"Şu ana kadar tahmin edilen harfler: {', '.join(sorted(tahmin_edilen_harfler))}")
        harf = input("Bir harf tahmin edin: ").lower()

        if len(harf) != 1 or not harf.isalpha():
            print("Lütfen sadece bir harf girin.")
            continue

        if harf in tahmin_edilen_harfler:
            print(f"{harf} harfini zaten tahmin ettiniz. Lütfen başka bir harf deneyin.")
            continue

        tahmin_edilen_harfler.add(harf)

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
            adam_asmaca_grafik(yanlis_tahminler)
            print(f"Üzgünüm, adam asıldı! Kelime: {kelime}")
            break

    print("Oyun bitti.")

def main():
    while True:
        oyun_oyna()
        tekrar = input("Tekrar oynamak ister misiniz? (e/h): ").lower()
        if tekrar != 'e':
            print("Oyun sona erdi. Teşekkürler!")
            break

if __name__ == "__main__":
    main()

