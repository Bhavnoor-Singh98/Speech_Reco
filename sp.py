import speech_recognition as sr                               # for speech recognition
                                                              #import pyaudio for microphone
import webbrowser as wb                                       # to search on the web

r1=sr.Recognizer()                                            # recognizer class
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print('[To Open Google: Speak search]')
    print('[To Search on Youtube: Speak video]')
    print('Speak now')
    audio=r3.listen(source)

if 'search' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.google.com/search?'                        
    with sr.Microphone() as source:
        print("Speak Google")
        audio=r2.listen(source)

        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("Error")
        except sr.RequestError as e:
            print('failed'.format(e))
            
            
if 'video' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    with sr.Microphone() as source:
        print("Speak Your Query")
        audio=r1.listen(source)

        try:
            get=r1.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print("Error")
        except sr.RequestError as e:
            print('failed'.format(e))
