import pyAesCrypt, os, string, random, sys, atexit

def sifre_ekle(veri):
    file_object = open('password.json', 'a')
    file_object.write(veri)
    file_object.close()
# encrypt
def kriptola_dosya(filename, password):
    pyAesCrypt.encryptFile(filename, "" + str(filename).replace(".json", "") + ".crypt", password)
# decrypt
def dekriptola_dosya(filename, password):
    pyAesCrypt.decryptFile(str(filename), "" + str(filename).replace(".crypt", "") + ".json", password)

def cikis(password):
    kriptola_dosya("password.json", password)
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clean')
  
def kripto():
    if(os.path.exists("password.crypt")):
        print("1)Add Password\n2)Show Passwords")
        tip = input()
        if(str(tip) == "1"):
            print("Please enter the admin password : ")
            admin = input()
            dekriptola_dosya("password.crypt", admin)
            os.remove("password.crypt")
            print("Please write your new password's tag : ")
            sifread = input()
            print("Please write your password (this password will be store) : ")
            sifre = input()
            sifre_ekle('Adı : ' + sifread + ' | Şifresi : ' + sifre + '\n')
            kriptola_dosya("password.json", admin)
            os.remove("password.json")
            clear()
            print("Password Added.")
        else:
            print("Please enter the admin password : ")
            admin = input()
            dekriptola_dosya("password.crypt", admin)
            os.remove("password.crypt")
            with open('password.json') as f:
                lines = f.readlines()
                print(lines)
        kriptola_dosya("password.json", admin)
        os.remove("password.json")
        os.system("pause") 
    else:
        print("Files are creating...")
        file_object = open('password.json', 'a')
        file_object.write('')
        file_object.close()
        sifre_ekle('')
        print("Please enter the admin password : ")
        admin = input()
        kriptola_dosya("password.json", admin)
        os.remove("password.json")
        clear()
        print("Program are ready.")

kripto()