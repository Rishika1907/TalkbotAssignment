# importing the libraries
import pyttsx3
import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#function to convert text to speech  
def TextToSpeech(msg):
    #Getting a reference to an engine instance that will use the given driver.
    engine = pyttsx3.init()
    #Queues a command to speak an utterance
    engine.say(msg)
    #Blocks while processing all currently queued commands.
    #Returns when all commands queued before this call are emptied from the queue.
    engine.runAndWait()
    
#function to convert speech to text   
def SpeechToText():
    #recogniser instance
    r = sr.Recognizer()
    #creating an instance of the Microphone class
    mic = sr.Microphone()
    with mic as source:
        print("Listening....(Say Bye to end our conversation)")
        #speech input entered through microphone is saved as audio
        audio = r.listen(source)
        #invoking recognize_google() to attempt to recognize any speech in the audio 
        msg=r.recognize_google(audio)
        return msg

#instialising the chatbot norman       
bot = ChatBot('Norman')
#setting the trainer
bot.set_trainer(ChatterBotCorpusTrainer)
#Training with corpus data
bot.train('chatterbot.corpus.english')
#Calling TextToSpeech function
TextToSpeech("Welcome to my world")
TextToSpeech("I am Norman your AI assistant")
while(True):
    #obtaining text input from speech 
    message=SpeechToText()
    print("You : ",message)
    #if the message is bye quitting the chatbot
    if(message=='bye'):
        print('{}: See you Later !'.format(bot.name))
        TextToSpeech("See you Later!")
        break
    if(message!='BYE' or message!='bye'):  
        #getting the response for the given text input from the bot
        response=bot.get_response(message)
        TextToSpeech(response)
        #printing the response from the bot
        print("Norman : ",response)




    


  

