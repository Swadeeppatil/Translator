import tkinter as tk  
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 
from googletrans import Translator  
from tkinter import messagebox
import pyperclip as pc 
from gtts import gTTS  
import os
import speech_recognition as spr 

# ---------------------------------------------------Language Translator--------------------------------------------------------------


root = tk.Tk()
root.title('Langauge Translator')
root.geometry('1060x660')
root.maxsize(1060, 660)
root.minsize(1060, 660)

title_bar_icon = PhotoImage(file='C:/Users/swade/OneDrive/Desktop/Infotact Solutions/translator/res/translation.png')
root.iconphoto(False,title_bar_icon)
cl =''
output=''




frame = tk.Frame(root, bg='lightgreen')
frame.place(relwidth=1, relheight=1)

a = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20,textvariable=a, state='readonly', font=('Corbel', 20, 'bold'), )

auto_detect['values'] = (
    'Auto Detect',
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

auto_detect.place(x=50, y=140)
auto_detect.current(0)
l = tk.StringVar()





# combobox for to-language selection
choose_langauge = ttk.Combobox(root, width=20, textvariable=l, state='readonly', font=('Corbel', 20, 'bold'))
choose_langauge['values'] = (
    'Afrikaans',
    'Albanian',
    'Arabic',
    'Armenian',
    'Azerbaijani',
    'Basque',
    'Belarusian',
    'Bengali',
    'Bosnian',
    'Bulgarian',
    'Catalan',
    'Cebuano',
    'Chichewa',
    'Chinese',
    'Corsican',
    'Croatian',
    'Czech',
    'Danish',
    'Dutch',
    'English',
    'Esperanto',
    'Estonian',
    'Filipino',
    'Finnish',
    'French',
    'Frisian',
    'Galician',
    'Georgian',
    'German',
    'Greek',
    'Gujarati',
    'Haitian Creole',
    'Hausa',
    'Hawaiian',
    'Hebrew',
    'Hindi',
    'Hmong',
    'Hungarian',
    'Icelandic',
    'Igbo',
    'Indonesian',
    'Irish',
    'Italian',
    'Japanese',
    'Javanese',
    'Kannada',
    'Kazakh',
    'Khmer',
    'Kinyarwanda',
    'Korean',
    'Kurdish',
    'Kyrgyz',
    'Lao',
    'Latin',
    'Latvian',
    'Lithuanian',
    'Luxembourgish',
    'Macedonian',
    'Malagasy',
    'Malay',
    'Malayalam',
    'Maltese',
    'Maori',
    'Marathi',
    'Mongolian',
    'Myanmar',
    'Nepali',
    'Norwegian'
    'Odia',
    'Pashto',
    'Persian',
    'Polish',
    'Portuguese',
    'Punjabi',
    'Romanian',
    'Russian',
    'Samoan',
    'Scots Gaelic',
    'Serbian',
    'Sesotho',
    'Shona',
    'Sindhi',
    'Sinhala',
    'Slovak',
    'Slovenian',
    'Somali',
    'Spanish',
    'Sundanese',
    'Swahili',
    'Swedish',
    'Tajik',
    'Tamil',
    'Tatar',
    'Telugu',
    'Thai',
    'Turkish',
    'Turkmen',
    'Ukrainian',
    'Urdu',
    'Uyghur',
    'Uzbek',
    'Vietnamese',
    'Welsh',
    'Xhosa'
    'Yiddish',
    'Yoruba',
    'Zulu',
)

choose_langauge.place(x=600, y=140)
choose_langauge.current(0)

#------------------************* new**********______________
# Text area for input and output
input_text = Text(root, height=10, width=50, font=('Corbel', 16))
input_text.place(x=30, y=200)

output_text = Text(root, height=10, width=50, font=('Corbel', 16))
output_text.place(x=470, y=200)

translator = Translator()

def translate_text():
    input_lang = auto_detect.get()
    output_lang = l.get()
    text_to_translate = input_text.get("1.0", tk.END).strip()
    
    if not text_to_translate:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    
    try:
        translated = translator.translate(text_to_translate, src=input_lang, dest=output_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

def copy_text():
    translated_text = output_text.get("1.0", tk.END).strip()
    if translated_text:
        pc.copy(translated_text)
        messagebox.showinfo("Copied", "Translated text copied to clipboard.")

def read_aloud():
    text_to_read = output_text.get("1.0", tk.END).strip()
    if text_to_read:
        tts = gTTS(text=text_to_read, lang=l.get())
        tts.save("output.mp3")
        os.system("start output.mp3")  # This will work on Windows

def voice_input():
    recognizer = spr.Recognizer()
    with spr.Microphone() as source:
        messagebox.showinfo("Voice Input", "Please speak now...")
        audio = recognizer.listen(source)
        try:
            spoken_text = recognizer.recognize_google(audio)
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, spoken_text)
        except spr.UnknownValueError:
            messagebox.showerror("Voice Input Error", "Could not understand audio.")
        except spr.RequestError as e:
            messagebox.showerror("Voice Input Error", f"Could not request results; {e}")

translate_button = Button(root, text=" Translate Text ", compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                bg="#ffffff")
translate_button.place(x=40, y=565)

clear_button = Button(root, text=" Clear ", compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
               bg="#ffffff")
clear_button.place(x=270, y=565)

copy_button = Button(root, text=" Copy ", compound="right", relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                bg="#ffffff")
copy_button.place(x=485, y=565)

read_aloud = Button(root, text=" Read Aloud ", compound="right" ,relief=RIDGE, borderwidth=0, font=('Corbel', 20, 'bold'), cursor="hand2",
                bg="#ffffff")
read_aloud.place(x=650, y=565)

voice_input = Button(root, text=" Voice Input ",  compound="right", relief=RIDGE, borderwidth=0,
                     font=('Corbel', 20, 'bold'), cursor="hand2",  bg="#ffffff")
voice_input.place(x=850, y=565)

root.mainloop()