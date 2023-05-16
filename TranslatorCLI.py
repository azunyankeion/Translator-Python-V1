import sys
import argparse
from time import sleep
from googletrans import Translator
from colorama import Fore, init, AnsiToWin32


translator = Translator()
init=init(wrap=False)
stream = AnsiToWin32(sys.stderr).stream


class Translate:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description='Translate a phrases and words into whatever language you want')
        self.parser.add_argument('-t', '--text', type=str, help='Enter the phrase you want to translate')
        self.parser.add_argument('-f', '--filename', help='Enter the name of the file you want to translate')
        self.args = self.parser.parse_args()


    def print_help(self):
        """ 
            # * This function prints the help! 
        """
        self.parser.print_help() 

    
    def translate(self, translating: any) -> str:
        """ 
            # * The principal function, translate phrases in this translator!
        """
        while True:
            try:
                lang_dest = str(input(Fore.GREEN + 'Enter the language you want to translate, EXAMPLE: EN, PT, ES, JA, zh-tw(Chinese): '))
            except ValueError:
                print(Fore.RED + 'Please enter a valid phrase or word', file=stream)
            translating = translator.translate(str(self.args.text), dest=lang_dest.lower())     
            print(Fore.RED + f'\nORIGINAL -> {translating.origin}\n' + Fore.BLUE + f'TRANSLATED -> {translating.text}\n', file=stream)
            break


    def ftranslate(self, content: list = list[str]) -> str:
        """ 
            # * Function to translate a file!        
        """
        with open(self.args.filename, 'r', encoding='utf-8') as f:
            try:
                lang_dest = str(input(Fore.GREEN + 'Enter the language you want to translate, EXAMPLE: EN, PT, ES, JA, zh-tw(Chinese): '))
                content = f.readlines()
                print(Fore.LIGHTRED_EX + "ATTENTION, IF IN YOU ARCHIVE DON'T HAVE ONCE BREAK LINE IN THE LAST LINE OF THE ARCHIVE, THE HYPHENS GOT MESSED UP", file=stream)
                sleep(2)
            except ValueError:
                print(Fore.BLACK + 'Please enter a valid file', file=stream)
            try:
                for i in content:
                    translating = translator.translate(str(i), dest=lang_dest.lower())
                    print(Fore.RED + f'\nORIGINAL -> {translating.origin}---------------------\n' + Fore.BLUE + f'TRANSLATED -> {translating.text}\n', file=stream)
            except Exception as error:
                print(f'{error}')

    def __main__(self, validate: list = [0]) -> None:
        """ 
            # * The main function of the Translator!
        """
        while True: 
            validate = [0] # Create a variable, finality is checking if it exists one argument specified!
            if self.args.text == None:
                self.args.text = str(self.args.text)
                self.args.text = ''
            elif self.args.filename == None: # If self.args.filename == None(Null value in C, Java, etc), execute the block below!
                self.args.filename = str(self.args.filename) 
                self.args.filename = ''
            try:
                if validate[0] < len(str(self.args.text)) and validate[0] >= len(str(self.args.filename)): # If 0 is < the letters in self.args.text and 0 >= the letters in self.args.filename execute the block below
                    self.translate()
                    break
                elif validate[0] >= len(str(self.args.text)) and validate[0] < len(str(self.args.filename)): # If 0 is >= the letters in self.args.text and 0 < the letters in self.args.filename execute the block below
                    self.ftranslate()
                    break
                elif validate[0] <= len(str(self.args.filename)) and validate[0] <= len(str(self.args.text)): # If 0 is <= the letters in self.args.filename and 0 <= the letters in self.args.text execute the block of error below
                    print(Fore.GREEN + '\nPLEASE,' + ' ' + Fore.YELLOW + 'ENTER,' + ' ' + Fore.MAGENTA + 'ONLY,' + ' ' + Fore.CYAN + 'ONE,' + ' ' + Fore.LIGHTBLACK_EX + 'ARGUMENT!\n', file=stream)
                    break
            except Exception as error:
                print(Fore.LIGHTGREEN_EX + f'{error}', file=stream)
                break
    

if __name__ == '__main__':
    Translate().__main__()
