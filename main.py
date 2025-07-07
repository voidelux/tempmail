from tempmail import EMail
import pystyle
from pystyle import Write, Colors
import html2text
import colorama
from colorama import init, Fore, Back, Style
import raducord
from raducord import Logger
import time
from src.banner import print_banner
print_banner()
def generate_mail():
    Logger.warning('Generating email...')
    email = EMail()
    Logger.success(f'Sucess, email generated,{email.address}')
    time.sleep(1)
    Logger.info('Wating, Wating for message,...')
    msg = email.wait_for_message(timeout=240)
    text_content = html2text.html2text(msg.body)
    print()
    print(text_content)
    input("Type ENTER to leave..")

opc = Write.Input('\n\nroot@mail>> ', Colors.red_to_black)

if opc == '1':
    generate_mail()

else:
    print("Just type 1 bruh.")
