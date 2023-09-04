def caesar_cipher_encrypt(string, key):
    encrypted_string = ""
    proses = string

    for kunci in key:
        encrypted_string = ""
        for char in proses:
            if char.isalpha():  # Periksa apakah karakter adalah huruf
                if kunci.isupper():
                    shift = ord(kunci) - ord('A')  # Menghitung pergeseran berdasarkan urutan karakter kunci
                else:
                    shift = ord(kunci) - ord('a')  # Menghitung pergeseran berdasarkan urutan karakter kunci
                if char.isupper():
                    encrypted_char = chr(((ord(char) - ord('A') + shift)%26 ) + ord('A'))
                else:
                    encrypted_char = chr(((ord(char) - ord('a') + shift)%26 ) + ord('a'))
            else:
                encrypted_char = char
            encrypted_string += encrypted_char
        proses = encrypted_string
    return encrypted_string


# Contoh penggunaan
teks = input("Masukkan teks yang ingin dienkripsi: ")
kunci = input("Masukkan kunci: ")

hasil_enkripsi = caesar_cipher_encrypt(teks, kunci)
print("Teks terenkripsi:", hasil_enkripsi)
