import PyPDF2 
import pyttsx3    
import sys
print('######Ce programme permet de lire ou de creer un fichier audio du fichier pdf###### \n')
print("Exécuter le script sur ce format: python3 nom_du_script.py nom_du_fichiet.pdf 1\n")
print("le chiffre 1 de fin est pour préciser si vous voulez un fichier mp3 à la fin sinon mettez 0 à la place")
try:
    file = sys.argv[1]
    a=file.split('.')
    if a[1]!= 'pdf':
        print('le fichier doit etre un pdf')
        exit()
    
    createAudio= sys.argv[2]
except IndexError:
    print('vous devez passer en argument un fichier pdf et specifier si vous voules un ficher mp3 du pdf')
else:
    book = open(file,'rb')
    pdfReader = PyPDF2.PdfFileReader(book)

    speaker = pyttsx3.init()

    for page_num in range(pdfReader.numPages):
        text = pdfReader.getPage(page_num).extractText()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()
    if int(createAudio) == 1:
        speaker.save_to_file(text, 'audio.mp3')
    speaker.runAndWait()