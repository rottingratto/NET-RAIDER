#!/usr/bin/env python


import os, sys
import socket
from colorama import Fore, Style
import time

#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'

os.system("clear")

banner =  ("""\033[1;31m███╗   ██╗███████╗████████╗   ██████╗  █████╗ ██╗██████╗ ███████╗██████╗ \033[0;31m   MMNO!                           MNNOO!!
████╗  ██║██╔════╝╚══██╔══╝   ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗\033[0;31m MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
██╔██╗ ██║█████╗     ██║█████╗██████╔╝███████║██║██║  ██║█████╗  ██████╔╝\033[0;31m !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
██║╚██╗██║██╔══╝     ██║╚════╝██╔══██╗██╔══██║██║██║  ██║██╔══╝  ██╔══██╗\033[0;31m       ! MMMMMMMMMMMMMPPPPOOOOIII! !
██║ ╚████║███████╗   ██║      ██║  ██║██║  ██║██║██████╔╝███████╗██║  ██║\033[0;31m        MMMMMMMMMMMMPPPPPOOOOOOII!!
╚═╝  ╚═══╝╚══════╝   ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝\033[0;31m        MMMMMOOOOOOPPPPPPPPOOOOMII!
 \033[0;31m                                                                                MMMMM..    OPPMMP    .,OMI!
═════════════════════════════════════════════════════════════════════════\033[0;31m        MMMM::   o.,OPMP,.o   ::I!!
═════════════════════════════════════════════════════════════════════════\033[0;31m          NNM:::.,,OOPM!P,.::::!!
═════════════════════════════════════════════════════════════════════════\033[0;31m         MMNNNNNOOOOPMO!!IIPPO!!O!
═════════════════════════════════════════════════════════════════════════\033[0;31m         MMMMMNNNNOO:!!:!!IPPPPOO!
═════════════════════════════════════════════════════════════════════════\033[0;31m          MMMMMNNOOMMNNIIIPPPOO!!
═════════════════════════════════════════════════════════════════════════\033[0;31m             MMMONNMMNNNIIIOO!
═════════════════════════════════════════════════════════════════════════\033[0;31m           MN MOMMMNNNIIIIIO! OO
═════════════════════════════════════════════════════════════════════════\033[0;31m          MNO! IiiiiiiiiiiiI OOOO
═════════════════════════════════════════════════════════════════════════\033[0;31m     NNN.MNO!   O!!!!!!!!!O   OONO NO!
═════════════════════════════════════════════════════════════════════════\033[0;31m    MNNNNNO!    OOOOOOOOOOO    MMNNON!
═════════════════════════════════════════════════════════════════════════\033[0;31m      MNNNNO!    PPPPPPPPP    MMNON!
═════════════════════════════════════════════════════════════════════════\033[0;31m         OO!                   ON!\033[0m
""")








print(banner)
copyright = ("         \033[1;34m-=-=-=-=-=-=-Github: zod-the-immortal-=-=-=-=-=-=-\033[0m")
print(copyright)
copyright1 = ("     \033[1;34m-=-=-=-=-=-=-https://github.com/rottingratto/NET-RAIDER-=-=-=-=-=-=-\033[0m")
print(copyright1)


def menu():
	print("""
\033[1;37m[\033[1;34m1\033[1;37m] \033[0;37mCheck your internet connection\033[0m
\033[1;37m[\033[1;34m2\033[1;37m] \033[0;37mPublic address of Websites\033[0m
\033[1;37m[\033[1;34m3\033[1;37m] \033[0;37mPort scanner\033[0m
\033[1;37m[\033[1;34m4\033[1;37m] \033[0;37mScan IP's and MAC's on your Wi-Fi\033[0m
\033[1;37m[\033[1;34m5\033[1;37m] \033[0;37mscan nearby networks\033[0m
\033[1;37m[\033[1;34m6\033[1;37m] \033[0;37mstart monitor mode\033[0m
\033[1;37m[\033[1;34m7\033\033[1;37m] \033[0;37mreboot network\033[0m
\033[1;37m[\033[1;34m0\033[1;37m] \033[0;31mExit\033[0m

""")

def restart():
    if input("\n\033[1;37mBack to main menu \033[0;32my\033[1;37m/\033[0;31mn\033[0;m\n\033[1;37m->\033[0m ").upper() != "Y":
        time.sleep(1)
        os.system("clear")
        print(banner)
        print(copyright)
        print("\n\033[1;32mGoodbye\033[0;m\033[1;37m!\033[0;m")
        tool = exit(0)
    os.system("python3 NET-RAIDER.py")    	

def check_network():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("Checking connection...\n")
	s.settimeout(2)
	try:
		s.connect(('nmap.org',443))
		print("\033[0;32m[Connected]\033[0m")

	except:
		print("\033[0;31m[Disconnected]")

def Public_IP():
    hostName = input("Target: ")
 
    ipaddress = socket.gethostbyname(hostName)
    print("IP Address:\033[0;32m {}\033[0m".format(ipaddress))

def ScanManual():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.setdefaulttimeout(2)

    target = input("Target: ")
    port = int(input("Port: "))
    print("")

    def scan(port):
        if sock.connect_ex((target,port)):
            print("-" * 30,"\nPort",port,"is \033[0;31mclosed\033[0m")
            print("-" * 30)


        else:
        	print("-" * 30)
        	print("Port", port,"is \033[0;32mopen\033[0m")
        	print("-" * 30)

    scan(port) 


