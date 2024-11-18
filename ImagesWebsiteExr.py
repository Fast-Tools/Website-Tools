# <-- 𝚌𝚘𝚙𝚢𝚛𝚒𝚐𝚑𝚛 => ʰᵃᵏᵉʳ TEAM -->
# 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 => https://t.me/H_T_Oi

import requests as Re
from requests import exceptions as Ex
from bs4 import BeautifulSoup
import os
import zipfile
import shutil
from urllib.parse import urljoin
	
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"  
cyan="\033[1;36m"
white="\033[1;37m"
info= yellow + '\n[' + white + '?' + yellow + '] '+ cyan
success = green + '\n[' + white + '✓' + green + '] '
error = red + '\n[' + white + '!' + red + '] '
def logo(haker):
	print(haker)
def clear():
	__import__('time').sleep(2)
	__import__('os').system('clear')
def Tool():
	logo(haker='𝙲𝚁𝙸𝚃𝙴𝙳 𝙱𝚈 :\n\n \x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m╗\x1b[39m  \x1b[31m█████\x1b[39m\x1b[32m╗\x1b[39m  \x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m███████\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m██████\x1b[39m\x1b[32m╗ \x1b[39m \n \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m ██\x1b[39m\x1b[32m╔╝\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔════╝\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m \n \x1b[31m███████\x1b[39m\x1b[32m║\x1b[39m \x1b[31m███████\x1b[39m\x1b[32m║\x1b[39m \x1b[31m█████\x1b[39m\x1b[32m╔╝ \x1b[39m \x1b[31m█████\x1b[39m\x1b[32m╗  \x1b[39m \x1b[31m██████\x1b[39m\x1b[32m╔╝\x1b[39m \n \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔═\x1b[39m\x1b[31m██\x1b[39m\x1b[32m╗ \x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══╝  \x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m \n \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m███████\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m║\x1b[39m \n \x1b[32m╚═╝  ╚═╝\x1b[39m \x1b[32m╚═╝  ╚═╝\x1b[39m \x1b[32m╚═╝  ╚═╝\x1b[39m \x1b[32m╚══════╝\x1b[39m \x1b[32m╚═╝  ╚═╝\x1b[39m \n\n'+'\n\n \x1b[32m████████\x1b[39m\x1b[31m╗\x1b[39m \x1b[32m███████\x1b[39m\x1b[31m╗\x1b[39m  \x1b[32m█████\x1b[39m\x1b[31m╗\x1b[39m  \x1b[32m███\x1b[39m\x1b[31m╗\x1b[39m\x1b[32m   ███\x1b[39m\x1b[31m╗\x1b[39m \n \x1b[31m╚══\x1b[39m\x1b[32m██\x1b[39m\x1b[31m╔══╝\x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔════╝\x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔══\x1b[39m\x1b[32m██\x1b[39m\x1b[31m╗\x1b[39m \x1b[32m████\x1b[39m\x1b[31m╗\x1b[39m\x1b[32m ████\x1b[39m\x1b[31m║\x1b[39m \n \x1b[32m   ██\x1b[39m\x1b[31m║   \x1b[39m \x1b[32m█████\x1b[39m\x1b[31m╗  \x1b[39m \x1b[32m███████\x1b[39m\x1b[31m║\x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔\x1b[39m\x1b[32m████\x1b[39m\x1b[31m╔\x1b[39m\x1b[32m██\x1b[39m\x1b[31m║\x1b[39m \n \x1b[32m   ██\x1b[39m\x1b[31m║   \x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔══╝  \x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔══\x1b[39m\x1b[32m██\x1b[39m\x1b[31m║\x1b[39m \x1b[32m██\x1b[39m\x1b[31m║╚\x1b[39m\x1b[32m██\x1b[39m\x1b[31m╔╝\x1b[39m\x1b[32m██\x1b[39m\x1b[31m║\x1b[39m \n \x1b[32m   ██\x1b[39m\x1b[31m║   \x1b[39m \x1b[32m███████\x1b[39m\x1b[31m╗\x1b[39m \x1b[32m██\x1b[39m\x1b[31m║\x1b[39m\x1b[32m  ██\x1b[39m\x1b[31m║\x1b[39m \x1b[32m██\x1b[39m\x1b[31m║ ╚═╝\x1b[39m\x1b[32m ██\x1b[39m\x1b[31m║\x1b[39m \n \x1b[31m   ╚═╝   \x1b[39m \x1b[31m╚══════╝\x1b[39m \x1b[31m╚═╝  ╚═╝\x1b[39m \x1b[31m╚═╝     ╚═╝\x1b[39m \n\n')
	clear()
	
	def Picc(api):
	    response = Re.get(api)
	    soup = BeautifulSoup(response.text, 'html.parser')
	    images = soup.find_all('img')
	    piiic = [urljoin(api, img['src']) for img in images if 'src' in img.attrs]
	
	    if not os.path.exists('images'):
	        os.makedirs('images')
	
	    for i, img_api in enumerate(piiic):
	        img_data = Re.get(img_api).content
	        with open(f'images/image_{i}.jpg', 'wb') as handler:
	            handler.write(img_data)
	
	    return piiic
	
	def Czip():
	    with zipfile.ZipFile('fast_pic.zip', 'w') as zipf:
	        for root, dirs, files in os.walk('images'):
	            for file in files:
	                zipf.write(os.path.join(root, file))
	    shutil.rmtree('images')
	
	
	def sendTELE(tok, id):
	    for filename in os.listdir('images'):
	        with open(f'images/{filename}', 'rb') as photo:
	            response = Re.post(
	                f'https://api.telegram.org/bot{tok}/sendPhoto',
	                data={'chat_id': id},
	                files={'photo': photo}
	            )
	            
	    shutil.rmtree('images')
	
	def main():
	    api = input(f"{info} ᴜʀʟ > {white}")
	    piiic = Picc(api)
	
	    print(f"ᴅᴏɴᴇ ғɪɴᴅ {len(piiic)} ᴘɪᴄᴛᴜʀᴇ.")
	    print("ʏᴏᴜ ᴡᴀɴᴛ : \n [1] » sᴀᴠᴇ ɪɴ ᴢɪᴘ ғɪʟᴇ\n [2] »  sᴇɴᴅ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ")
	    choice = input(f'{info} ᴇɴᴛᴇʀ [1 ᴏʀ 2 > {white}')
	
	    if choice == '1':
	        Czip()
	        print("ᴅᴏɴᴇ sᴀᴠᴇ ɪɴ > [fast_pic.zip]")
	    elif choice == '2':
	        tok = input(f"{info} ʙᴏᴛ ᴛᴏᴋᴇɴ > ")
	        id = input(f"{info} ɪᴅ > {white}")
	        sendTELE(tok, id)
	        print(f"{success} ᴅᴏɴᴇ sᴇɴᴅɪɴɢ")
	    else:
	        print(f"{error} ʙᴀᴅ ᴄʜᴏɪᴄᴇ")
	
	DT = main
	DT()
try:
	Tool()
except Ex.ConnectionError:
	print(f'{error} ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴏɴɪᴄᴛɪᴏɴ{white}')
except Ex.MissingSchema:
	print(f'{error} ɪɴᴠᴀʟɪᴅ ᴜʀʟ')
