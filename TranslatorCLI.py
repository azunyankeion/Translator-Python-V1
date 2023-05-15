from googletrans import Translator
from time import sleep
import argparse

translator = Translator()

class Translate:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            description='Translate a phrases and words into whatever language you want', add_help=True)
        self.parser.add_argument('-t', '--text',type=str,help='Enter the phrase you want to translate')
        self.parser.add_argument('-f', '--filename',help='Enter the name of the file you want to translate')
        self.args = self.parser.parse_args()


    def translate_text(self):
        while True:
            try:
                lang_dest = input('Enter the language you want to translate, EXAMPLE: EN, PT, ES, JA, zh-tw(Chinese) ')
            except ValueError:
                print('Please enter a valid phrase or word')
            translating = translator.translate(str(self.args.text), dest=lang_dest.lower())     
            sleep(1)
            print(f'\n\nORIGINAL -> {translating.origin}, TRANSLATED -> {translating.text}\n\n')
            break


    def translate_file(self):
        with open(self.args.filename, 'r', encoding='utf-8') as f:
            try:
                lang_dest = str(input('Enter the language you want to translate, EXAMPLE: EN, PT, ES, JA, zh-tw(Chinese): '))
                content = f.readlines()
                print("ATTENTION, IF IN YOU ARCHIVE DON'T HAVE ONCE BREAKLINE IN THE LAST LINE OF THE ARCHIVE, THE HYPHENS GOT MESSED UP")
                sleep(2)
                for i in content:
                    translating = translator.translate(str(i), dest=lang_dest.lower())
                    print(f'\nORIGINAL -> {translating.origin}---------------------\nTRANSLATED -> {translating.text}\n')
            except ValueError:
                print('Please enter a valid phrase or word')

    def init(self):
        validate = [0]
        if self.args.text == None:
            self.args.text = str(self.args.text)
            self.args.text = ''
        if self.args.filename == None:
            self.args.filename = str(self.args.filename)
            self.args.filename = ''
        try: 
            if validate[0] < len(str(self.args.text)):
                self.translate_text()
            
            elif validate[0] < len(str(self.args.filename)):
                self.translate_file()
            else:
                print('Please enter a argument')
        except Exception as error:
            print(f'{error}')
        
if __name__ == '__main__':
    Translate().init()