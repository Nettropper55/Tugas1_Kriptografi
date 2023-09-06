def caesar_cipher_encrypt(string, key):
    encrypted_string = ""
    proses = string
    kunci_steps = []

    for kunci in key.lower():  # Konversi kunci menjadi huruf kecil
        encrypted_string = ""
        for char in proses:
            if char.isalpha():  # Periksa apakah karakter adalah huruf
                if kunci.isupper():
                    shift = ord(kunci) - ord('A')  # Menghitung pergeseran berdasarkan urutan karakter kunci
                else:
                    shift = ord(kunci) - ord('a')  # Menghitung pergeseran berdasarkan urutan karakter kunci
                if char.isupper():
                    encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('a'))  # Konversi menjadi huruf kecil
                else:
                    encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                print("Error: Input mengandung spasi atau angka.")
                return None
            encrypted_string += encrypted_char
        kunci_steps.append(encrypted_string)  # Tambahkan langkah perubahan kunci
        proses = encrypted_string

    # Menampilkan langkah perubahan kunci
    for i, step in enumerate(kunci_steps):
        print(f"Karakter ke-{i+1} kunci: {step} ({key[i]})")

    return encrypted_string

# Contoh penggunaan
teks = input("Masukkan teks yang ingin dienkripsi: ")
kunci = input("Masukkan kunci: ")

hasil_enkripsi = caesar_cipher_encrypt(teks, kunci)
if hasil_enkripsi is not None:
    print("Teks terenkripsi:", hasil_enkripsi)
