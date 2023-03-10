import os
from cryptography.fernet import Fernet


def login():
    while True:
        user_name = input("what is your username: ").lower().replace(" ", "")
        password = input(f"what is your password: ").replace(" ", "")
        if user_name == "idan" and password == "123":
            print(f"welcome {user_name}")
            while True:
                what_to_do = in_vault(user_name)
                if what_to_do == "ex":
                    print("bye")
                    break
        else:
            print("try again")


def in_vault(username):
    print("what do you want to do")
    what_to_do = input("[W]rite [E]dit [S]how [D]elete [EN]crypt [DE]crypt [EX]it: ").lower().replace(" ", "")
    if what_to_do == "w":
        WirteFile()
    elif what_to_do == "s":
        PrintFile()
    elif what_to_do == "e":
        FileEditor_first()
    elif what_to_do == "d":
        delete_file()
    elif what_to_do == "en":
        Encrypt_file()
    elif what_to_do == "de":
        Decrypt_file()
    else:
        print("please choose a available option")
    return what_to_do


def delete_file():
    t = "delete file"
    print(f"{t:.^20}")
    file = input("what file you want to delete: ").lower().replace(" ", "") + ".txt"
    if os.path.exists(file):
        os.remove(file)
        print(f"{file} was deleted")
    else:
        print("The file does not exist")


def FileEditor_first():
    t = "edit file"
    print(f"{t:.^20}")
    file = input("what file you want to edit: ").lower().replace(" ", "") + ".txt"
    FileEditor(file)


def PrintFile():
    t = "show a file"
    print(f"{t:.^20}")
    FileName = input("file name: ").replace(" ", "").replace(".txt", "") + ".txt"
    try:
        print("---------------------------------")
        f = open(FileName, "r")
    except:
        print("this file does not exit try to write a new onw")
    else:
        print(f.read())


def WirteFile():
    t = "write a new file"
    print(f"{t:.^20}")
    FileName = input("file name: ").replace(" ", "").replace(".txt", "") + ".txt"
    try:
        f = open(FileName, "x")
    except:
        print("this file already exist try edit or show")
    else:
        print(f"creating a new file: {FileName}")
        FileEditor(FileName)


def FileEditor(FileName):
    f = open(FileName, "a")
    line = 1
    print("if you want to exit editor write EXIT")
    print("if you want see the text write SHOW")
    while True:
        text = input(f"line {line}: ") + "\n"
        if text.replace("\n", "") == "EXIT":
            break
        if text.replace("\n", "") == "SHOW":
            f = open(FileName, "r")
            print(f.read())
            f = open(FileName, "a")
            text = ""
        f.write(text)
        line = line + 1
    f.close()


def Encrypt_file():
    t = "encrypt file"
    print(f"{t:.^20}")
    file_name = input("what file you want to encrypt: ").replace(" ", "").replace(".txt", "") + ".txt"
    try:
        key = read_key()
        fernet = Fernet(key)
    except:
        create_key()
    else:
        try:
            with open(file_name, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(file_name, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        except FileNotFoundError:
            print("this file does not exit")


def Decrypt_file():
    t = "decrypt file"
    print(f"{t:.^20}")
    file_name = input("what file you want to decrypt: ").replace(" ", "").replace(".txt", "") + ".txt"
    try:
        key = read_key()
        fernet = Fernet(key)
    except:
        create_key()
    else:
        try:
            with open(file_name, 'rb') as file:
                encrypted  = file.read()
            decrypted = fernet.decrypt(encrypted)
            with open(file_name, 'wb') as dec_file:
                dec_file.write(decrypted)
        except FileNotFoundError:
            print("this file does not exit")
        except:
            print("file need to be encrypted before decrypted")



def read_key():
    try:
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
            return key
    except:
        print("the key file is empty")


def create_key():
    print("there is no key")
    print("creating a key now")
    key = Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)


login()
