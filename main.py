import speech_recognition as sr

# Initialize a recognizer, this is respoinsible for handling our speech queries
r = sr.Recognizer()

with sr.Microphone() as source:
    print('Try saying something... ')
    # captured audio from user
    audio = r.listen(source)
    # user's voice query, processed using google's API
    voice_data = r.recognize_google(audio)
    print(voice_data)