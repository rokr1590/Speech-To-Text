import speech_recognition as sr
import webbrowser as wb
import mysql.connector as my
import time
from datetime import *

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

mycon=my.connect(host="localhost",user="root",passwd="1234",database="speech")
if mycon.is_connected()==False:
    print("Error Connecting to Database")


with sr.Microphone() as source:
 print('speak now')

 r3.adjust_for_ambient_noise(source, duration=0.0001)

 audio = r3.listen(source)


if 'hello' or 'namaste' or 'hi' in r2.recognize_google(audio):
  r2 = sr.Recognizer()
  with sr.Microphone() as source:
   print('listening............')
   audio = r2.listen(source)


  try:


   while True:
    t1 = datetime.now()
    d = date.today()
    print(d)
    get = r2.recognize_google(audio)
    print(get)


    url = "http://www.google.com/search?=en&q=" + get + "&btnG=Google+Search"

    # checking if the user says exit
    if get == 'exit':
        print("stopped")
        break


    wb.open_new_tab(url)
    mycursor = mycon.cursor()
    sql1 = "SELECT Srno FROM info ORDER BY Srno DESC LIMIT 1 "
    mycursor.execute(sql1)
    data = mycursor.fetchone()
    print(data)
    srn = 0;
    if type(data) == type(None):
        srn = 1;
    else:
        srn = data[0] + 1
    sql = "INSERT INTO info (Srno,Query,Date,Time)  VALUES (%s,%s, %s,%s)"
    val = (srn, get, str(d), str(t1))
    mycursor.execute(sql, val)
    mycon.commit()
    break

        #resolving error issues
  except sr.RequestError:
            print("error")
  except sr.UnknownValueError:
            print("failed")

