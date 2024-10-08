import sys
import argparse
import platform
import os
from time import sleep

from googletrans import Translator
from colorama import Fore, init, AnsiToWin32
import psutil


translator = Translator()
init = init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream


class Translate:

    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description='Translate a phrases and words into whatever language you want')
        self.parser.add_argument(
            '-t', '--text', type=str, help='Enter the phrase you want to translate')
        self.parser.add_argument(
            '-f', '--filename', help='Enter the name of the file you want to translate')
        self.args = self.parser.parse_args()

    def print_help(self):
        """ 
            # * This function prints the help! 
        """
        self.parser.print_help()

    
    def system_info(self) -> str:
        """ 
            Print the your system information !
        """
        ram_memory = str(round(psutil.virtual_memory().total / (1024.0 **3)))
        username = os.getlogin()
        system = platform.system()
        processor = platform.uname()
        if system == 'Linux':
            print(Fore.RED + f'\nThe system is GNU/Linux')
        elif system == 'Windows':
                print(Fore.RED + f'\nThe system is Windows')
        else:
            system = Fore.RED + f'\nThe system is {platform.system()}'
            print(system)
        print(Fore.BLUE + f'Username: {username}')
        print(Fore.LIGHTCYAN_EX + f'The RAM Memory is {ram_memory} GB')
        print(Fore.LIGHTBLUE_EX + f'The architecture of the processor is {processor.processor}\n')

    def translate(self) -> str:
        """ 
            # * The principal function, translate phrases in this translator!
        """
        while True:
            lang_dest = str(input(Fore.LIGHTMAGENTA_EX + 'Enter the language you want to translate, EXAMPLE: EN, PT, ES, JA, zh-tw(Chinese): '))
            translating = translator.translate(str(self.args.text), dest=lang_dest.lower())
            print(Fore.RED + f'\nORIGINAL -> {translating.origin}\n' + Fore.BLUE + f'TRANSLATED -> {translating.text}\n', file=stream)
            break

    def ftranslate(self, content: list = list[str]) -> str:
        """ 
            # * Function to translate a file!        
        """
        with open(self.args.filename, 'r', encoding='utf-8') as f:
            try:
                lang_dest = str(input(
                    Fore.GREEN + 'Enter the language you want to translate, EXAMPLE: EN, PT, ES, JA, zh-tw(Chinese): '))
                content = f.readlines()
                print(Fore.LIGHTRED_EX + "ATTENTION, IF IN YOUR FILE YOU DON'T HAVE ONCE BREAK LINE IN THE LAST LINE OF THE FILE, THE HYPHENS GOT MESSED UP", file=stream)
                sleep(2)
            except ValueError:
                print(Fore.BLACK + 'Please enter a valid file', file=stream)
            try:
                for i in content:
                    translating = translator.translate(
                        str(i), dest=lang_dest.lower())
                    print(Fore.RED + f'\nORIGINAL -> {translating.origin}---------------------\n' +
                          Fore.BLUE + f'TRANSLATED -> {translating.text}\n', file=stream)
            except Exception as error:
                print(f'{error}')

    def __main__(self, validate: list = [0]) -> None:
        """ 
            # * The main function of the Translator!
        """
        while True:
            # Create a variable, finality is checking if it exists one argument specified!
            validate = [0]
            if self.args.text == None:
                self.args.text = str(self.args.text)
                self.args.text = ''
            # If self.args.filename == None(Null value in C, Java, etc), execute the block below!
            elif self.args.filename == None:
                self.args.filename = str(self.args.filename)
                self.args.filename = ''
            try:
                # If 0 is < the letters in self.args.text and 0 >= the letters in self.args.filename execute the block below
                if validate[0] < len(str(self.args.text)) and validate[0] >= len(str(self.args.filename)):
                    self.translate()
                    break
                # If 0 is >= the letters in self.args.text and 0 < the letters in self.args.filename execute the block below
                elif validate[0] >= len(str(self.args.text)) and validate[0] < len(str(self.args.filename)):
                    self.ftranslate()
                    break
                # If 0 is <= the letters in self.args.filename and 0 <= the letters in self.args.text execute the block of error below
                elif validate[0] <= len(str(self.args.filename)) and validate[0] <= len(str(self.args.text)):
                    print(Fore.GREEN + '\nPLEASE,' + ' ' + Fore.YELLOW + 'ENTER,' + ' ' + Fore.MAGENTA +
                          'ONLY,' + ' ' + Fore.CYAN + 'ONE,' + ' ' + Fore.LIGHTBLACK_EX + 'ARGUMENT!\n', file=stream)
                    break
            except Exception as error:
                print(Fore.LIGHTGREEN_EX + f'{error}', file=stream)
                break


if __name__ == '__main__':
    Translate().system_info()
    Translate().__main__()
