#!/usr/bin/pkexec /usr/bin/python3
# test.py
import os

def main():
    print("Bu bir Polkit ile çalıştırılan Python dosyasıdır.")
    os.system("mkdir /de")  # Kullanıcı adını gösterir

if __name__ == "__main__":
    main()

