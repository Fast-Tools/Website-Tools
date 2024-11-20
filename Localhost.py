import http.server
import socketserver
def clear():
	__import__('time').sleep(2)
	__import__('os').system('clear')
def logo(haker):
 print(haker)
logo(haker='𝙲𝚁𝙸𝚃𝙴𝙳 𝙱𝚈 :\n\n \x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m╗\x1b[39m  \x1b[31m█████\x1b[39m\x1b[32m╗\x1b[39m  \x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m███████\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m██████\x1b[39m\x1b[32m╗ \x1b[39m \n \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m ██\x1b[39m\x1b[32m╔╝\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔════╝\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m \n \x1b[31m███████\x1b[39m\x1b[32m║\x1b[39m \x1b[31m███████\x1b[39m\x1b[32m║\x1b[39m \x1b[31m█████\x1b[39m\x1b[32m╔╝ \x1b[39m \x1b[31m█████\x1b[39m\x1b[32m╗  \x1b[39m \x1b[31m██████\x1b[39m\x1b[32m╔╝\x1b[39m \n \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔═\x1b[39m\x1b[31m██\x1b[39m\x1b[32m╗ \x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══╝  \x1b[39m \x1b[31m██\x1b[39m\x1b[32m╔══\x1b[39m\x1b[31m██\x1b[39m\x1b[32m╗\x1b[39m \n \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m║\x1b[39m \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m███████\x1b[39m\x1b[32m╗\x1b[39m \x1b[31m██\x1b[39m\x1b[32m║\x1b[39m\x1b[31m  ██\x1b[39m\x1b[32m║\x1b[39m \n \x1b[32m╚═╝  ╚═╝\x1b[39m \x1b[32m╚═╝  ╚═╝\x1b[39m \x1b[32m╚═╝  ╚═╝\x1b[39m \x1b[32m╚══════╝\x1b[39m \x1b[32m╚═╝  ╚═╝\x1b[39m \n\n'+'\n\n \x1b[32m████████\x1b[39m\x1b[31m╗\x1b[39m \x1b[32m███████\x1b[39m\x1b[31m╗\x1b[39m  \x1b[32m█████\x1b[39m\x1b[31m╗\x1b[39m  \x1b[32m███\x1b[39m\x1b[31m╗\x1b[39m\x1b[32m   ███\x1b[39m\x1b[31m╗\x1b[39m \n \x1b[31m╚══\x1b[39m\x1b[32m██\x1b[39m\x1b[31m╔══╝\x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔════╝\x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔══\x1b[39m\x1b[32m██\x1b[39m\x1b[31m╗\x1b[39m \x1b[32m████\x1b[39m\x1b[31m╗\x1b[39m\x1b[32m ████\x1b[39m\x1b[31m║\x1b[39m \n \x1b[32m   ██\x1b[39m\x1b[31m║   \x1b[39m \x1b[32m█████\x1b[39m\x1b[31m╗  \x1b[39m \x1b[32m███████\x1b[39m\x1b[31m║\x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔\x1b[39m\x1b[32m████\x1b[39m\x1b[31m╔\x1b[39m\x1b[32m██\x1b[39m\x1b[31m║\x1b[39m \n \x1b[32m   ██\x1b[39m\x1b[31m║   \x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔══╝  \x1b[39m \x1b[32m██\x1b[39m\x1b[31m╔══\x1b[39m\x1b[32m██\x1b[39m\x1b[31m║\x1b[39m \x1b[32m██\x1b[39m\x1b[31m║╚\x1b[39m\x1b[32m██\x1b[39m\x1b[31m╔╝\x1b[39m\x1b[32m██\x1b[39m\x1b[31m║\x1b[39m \n \x1b[32m   ██\x1b[39m\x1b[31m║   \x1b[39m \x1b[32m███████\x1b[39m\x1b[31m╗\x1b[39m \x1b[32m██\x1b[39m\x1b[31m║\x1b[39m\x1b[32m  ██\x1b[39m\x1b[31m║\x1b[39m \x1b[32m██\x1b[39m\x1b[31m║ ╚═╝\x1b[39m\x1b[32m ██\x1b[39m\x1b[31m║\x1b[39m \n \x1b[31m   ╚═╝   \x1b[39m \x1b[31m╚══════╝\x1b[39m \x1b[31m╚═╝  ╚═╝\x1b[39m \x1b[31m╚═╝     ╚═╝\x1b[39m \n\n')
clear()
PORT = int(input("ᴇɴᴛᴇʀ ᴛʜᴇ ᴘᴏʀᴛ > "))
file = input("ᴇɴᴛᴇʀ ᴛʜᴇ ғɪʟᴇ ᴡɪᴛʜ .html > ")
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = super().translate_path(path)
        if path.endswith('/'):
            path += file
        return path


with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"http://localhost:{PORT}/{file}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print("sᴇʀᴠᴇʀ sᴛᴏᴘᴇᴅ")
