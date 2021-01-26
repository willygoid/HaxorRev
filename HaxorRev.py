import json, os
from urllib.request import urlopen as unduh

print(" _   _                     ______           ")
print("| | | |   t.me/its_willy   | ___ \          ")
print("| |_| | __ ___  _____  _ __| |_/ /_____   __")
print("|  _  |/ _` \ \/ / _ \| '__|    // _ \ \ / /")
print("| | | | (_| |>  < (_) | |  | |\ \  __/\ V / ")
print("\_| |_/\__,_/_/\_\___/|_|  \_| \_\___| \_/  ")
print("       The Ultimate Reverse IP Tools        \n")                                            
                                            

#Inputan User
key = str(input("Enter API Key: "))
lists = open(input('Enter IP list: '), 'r').read().split('\n')

for ip in lists:
    print("[>] Reversing", ip, "...")
    colong = 'null'   
    try:
        data = unduh('https://api.hax.or.id/revip/?apikey='+key+'&ip=' + ip).read().decode('utf-8')
        colong = json.loads(data)

    except:
        continue
    for domains in colong['HaxorRev']:
        open('HaxorRev.txt', 'a+').write(domains + '\n')

#Hasil Akhir
print("\n======================[ Report ]======================")
#Baca Jumlah Baris
with open('HaxorRev.txt', 'a+') as buatfile:
  pass 
file = open("HaxorRev.txt","r") 
Counter = 0 
konten = file.read() 
listisian = konten.split("\n") 
for isi in listisian: 
    if isi: 
        Counter += 1
if Counter == 0:
  print("[!] Invalid API Key, Contact mi77ihaxor@gmail.com to buy a valid API Key")
else:          
  print("[#] Result:", (Counter), "Domains")
print(f'[#] Saved on: {os.getcwd()}/HaxorRev.txt') 
print("======================================================")