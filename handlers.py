from pytube import YouTube
from config import prefix, help
from colorama import *
import os
from art import *
import platform

link = []

def start():
    os.system('CLS')
    tprint('ZZDownloader')
    print(prefix + Fore.YELLOW + ' Python Version ' + Fore.CYAN + str(platform.python_version()) + Fore.RESET + '')
    print(prefix + Fore.YELLOW + ' Project Version ' + Fore.CYAN + 'alpha 1.0.0 ' + Fore.RESET + '')
    print(prefix + Fore.YELLOW + ' Made by ' + Fore.CYAN + 'iTendyZz ' + Fore.RESET + '')
    print(help)
    link.append(input(prefix + ' Введи ссылку, друже: '))
    com = input(prefix + ' Введи команду: ')
    register_handlers(com)
        

def video_download(lnk):
    print(prefix + Fore.YELLOW + ' Видео скачивается в формате mp4!', Fore.RESET + '')
    video = YouTube(lnk)
    streams = video.streams.filter(type='video')
    stream = streams.get_highest_resolution()
    name = video.title + '.mp4'
    if stream is not None:
        stream.download(output_path="./downloads", filename=name)
        start()


def audio_download(lnk):
    print(prefix + Fore.YELLOW + ' Аудио скачивается в формате mp3!' + Fore.RESET + '')
    audio = YouTube(lnk)
    streams = audio.streams.filter(only_audio=True)
    stream = streams.get_audio_only()
    name = audio.title + '.mp3'
    if stream is not None:
        stream.download(output_path='./downloads', filename=name)
        start()
    else:
        start()

def register_handlers(com):
    lnk = link[0]
    comm = com.lower()
    if comm == 'видео' or 'video':
        video_download(lnk)
    if comm == 'аудио' or 'audio':
        audio_download(lnk)
    if comm == 'субтитры' or 'subtitles':
        pass




