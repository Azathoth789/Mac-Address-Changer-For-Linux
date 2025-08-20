#importing modules
import subprocess
import random
import time
from colorama import init, Fore, Style
import pyfiglet

#setting colorama variables and functions
foreG = Fore.GREEN + Style.BRIGHT
foreM = Fore.MAGENTA + Style.BRIGHT
foreY= Fore.YELLOW + Style.BRIGHT
init(autoreset=True)
def print_colored(text, color=Fore.WHITE, style=Style.NORMAL):
    print(f"{style}{color}{text}{Style.RESET_ALL}")

# Display large welcome message
ascii_banner = pyfiglet.figlet_format("WELCOME TO LINUX  MAC  CHANGER BY ARNAV")
print("\n")
print_colored(ascii_banner, Fore.RED, Style.BRIGHT)

#showing available interfaces
print_colored(f"{foreG} Following are the availabe interfaces : ")
print("\n")
result = subprocess.run(['ifconfig'], capture_output=True, text=True)
if result.returncode == 0:
    print_colored(result.stdout, color=Fore.YELLOW)
else:
    print_colored(f"{foreY}Error occurred: Command returned non-zero exit status {result.returncode}")

#basic input commands
interface=input(f"{foreG} Enter your interface name ( for example :- wlan0 , eth0 etc ) : {foreY} " )
print("\n")
type=int(input(f"{foreG} Press 1 for inputting new mac address manually & 2 to get a new random mac address :{foreY} "))
print("\n")

#conditional statements 
if type==1:
    nmac=input(f" {foreM}Please enter the desired new mac address :{foreY} ")
    print("\n")
    print_colored(f"{foreM} Changing mac address for : {foreY}" +interface)
    print("\n")
    command=f"cat /sys/class/net/{interface}/address"
    macadd=subprocess.run(command,shell=True,capture_output=True,text=True)
    result=macadd.stdout.strip()
    print_colored(f"{foreM} Your current mac address is : {foreY} {result}")
    print("\n")
    time.sleep(3)
    print_colored(f"{foreM} Changing the mac address to : {foreY}{nmac}")
    print("\n")
#changing mac address   
    subprocess.call(f"sudo ifconfig {interface} down" , shell=True)
    new_mac=nmac
    subprocess.call(f"sudo ifconfig {interface} hw ether {nmac}" , shell=True)
    subprocess.call(f"sudo ifconfig {interface} up " , shell=True)
    time.sleep(3)
    macadd1=subprocess.run(command,shell=True,capture_output=True,text=True)
    result=(macadd1.stdout.strip())
    print_colored(f" {foreM}Your new mac address is : {foreY}{result} ")
    print("\n")
    subprocess.call(f"sudo ifconfig {interface} up " , shell=True)
    
#verification
    inp=input(f"{foreG} Do you want to verify the mac address? input y/n : {foreY}")
    print("\n")
    if inp.lower()=="y":
        result = subprocess.run([f'ifconfig',interface], capture_output=True, text=True)
        if result.returncode == 0:
            print_colored(result.stdout, color=Fore.YELLOW)
            print(f"{foreM} THANKS FOR USING THE TOOL")
        else:
            print_colored(f"{foreY}Error occurred: Command returned non-zero exit status {result.returncode}")
    elif inp.lower()=="n" or "N":
        print(f"{foreM} THANKS FOR USING THE TOOL")
    else:
        print("wrong choice entered")

#8b37fa2024f557b176cb49ad2087320dbdfaf272e0b126fcd55964cd10d1c98b18d619b2481f08f9e7c6ab4c82dde73f3d262d4174df0f7429a8183bcf0b349f


elif type==2:
    print_colored(f"{foreM} Changing mac address for : {foreY}" +interface)
    print("\n")
    command=f"cat /sys/class/net/{interface}/address"
    macadd=subprocess.run(command,shell=True,capture_output=True,text=True)
    result1=macadd.stdout.strip()
    print_colored(f"{foreM} Your current mac address is : {foreY} {result1}")
    print("\n")
    time.sleep(1)

    def random_mac():
        mac = [0x00,0x16,0x3e,
               random.randint(0x00,0x7f),
                random.randint(0x00,0xff),
                random.randint(0x00,0xff)]
        return ':'.join(map(lambda
                            x : f"{x:02x}",mac))

#changing mac address
    subprocess.call(f"sudo ifconfig {interface} down " , shell=True)
    new_macc=random_mac()
    subprocess.call((f"sudo ifconfig {interface} hw ether {new_macc}") , shell=True)
    subprocess.call(f"sudo ifconfig {interface} up " , shell=True)
    time.sleep(1)
    command=f"cat /sys/class/net/{interface}/address"
    macadd1=subprocess.run(command,shell=True,capture_output=True,text=True)
    result2=macadd1.stdout.strip()
    print_colored(f"{foreM} Your new mac address is : {foreY} {result2}")
    print("\n")
    subprocess.call(f"sudo ifconfig {interface} up " , shell=True)

#verification
    inp=input(f"{foreG} Do you want to verify the mac address? input y/n : {foreY}")
    print("\n")
    if inp.lower()=="y":
        result = subprocess.run([f'ifconfig' ,interface], capture_output=True, text=True)
        if result.returncode == 0:
            print_colored(result.stdout, color=Fore.YELLOW)
            thanks=pyfiglet.figlet_format("THANK YOU FOR USING THE TOOL")
            print_colored(thanks,Fore.RED,Style.BRIGHT)
        else:
            print_colored(f"{foreY}Error occurred: Command returned non-zero exit status {result.returncode}")
    elif inp.lower()=="n" or "N":
        thanks=pyfiglet.figlet_format("THANK YOU FOR USING THE TOOL")
        print_colored(thanks,Fore.RED,Style.BRIGHT)
    else:
        print("wrong choice entered")

else:
    print_colored(f"{foreY} Wrong Choice Entered")


