# VirtualAssistant


ThisVirtualAssistant will help you to access and open other pages and applications from your running program with the help of
your voice- Commands.

echo fun: will speak the text which was given to it as output  through inbuilt speakers of PC.
Here in windows we used the SAPI API to get the default voices in windows for echoing.

speech_recognition(module): used it to recognize the text through microphones...
This speech_recognition function takes the microphone input of voice and converts into text. This helps in giving commands to the Virtual Assistant.

booting fun: This function will be called first whenever the program is executed. This funtion wishes the user according to the time.
This improves the user experience and he can feel it like a real virtual assistant assisting him.

Userinput fun: It takes the microphone input and returns us the query which we will use in looping statements to perform some actions.

We used pyttsx3 module which is a text to speech covertion library in python because it provides us several fields which helps us in easily convert the text into speech.
