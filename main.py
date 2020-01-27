import speech_recognition as sr
import webbrowser
import time

# Initialize a recognizer, this is respoinsible for handling our speech queries
r = sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
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

def respond_to_query(voice_data):
    if 'what is your name' in voice_data:
        print("How kind of you to ask! My name is Pyri!")
    if 'what time is it' in voice_data:
        print(time.strftime('%H:%M'))
    if 'search' in voice_data:
        # ask for search query
        search = record_audio('What would you like to search for?')
        url = f"https://google.com/search?q={search}"
        webbrowser.get().open(url)
        print(f"OK, this is what I found on the topic of {search}.")
    if 'find location' in voice_data:
        location = record_audio("What's the name of the location you need help finding?")
        url = f"https://google.nl/maps/place/{location}/&amp;"
        webbrowser.get().open(url)
        print(f"OK, here's where {location} is located on the map.")
    if 'goodbye' in voice_data:
        print("Bye! See you soon!")
        exit()

def init():
    print('Hi! What can I do for you?')
    time.sleep(1)

    while 1:
        user_query = record_audio()
        respond_to_query(user_query)

init()