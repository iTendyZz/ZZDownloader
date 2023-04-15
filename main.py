from colorama import *
from config import prefix, help
import platform
from art import *
from pytube import YouTube
import os
from handlers import start

os.system('CLS')
tprint('ZZDownloader')
print(prefix + Fore.YELLOW + ' Python Version ' + Fore.CYAN + str(platform.python_version()) + Fore.RESET + '')
print(prefix + Fore.YELLOW + ' Project Version ' + Fore.CYAN + 'alpha 1.0.0 ' + Fore.RESET + '')
print(prefix + Fore.YELLOW + ' Made by ' + Fore.CYAN + 'iTendyZz ' + Fore.RESET + '')
print(help)
start()