def ScanRandom():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket.setdefaulttimeout(1)

    target = input("Target: ")
    print("")

    def scanning(port):
        if sock.connect_ex((target,port)):
            print("-" * 30,"\nPort",port,"is \033[0;31mclosed\033[0m")
            print("-" * 30)

        else:
        	print("-" * 30)
        	print("Port", port,"is \033[0;32mopen\033[0m")
        	print("-" * 30)

    for port in range(1,65536):
        scanning(port)      


def NetworkScan():
        os.system("clear")
        print(banner)
        print(" \033[1;37mplease select the ip for scanning (\033[0;37mEX: xxx.xxx.x.xxx/24\033[0;31m)")
        ipaddress = input(" \033[1;39m>>\033[0;39m")
        comando = "nmap {} " .format(ipaddress)
        os.system(comando)
        time.sleep(20)
        os.system("python3 NET-RAIDER.py")

menu() 

option = int(input("\033[1;37m-> \033[0m"))

def goodbye():
  print("""
 \033[1;37m------------------------------------------------------\033[0m   
\033[1;34m    _____  ____   ____  _____  ______     ________ _ 
   / ____|/ __ \ / __ \|  __ \|  _ \ \   / /  ____| |
  | |  __| |  | | |  | | |  | | |_) \ \_/ /| |__  | |
  | | |_ | |  | | |  | | |  | |  _ < \   / |  __| | |
  | |__| | |__| | |__| | |__| | |_) | | |  | |____|_|
   \_____|\____/ \____/|_____/|____/  |_|  |______(_)\033[0m

     \033[1;31m<\033[1;37mbecome blackhat  - zod-the-immortal \033[1;31m>\033[0m 

 \033[1;37m------------------------------------------------------\033[0m 
                                                   
"""+ WHITE + Style.NORMAL)

if option == 1:
	check_network()
	restart()


elif option == 2:
	Public_IP()
	restart()

elif option == 4:
	NetworkScan()
	restart()

elif option == 5:
    os.system("clear")
    print(banner)
    print(" \033[1;37mplease select wifi inerface for attack : (\033[0;37mwlan\033[0;31m0\033[0;37\033[1;37m| \033[0;37mwlan\033[0;34m1\033[0;37\033[1;37m)\033[0m")
    interfaz = input(" \033[1;39m>> \033[0;39m")
    print("\033[1;37menter the name of the output file : (ex: \033[0;31mrandom-output\033[0m\033[1;37m)\033[0m")
    archivo_salida = input(" \033[1;39m>> \033[0;39m")
    comando = "airodump-ng --write scan-output/{} --output-format csv  {}".format(archivo_salida,interfaz)
    print("\n \033[1;31m[WARNING] \033[0;37mwhen finished press  \033[1;37mCTRL + C\033[0m")
    time.sleep(3)
    try:
        os.system(comando)
    except KeyboardInterrupt:
        print("\n\n \033[1;31m[WARNING] \033[0;37Escanning stopped saving results ...\033[0m")
        time.sleep(2)
    finally:
        time.sleep(3)
        print("\n\033[1;37mdata has been saved at: \033[0;37mscan-output/\033[0;32m{}01.csv\033[0m".format(archivo_salida))
        
        print("\033[1;37mwould you like to return to the menu? (\033[0;32my\033[0;37m/\033[0;31mn\033[1;37m):\033[0m")
        volver = input(" \033[1;39m>> \033[0;39m").strip().lower()
        if volver != 'y':
            print("\n\033[1;31m[GOODBYE]\033[0m killing  program...")
            time.sleep(1)
            exit(0)
        else:
            os.system('python3 NET-RAIDER.py')  
            
elif option  == 6:
	os.system("clear")
	print(banner)
	print(" \033[1;37mplease select wifi interface for attack (\033[0;37mwlan\033[0;31m0 \033[1;37m| \033[0;37mwlan\033[0;34m1\033[1;37m)")
	interfaz = input(" \033[1;39m>> \033[0;39m")
	comando = "airmon-ng start {} && airmon-ng check kill".format(interfaz)
	os.system(comando)
	os.system("python3 NET-RAIDER.py")

elif option == 7: 
    os.system("clear")
    print (banner)
    slowly(" \033[1;37mrestarting please wait...\033[0m")
    comando = "sudo systemctl restart NetworkManager"
    os.system(comando)
    print(" \033[1;31mtask finished!\033[0m")
    time.sleep(2)
    os.system("clear")
    os.system("python3 NET-RAIDER.py")
    
    
elif option == 0:
    os.system("clear")
    goodbye()
    exit() 



while option == 3:
	os.system("clear")
	print(banner)
	print(copyright)
	print("\n\033[1;37m[\033[1;31m1\033[1;37m]\033[0m \033[0;32mManual scan")
	print("\033[1;37m[\033[1;31m2\033[1;37m]\033[0m \033[0;32mRandom scan (\033[0;33m1\033[0;37m,\033[0;33m65536\033[0;32m)\033[0m")

	option = int(input("\n\033[1;37m-> \033[0m"))

	if option == 1:
		ScanManual()
		restart()

	elif option == 2:
		ScanRandom()
		restart()	

	
#CODE END 
#FOLLOW MY GITHUB FOR MORE COOL PROJECTS https://github.com/rottingratto
#DM IF U FOUND THIS XD .zod-the-immortal. on discord ^_^
#hint for next tool html&packets XD
