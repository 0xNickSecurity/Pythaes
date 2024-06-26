'''
Copyright (c) 2024 0xNickSecurity LUKE6044

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
''' 
#type: ignore


## IMPORTS
import os #for files dirs and paths
import sys #exit func 
from cryptography.fernet import Fernet #AES encryption
from time import sleep #to wait between func-func
from termcolor import colored #for colors in the code

## BANNER
Banner_1 = f"""
                                                              .--------.
                                                             / .------. \    
                                                            / /        \ \            
______ __   __ _____  _   _    ___    _____  _____          | |        | |
| ___ \  \ / /|_   _|| | | |  / _ \  |  ___|/  ___|         | |________| |_        
| |_/ / \ V /   | |  | |_| | / /_\ \ | |__  \ `--.       .' |_|        |_| '.
|  __/   \ /    | |  |  _  | |  _  | |  __|  `--. \\     '._____ ____ _____.'
| |      | |    | |  | | | | | | | | | |___ /\__/ /      |     .'____'.     |
\_|      \_/    \_/  \_| |_/ \_| |_/ \____/ \____/       '.__.'.'    '.'.__.'
{colored('Python Tool With Highly Advanced Encryption Standard', "grey", attrs=["bold"])}     '.__  |      |  __.'
                                                         |   '.'.____.'.'   |
{colored('<created by>', "blue")}  {colored('0xNickSecurity, LUKE6044', 'white', attrs=['bold'])}  {colored('</created by>', "blue")}    '.____'.____.'____.'
{colored('<algorithm>', "blue")}  {colored('Python Fernet AES Encryption', 'white', attrs=['bold'])}  {colored('</algorithm>', "blue")}  '.________________.'
{colored('NOTE:', "red")}
This software is distributed under the MIT license
Please refer to the 'LICENSE.txt' file for details.

"""


#section for colors
global info
global error
global success
info = colored("[*]", "blue")
error = colored("[-]", "red", attrs=["bold"])
success = colored("[+]", "green", attrs=["bold"])

