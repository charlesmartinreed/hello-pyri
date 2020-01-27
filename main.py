import speech_recognition as sr

# Initialize a recognizer, this is respoinsible for handling our speech queries
r = sr.Recognizer()
def record_audio():
    with sr.Microphone() as source:
        # captured audio from user
        audio = r.listen(source)
        voice_data = ''
        error_response = ''

        try:
            # user's voice query, processed using google's API
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            # unable to understand speech query
            error_response = "Apologies, but I couldn't understand that."
            return error_response
        except sr.RequestError:
            # can't connect to Google's servers or having a general networking error
            error_response = "I'm terribly sorry, but I'm having problems phoning home right now"
            return error_response
        return voice_data

def respond(voice_data):
    if 'what is your name' in voice_data:
        print("How kind of you to ask! My name is Pyri!")

print('Hi! What can I do for you?')
user_query = record_audio()

respond(user_query)