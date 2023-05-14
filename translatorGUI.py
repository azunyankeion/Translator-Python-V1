from tkinter import *
import textblob
import googletrans
from googletrans import Translator
from tkinter import ttk, messagebox

translator = Translator()


#Definition of the clear function
def clear():
    text.delete(1.0, END)
    translated_text.delete(1.0, END)


def translating():
    try:
        for key, value in languages.items():
             if value == original_combo.get():
                  language_key = key
                  
        for key, value in languages.items():
             if value == translated_combo.get():
                  to_language_key = key.capitalize()
        
        words = textblob.TextBlob(text.get(1.0, END))
        words = words.translate(from_lang=language_key, to=to_language_key)
        translated_text.insert(1.0, words)


    except textblob.exceptions.NotTranslated:
         messagebox.showerror('Translator GUI V1', 'You put the wrong language to translate, put the correct language!')

    except Exception as e:
            messagebox.showerror('Translator GUI V1', e)

#Get The Languages List of GoogleTrans Library
languages = googletrans.LANGUAGES
language_list = list(languages.values())

#Start the Main Window and your configurations
root = Tk()
root.title('Translator GUI V1')
root.geometry('1400x800')
root.configure(background='gray')

#Definition and configurations of the text want to translate
text = Text(root, height=10, width=40, bg='blue')
text.grid(row=0, column=0, pady=20, padx=10)

#Configurations of the Translate Button
translate_button = Button(root, text='Translate Text', font=('Arial', 20), activebackground='red', command=translating)
translate_button.grid(row=0, column=1, padx=10)

#Translated Text and your configurations
translated_text = Text(root, height=10, width=40, bg='purple')
translated_text.grid(row=0, column=2, pady=20, padx=10)

#The List of languages of the original text
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

#The List of languages of the translate text
translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(26)
translated_combo.grid(row=1, column=2)


#Clear Button to translated text and text want to translate
clear_button = Button(root, text='Clear Text', command=clear, activebackground='green')
clear_button.grid(row=1, column=1, ipadx=20)


if __name__ == '__main__':
     root.mainloop()
