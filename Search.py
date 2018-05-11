#catious run only with cmd, otherwise it might be dangerous
import smtplib
import speech_recognition as sr
import webbrowser as wb
import winspeech as ws
import time,os
from getpass import getpass

r=sr.Recognizer()

with sr.Microphone() as source:
    print("What you want Calculator, Email or Anything Else !")
    audio=r.listen(source)
    print('hello')
    we=r.recognize_google(audio)
    print('Begin')
    print(we)
    if 'cal' in we:
        print('''
            1. For Addition
            2. For Substraction
            3. For Multiplication
            4. For Division ''')
        
        choice=int(input('Enter your Choice : '))
        if choice == 1:
            first=int(input('Enter First Number: '))
            second=int(input('Enter Second Number: '))
            result=first+second
            ws.say('Output is '+ str(result))
            print('Output is '+ str(result))

        elif choice==2:
            first=int(input('Enter First Number: '))
            second=int(input('Enter Second Number: '))
            result=first-second
            ws.say('Output is '+str(result))
            print('Output is '+str(result))

        elif choice==3:
            first=int(input('Enter First Number: '))
            second=int(input('Enter Second Number: '))
            result=first*second
            ws.say('Output is ')
            print('Output is '+str(result))

        elif choice==4:
            first=int(input('Enter First Number: '))
            second=int(input('Enter Second Number: '))
            result=first/second
            ws.say('Output is '+str(result))
            print('Output is '+str(result))

            
    elif 'email' in we:
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
