from googletrans import Translator
import arabic_reshaper
from bidi.algorithm import get_display

translator = Translator()

print('Welcome to the English to Arabic Translator')
print('Using Google Translate\n')

sentence = ""
while sentence != '-99':

   sentence = input('Enter English text (-99 to quit): ')
   if sentence == '-99':
      break

   #translate sentence
   translation_ar = translator.translate(sentence, dest='ar').text

   #format setence for command line
   translation_ar_cli = get_display(arabic_reshaper.reshape(translation_ar))

   #output to command line
   print('\nEnglish: ' + sentence)
   print('Arabic: ' + translation_ar_cli +'\n')

print('\n---end of program---\n')