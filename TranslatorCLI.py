from googletrans import Translator
from time import sleep
import argparse


parser = argparse.ArgumentParser(
    description='Translate a phrases and words into whatever language you want', add_help=True)
parser.add_argument('-t', '--text',type=str,help='Enter the phrase you want to translate')
parser.add_argument('-f', '--filename',help='Enter the name of the file you want to translate')
args = parser.parse_args()
translator = Translator()

def translate_text():
    while True:
        try:
            lang_dest = input('Enter the language you want to translate, EXAMPLE: EN, PT, ES, JA, zh-tw(Chinese) ')
        except ValueError:
            print('Please enter a valid phrase or word')
        translating = translator.translate(str(args.text), dest=lang_dest.lower())     
        sleep(5)
        print(f'\n\nORIGINAL -> {translating.origin}, TRANSLATED -> {translating.text}\n\n')
        break


def translate_file():
    with open(args.filename, 'r', encoding='utf-8') as f:
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

validate = [0]
if args.text == None:
        args.text = str(args.text)
        args.text = ''
if args.filename == None:
    args.filename = str(args.filename)
    args.filename = ''
try: 
    if validate[0] < len(str(args.text)):
        translate_text()
    
    elif validate[0] < len(str(args.filename)):
        translate_file()
    else:
        print('Please enter a argument')
except Exception as error:
    print(f'{error}')