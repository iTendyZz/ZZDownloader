import time
from colorama import *


prefix = (Back.BLACK + Fore.GREEN + time.strftime(f'%d.%m.%Y %H:%M:%S GMT +3',
    time.localtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)

help = Fore.MAGENTA + '''Приветствую, странник!
Приятно видеть тебя снова.
Вводишь ссылку на видос, пишешь вот эти команды и все будет красиво:
''' + Fore.RED + 'видео ' + Fore.RESET + '-' + Fore.GREEN + ''' просит у тебя ссылку, а затем качество нужного тебе видео
''' + Fore.RED + 'аудио ' + Fore.RESET + '-' + Fore.GREEN + ''' то же самое что и с видео, но с аудио)
''' + Fore.RED + 'субтитры ' + Fore.RESET + '-' + Fore.GREEN + ''' скачивает нужные тебе субтитры''' + Fore.RESET + '\n'