#the REAL code
class encryption: #class for encryption part
    def one_file(): #encrypt only a file
        keycheck = False
        try:
            while True:
                file = str(input(
                        '[*] Put the full path of the file to encrypt:\n> '.replace("[*]", info)
                ))
                
                choice = str(input(
                    "[*] Do you want to use your own key for the encryption? (if you don't want to use your own, a new key will be generated) Y/N\n> ".replace("[*]", info)
                ))
                if choice == "Y" or choice == "y" or choice == "yes" or choice =="Yes" or choice == "YES":
                    key = str(input(
                        "[*] Insert your own key for the encryption:\n> ".replace("[*]", info)
                    ))
                    keycheck = True
                else:
                    print("[*] generating key manually...".replace("[*]", info))
                    sleep(0.6)
                    key = Fernet.generate_key()
                    
                if os.path.isdir(file):
                    print('[-] The file is a directory.'.replace("[-]", error))
                    continue
                try:
                    with open(file, 'rb') as file_r:
                        data = file_r.read()
                        sleep(0.4)
                        print('[*] Encrypting file: '.replace("[*]", info) + file)
                        
                        data_enc = Fernet(key).encrypt(data)         
                    with open(file, 'wb') as file_w:
                        file_w.write(data_enc)         
                    sleep(1)
                    print('[+] File encrypted successfully!'.replace("[+]", success))
                    sleep(0.4)
                    if keycheck == False:
                        print('[*] The key that has been used for the encryption is: '.replace("[*]", info) + colored(key.decode(), "yellow"))
                    else:
                        print('[*] The key that has been used for the encryption is: '.replace("[*]", info) + colored(key, "yellow"))
                    break
                except FileNotFoundError:
                    print("[-] File not found.".replace("[-]", error))
                    continue
                except PermissionError:
                    print("[-] This program doesn't have the required privileges to open and encrypt this file.".replace("[-]", error))
                    break
                except KeyboardInterrupt:
                    print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
                    sys.exit()
                except Exception as E:
                    print(f'[-] Failed to encrypt file (info below) ==> {file}'.replace("[-]", error))
                    print(E)
                    break
        except KeyboardInterrupt:
            print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
            sys.exit()
          
    def one_directory(): #encrypt a directory
        keycheck = True
        while True:
            try:
                dir = str(input(
                    '[*] Put the full path of the directory to encrypt:\n> '.replace("[*]", info)
                ))

                choice = str(input(
                    "[*] Do you want to use your own key for the encryption? (if you don't want to use your own, a new key will be generated) Y/N\n> ".replace("[*]", info)
                ))
                if choice == "Y" or choice == "y" or choice == "yes" or choice =="Yes" or choice == "YES":
                    key = str(input(
                        "[*] Insert your own key for the encryption:\n> ".replace("[*]", info)
                    ))
                    keycheck = False
                else:
                    print("[*] Generating key manually...".replace("[*]", info))
                    sleep(0.6)
                
                    key = Fernet.generate_key()
                if not os.path.exists(dir):
                    print("[-] The path doesn't exist.".replace("[-]", error))
                    continue
                if os.path.isfile(dir):
                    print('[-] The path is a file.'.replace("[-]", error))
                    continue
                files = []
                allfiles = os.listdir(dir) # list
                
                for file in allfiles:
                    
                    if os.path.isfile(os.path.join(dir, file)):
                        print(f"[*] Found file: {os.path.join(dir, file)}".replace("[*]", info))
                        files.append(os.path.join(dir, file))
                        sleep(0.4)
                    else:
                        continue
                
                for ffile in files:
                    try:
                        with open(ffile, 'rb') as file_r:
                            data = file_r.read()
                            data_enc = Fernet(key).encrypt(data) 
                        with open(ffile, 'wb') as file_w:
                            file_w.write(data_enc)
                        
                        print(f"[+] File encrypted successfully! ==> {ffile}".replace("[+]", success))
                        sleep(0.4)
                    except Exception as E:
                        print(f'[-] Failed to encrypt file (info below) ==> {ffile}'.replace("[-]", error))
                        print(E)
                        sleep(0.4)
                if keycheck:
                    print('[*] The key that has been used for encryption is: '.replace("[*]", info) + colored(str(key.decode()), "yellow"))
                    break
                else:
                    print('[*] The key that has been used for encryption is: '.replace("[*]", info) + colored(str(key), "yellow"))
                    break
            except PermissionError:
                print("[-] This program doesn't have the required privileges to open or encrypt this file.".replace("[-]", error))
                break
            except KeyboardInterrupt:
                print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()
                
            
    def dir_and_subdirs(): # encrypt a directory with his subdirectories
        keycheck = False
        while True:
            try:
                dir = dir = str(input(
                    '[*] Put the full path of the directory to encrypt:\n> '.replace("[*]", info)
                ))
                if not os.path.exists(dir):
                    print("[-] The path you have entered doesn't exist.".replace("[-]", error))
                    continue
                
                choice = str(input(
                    "[*] Do you want to use your own key for the encryption? (if you don't want to use your own, a new key will be generated) Y/N\n> ".replace("[*]", info)
                ))
                if choice == "Y" or choice == "y" or choice == "yes" or choice =="Yes" or choice == "YES":
                    key = str(input(
                        "[*] Insert your own key for the encryption:\n> ".replace("[*]", info)
                    ))
                    keycheck = True
                else:
                    print("[*] Generating key manually...".replace("[*]", info))
                    sleep(0.6)
                    key = Fernet.generate_key()
                fz = []
                for root, dirs, filez in os.walk(dir):
                    for file in filez:
                        full_path = os.path.join(root, file)
                        fz.append(full_path)
                        print("[*] Found file:".replace("[*]", info), full_path)
                        sleep(0.4)
                
                for ff in fz:
                    try:
                        with open(ff, 'rb') as file_r:
                            data = file_r.read()
                            data_enc = Fernet(key).encrypt(data)
                            sleep(0.4)
                            print(f'[+] File encrypted successfully! ==> {ff}'.replace("[+]", success))
                        with open(ff, 'wb') as file_w:
                            file_w.write(data_enc)
                            sleep(0.6)
                    except Exception as E:
                        print(f'[-] Failed to encrypt file (info below) ==> {ff}'.replace("[-]", error))
                        print(E)
                        sleep(0.4)
                if keycheck:
                    print('[*] The key that has been used for encryption is: '.replace("[*]", info) + colored(str(key), "yellow"))
                else:
                    print('[*] The key that has been used for encryption is: '.replace("[*]", info) + colored(str(key.decode()), "yellow"))
                break
            except PermissionError:
                print("[-] This program doesn't have the required privileges to open or encrypt this file.".replace("[-]", error))
                continue
            except KeyboardInterrupt:
                print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()
              
    def phrase_enc(): #encrypt a phrase
        keycheck = True
        while True:
            try:
                phrase = str(input(
                    '[*] Put the phrase for encryption:\n> '.replace("[*]", info)
                ))
                choice = str(input(
                    "[*] Do you want to use your own key for the encryption? (if you don't want to use your own, a new key will be generated) Y/N\n> ".replace("[*]", info)
                ))
                if choice == "Y" or choice == "y" or choice == "yes" or choice =="Yes" or choice == "YES":
                    key = str(input(
                        "[*] Insert your own key for the encryption:\n> ".replace("[*]", info)
                    ))
                    keycheck = False
                else:
                    print("[*] Generating key manually...".replace("[*]", info))
                    sleep(0.6)
                    key = Fernet.generate_key()
                    print("[*] Encrypting the phrase...".replace("[*]", info))
                try:
                    data = phrase.encode()
                    data_enc = Fernet(key).encrypt(data)
                    sleep(1)
                    print(f"[+] The encrypted phrase is ==> {data_enc.decode()}".replace("[+]", success))
                    if keycheck:
                        print(f'[*] The key that has been used for encryption is: '.replace("[*]", info) + colored(str(key.decode()), "yellow"))
                    else:
                        print(f'[*] The key that has been used for encryption is: '.replace("[*]", info) + colored(str(key), "yellow"))
                except Exception as E:
                    print(f'[-] Failed to encrypt the phrase (info below) ==> {data.decode()}'.replace("[-]", error))
                    print(E)
                    break
                break
            except KeyboardInterrupt:
                print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()

            
                

    def main(action): #action = integer (this is the main of the encryption class)
        if action == 1:
            encryption.one_file()
        elif action == 2:
            encryption.one_directory()
        elif action == 3:
            encryption.dir_and_subdirs()
        elif action == 4:
            encryption.phrase_enc()
        elif action == 5: #quit function
            print("quitting, ByEzZ!!")
            sys.exit()


