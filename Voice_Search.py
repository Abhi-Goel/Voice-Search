#catious run only with cmd, otherwise it might be dangerous
import smtplib
import speech_recognition as sr
import webbrowser as wb
import winspeech as ws
import time,os
from getpass import getpass

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something!")
    audio=r.listen(source)
    print('hello')
    we=r.recognize_google(audio)
    print('Begin')
    print(we)
    if 'email' or 'gmail' in we:
        ws.say('Enter your Email address')
        user_add=input("Your Email address : ")

        ws.say('Enter Password of your Email address')
        password=getpass('Enter password of email address : ')

        ws.say('Enter Reciever Email address')
        sender_add=input("Enter Reciever Email address : ")

        print("Speak Content of your Email : ")
        record=r.listen(source)
        content=r.recognize_google(record)

        mail=smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()

        #authentication with gmail

        mail.login(user_add,password)
        ws.say('Your Email has been sent')
        mail.sendmail(user_add,sender_add,content)
        time.sleep(2)
        mail.close()
        
                
    
    else:

        ws.say('I think you are looking for '+ we)
        print('I think you are looking for  : '+r.recognize_google(audio))
        search='http://www.google.com/#q='+we
        wb.open(search)
