from tkinter import*
import googletrans
import textblob
from tkinter import ttk,messagebox
import pyttsx3  
import speech_recognition as sr



root = Tk()
root.title('Translation App')
root.geometry("800x300")
root.config(bg="black")

def translate():
   #Deleting previous translations
   translate_txt.delete(1.0,END)

   try:
    #get lang codes from dictionary
        for key , value in lang.items():
             if(value == original_drop.get()):
                from_lang_key = key
        for key , value in lang.items():
             if(value == translate_drop.get()):
                 to_lang_key = key
        #turns original text to textblob         
        words  = textblob.TextBlob(original_t.get(1.0 , END))
   
        #translate text
        words = words.translate(from_lang_key, to_lang_key)
   
        # output translated text into textbox

        translate_txt.insert(1.0, words)
        
        #speech output
        engine = pyttsx3.init()



        engine.say(words)

        engine.runAndWait()

   except Exception as e:
        messagebox.showerror("Error",e)

def clear():
      original_t.delete(1.0, END)
      translate_txt.delete(1.0,END)


def get_audio():
     r = sr.Recognizer()
     with sr.Microphone() as source:
          audio = r.listen(source)
          said  =""

          try:
               said  = r.recognize_google(audio)
               original_t.insert(1.0, said)
          except Exception as e:
                messagebox.showerror(e)

                

#GET LANG_LIST FROM GOOGLETRANS
lang = googletrans.LANGUAGES
language_list = list(lang.values())
         

#text 

original_t = Text(root , height= 10 , width=40)
original_t.grid(row=0, column=0 , pady=20, padx=10)
original_t.config(bg="red")

translate_btn = Button(root,text = "Translate" , font  = (24) , command = translate)
translate_btn.grid(row=0, column=1, padx = 10)


translate_txt  =  Text(root , height= 10 , width=40)
translate_txt.grid(row=0, column=2 , pady=20, padx=10)
translate_txt.config(bg="yellow")

#drop boxes

original_drop = ttk.Combobox(root , width = 50 , value = language_list)
original_drop.current(21)
original_drop.grid(row = 1 , column=0)

translate_drop = ttk.Combobox(root , width = 50 , value = language_list)
translate_drop.current(1)
translate_drop.grid(row = 1 , column=2)


#clear button 

clr_btn  = Button(root , text = "Clear" , command= clear)
clr_btn.grid(row=2 , column = 1 , padx = 10)

#Microphone input 
mic_btn =Button(root , text = "Microphone_Input" , command = get_audio)

mic_btn.grid(row=3 , column = 0 , padx = 10)


root.mainloop()