##########################################################################        DECRYPTION
##########################################################################        DECRYPTION
##########################################################################        DECRYPTION


class decryption: #decryption class
    def one_file(): #decrypt only a file
        while True:
            try:
                file = str(input(
                        '[*] Put the full path of the file to decrypt:\n> '.replace("[*]", info)
                ))
                
                key = str(input(
                    "[*] Put the decryption key:\n> ".replace("[*]", info)
                ))

                if os.path.isdir(file):
                    print('[-] The file is a directory.'.replace("[-]", error))
                    continue
                try:
                    with open(file, 'rb') as file_r:
                        data = file_r.read()
                        sleep(0.4)
                        print('[*] Decrypting file: '.replace("[*]", info) + file)
                        
                        try:
                            data_dec = Fernet(key).decrypt(data)
                        except:
                            print("[-] The key you have entered is not a valid Fernet AES key or the content of the file is already decrypted.".replace("[-]", error))
                            continue     
                    with open(file, 'wb') as file_w:
                        file_w.write(data_dec)         
                    sleep(1)
                    print(f'[+] File decrypted successfully! ==> {file}'.replace("[+]", success))
                    sleep(0.4)
                    break
                except FileNotFoundError:
                    print("[-] File not found.".replace("[-]", error))
                    continue
                except KeyboardInterrupt:
                    print("[*] CTRL + C DETECTED! ByeZzzZ!!".replace("[*]", info))
                    sys.exit()
            except PermissionError:
                print("[-] This program doesn't have the required privileges to open and encrypt this file.".replace("[-]", error))
            except KeyboardInterrupt:
                print("[*] CTRL + C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()   
            except Exception as E:
                print(f'[-] Failed to decrypt file (info below) ==> {file}'.replace("[-]", error))
                print(colored(f"[   probabily the file {file} are already decrypted or the key is invalid.   ]", "red", attrs=["bold"]))
                print(E)
                continue
              
    def one_directory(): #decrypt only a directory (all files in)
        while True:
            try:
                dir = str(input(
                    '[*] Put the full path of the directory to decrypt:\n> '.replace("[*]", info)
                ))
                if not os.path.exists(dir):
                    print("[-] The path doesn't exist.".replace("[-]", error))
                    continue
                if os.path.isfile(dir):
                    print('[-] The path is a file.'.replace("[-]", error))
                    continue
                key = str(input(
                    "[*] Put the decryption key:\n> ".replace("[*]", info)
                ))
                files = []
                allfiles = os.listdir(dir) # list
                
                for file in allfiles:
                    
                    if os.path.isfile(os.path.join(dir, file)):
                        print(f"[*] Found file: {os.path.join(dir, file)}".replace("[*]", info))
                        files.append(os.path.join(dir, file))
                        sleep(0.4)
                    else:
                        continue
                for ffile in files:
                    try:
                        with open(ffile, 'rb') as file_r:
                            data = file_r.read()
                            data_dec = Fernet(key).decrypt(data) 
                        with open(ffile, 'wb') as file_w:
                            file_w.write(data_dec)
                            print(f"[+] File decrypted successfully! ==> {ffile}".replace("[+]", success))
                            sleep(0.4)
                    except Exception as E:
                        print(f'[-] Failed to decrypt file (info below) ==> {ffile}'.replace("[-]", error))
                        print(colored(f"[   probabily the file {ffile} are already decrypted or the key is invalid.   ]", "red", attrs=["bold"]))
                        print(E)
                        sleep(0.4)
                        
                break
            except PermissionError:
                print("[-] This program doesn't have the required privileges to open or decrypt this file.".replace("[-]", error))
                break
            except KeyboardInterrupt:
                print("[*] CTRL + C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()
              
    def dirs_and_subdirs(): #decrypt a directory with is subdirectories
        while True:
            try:
                dir = str(input(
                    '[*] Put the full path of the directory to decrypt:\n> '.replace("[*]", info)
                ))
                if not os.path.exists(dir):
                    print("[-] The path you have entered doesn't exist.".replace("[-]", error))
                    continue

                key = str(input(
                    "[*] Insert the decryption key:\n> ".replace("[*]", info)
                ))
                fz = []
                for root, dirs, filez in os.walk(dir):
                    for file in filez:
                        full_path = os.path.join(root, file)
                        fz.append(full_path)
                        print("[*] Found file:".replace("[*]", info), full_path)
                        sleep(0.4)
                
                for ff in fz:
                    try:
                        with open(ff, 'rb') as file_r:
                            data = file_r.read()
                            data_dec = Fernet(key).decrypt(data)
                            sleep(0.4)
                            print(f'[+] File decrypted successfully! ==> {ff}'.replace("[+]", success))
                        with open(ff, 'wb') as file_w:
                            file_w.write(data_dec)
                    except Exception as E:
                        print(f'[-] Failed to decrypt file (info below) ==> {ff}'.replace("[-]", error))
                        print(colored(f"[   probabily the file {ff} are already decrypted or the key is invalid.   ]", "red", attrs=["bold"]))
                        print(E)
                        sleep(0.4)
                        
                break
            except PermissionError:
                print("[-] This program doesn't have the required privileges to open or encrypt this file.".replace("[-]", error))
                continue
            except KeyboardInterrupt:
                print("[*] CTRL + C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()
              
    def phrase_dec(): #decrypt only a phrase
        while True:
            try:
                phrase = str(input(
                    '[*] Put the phrase for decryption:\n> '.replace("[*]", info)
                ))
                key = str(input(
                    "[*] Insert the key for the decryption:\n> ".replace("[*]", info)
                ))
                data = phrase.encode()
                try:
                    data_enc = Fernet(key).decrypt(data).decode()
                except:
                    print("[-] The key is not valid for the decryption or the content are already decrypted.".replace("[-]", error))
                    continue
                print("[*] Decrypting the phrase...".replace("[*]", info))
                sleep(1)
                
                var_phrase_decrypted = f"[+] The decrypted phrase is ==> ".replace("[+]", success)
                print(var_phrase_decrypted + data_enc)
                break
            except KeyboardInterrupt:
                print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()
            except Exception as e:
                print(e)

    def main(action): # the main of the decryption class
        if action == 1:
            decryption.one_file()
        elif action == 2:
            decryption.one_directory()
        elif action == 3:
            decryption.dirs_and_subdirs()
        elif action == 4:
            decryption.phrase_dec()
        elif action == 5:
            print("quitting, ByEzZ!!")
            sys.exit()
class start: # the MAIN OF THE MAINS
    def banner(): #the function to print banner
        print(Banner_1)
      
    def select_crypto_action(): #function to select what you want to do (enc or dec)
        actions = f"""
{colored("****** AVAIABLE CHOICES ******", "blue")}
{colored("1)", "grey", attrs=["bold"])} Encryption
{colored("2)", "grey", attrs=["bold"])} Decryption
{colored("3)", "grey", attrs=["bold"])} {colored("EXIT", "red")}
        """
        print(actions)
        try:
            choice = int(input(
                "[*] Please select your choice in numbers:\n> ".replace("[*]", info)
            ))
        except KeyboardInterrupt:
            print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
            sys.exit()
        except:
            print("Only numbers allowed, quitting...")
            sleep(0.6)
            sys.exit()
        if choice  > 3 or choice < 1:
            print("[-] The choice doesn't exists, quitting...".replace("[-]", error))
            sys.exit()
            sleep(0.6)
        else:
            return choice
            
    def select_action(crypto_action): #the function to select the action to execute

        if crypto_action == 1:
            encrypt = f"""
{colored('***** ENCRYPTION *******', 'blue')} 
{colored("1)", "grey", attrs=["bold"])} encrypt only a file
{colored("2)", "grey", attrs=["bold"])} encrypt only a directory
{colored("3)", "grey", attrs=["bold"])} encrypt a directory with his subdirs
{colored("4)", "grey", attrs=["bold"])} encrypt a phrase 
{colored("5)", "grey", attrs=["bold"])} {colored("EXIT", "red")}
            """
            print(encrypt)
            try:
                choice = int(input(
                    "[*] Please select the action to execute in numbers:\n> ".replace("[*]", info)
                ))
            except KeyboardInterrupt:
                print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()
            except:
                print("[-] Only numbers allowed, quitting...".replace("[-]", error))
                sleep(0.6)
                sys.exit()
            if choice  > 5 or choice < 1:
                print("[-] The choice doesn't exists, quitting...".replace("[-]", error))
                sys.exit()
                sleep(0.6)
            else:
                return choice
        elif crypto_action == 2:
            decrypt = f"""
{colored('***** DECRYPTION *******', 'blue')} 
{colored("1)", "grey", attrs=["bold"])} decrypt only a file
{colored("2)", "grey", attrs=["bold"])} decrypt only a directory
{colored("3)", "grey", attrs=["bold"])} decrypt a directory with his subdirs
{colored("4)", "grey", attrs=["bold"])} decrypt a phrase
{colored("5)", "grey", attrs=["bold"])} {colored("EXIT", "red")}
            """
            print(decrypt)
        
            try:
                choice = int(input(
                    "[*] Please select the action to execute in numbers:\n> ".replace("[*]", info)
                ))
            except KeyboardInterrupt:
                print("[*] CTRL +C DETECTED! ByeZzzZ!!".replace("[*]", info))
                sys.exit()
            except:
                print("Only numbers allowed, quitting...")
                sleep(0.6)
                sys.exit()
            
                
            if choice  > 5 or choice < 1:
                print("[-] The choice doesn't exists, quitting...".replace("[-]", error))
                sys.exit()
                sleep(0.6)
            
        
            else:
                return choice
        elif crypto_action == 3:
            print("Quitting, ByEzZ!!")
            sys.exit()
        
    def main(): # THE MAINNNNNNNNNNNNNNNNNNNNNN
        start.banner()
        crypto_action = start.select_crypto_action() #integer
        action = start.select_action(crypto_action) #integer
        if crypto_action == 1:
            encryption.main(action)
        elif crypto_action == 2:
            decryption.main(action)
        elif KeyboardInterrupt:
            sys.exit()
          
start.main()
