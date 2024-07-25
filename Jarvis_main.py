import datetime
from email import message
import subprocess
import webbrowser
from numpy import tile
import pyttsx3
import qrcode
import speech_recognition #pip install SpeechRecognition
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
import geocoder
from plyer import notification
from pygame import mixer
import speedtest #pip uninstall speedtest pip uninstall speedtest-cli pip install speedtest-cli
import Translator

mixer.init()

for i in range(3):  # giving 3 chances to user to give correct pass
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

from INTRO import play_gif
play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

def play_music():
    music_folder = "F:\\DJ SONGS\\simple"  # Update this with the path to your music folder
    songs = os.listdir(music_folder)
    song = random.choice(songs)
    song_path = os.path.join(music_folder, song)
    os.startfile(song_path)

def search_on_youtube(song_name):
    try:
        # Construct the YouTube search URL
        search_url = f"https://www.youtube.com/results?search_query={song_name.replace(' ', '+')}"

        # Open the web browser and search for the song on YouTube
        webbrowser.open(search_url)
    except Exception as e:
        print("An error occurred:", str(e))
        print("Sorry, I couldn't perform the search.")

def check_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / (1024 * 1024)  # Convert bytes to megabits
    upload_speed = st.upload() / (1024 * 1024)  # Convert bytes to megabits
    ping = st.results.ping

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

def get_current_location():
    try:
        # Get the current location based on IP address
        location = geocoder.ip('me')
        if location:
            return location.address
        else:
            return "Location not found."
    except Exception as e:
        print(f"Error occurred while getting location: {str(e)}")
        return "Location not found."

def open_location_in_maps(location):
    try:
        # Construct the Google Maps URL with the location
        maps_url = f"https://www.google.com/maps/place/{location}"
        
        # Open the URL in Chrome
        subprocess.Popen(['chrome', maps_url])
    except Exception as e:
        print(f"Error occurred while opening location in Google Maps: {str(e)}")

def generate_qr_code(text_or_url, filename="qr_code.png"):
    try:
        # Create QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code
        qr.add_data(text_or_url)
        qr.make(fit=True)

        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(filename)

        print(f"QR code generated successfully as {filename}")
    except Exception as e:
        print(f"Error occurred while generating QR code: {str(e)}")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok SIR , You can call me anytime")
                    break 
                
              ####################################################################

                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "professor details" in query:
                    speak("Hello, Professor [Teacher's Last Name]. It's a pleasure to meet you.")
                    speak("How may I assist you today? You can ask me questions, get information, or give me commands.")
                    while True:
                        teacher_query = takeCommand()
                        if teacher_query == "":
                            continue
                        if teacher_query.lower() == "exit":
                            speak("Goodbye, Professor. Have a great day!")
                            break
                        elif "how are you" in teacher_query.lower():
                            speak("I'm just a program, Professor, but thank you for asking.")
                        elif "tell me a joke" in teacher_query.lower():
                            speak("Why don't scientists trust atoms? Because they make up everything!")
                        elif "what's the weather like" in teacher_query.lower():
                            speak("I'm sorry, Professor, I cannot provide real-time weather information.")
                        elif "set a reminder" in teacher_query.lower():
                            speak("Sure, what would you like to be reminded of?")
                            reminder = takeCommand()
                            if reminder != "":
                                speak(f"Reminder set for {reminder}.")
                            else:
                                speak("I'm sorry, Professor. I'm still learning and may not be able to assist with that yet.")
                                

                elif "developer details" in query:
                    speak("My developer is techoverflows. He created me to assist with various tasks and make life easier.")
                    speak("If you have any questions or need further assistance, feel free to ask!")

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                    )

                elif "play music" in query:
                    play_music()

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)

                




                elif "open" in query:   #EASY METHOD
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")                       
                     
                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[5].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 10
                    )
                
                elif "play a game" in query:
                    from game import game_play
                    game_play()

                elif "screenshot" in query:
                     import pyautogui #pip install pyautogui
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")

                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                
                

                ############################################################
                elif "hello" in query:
                    speak("Hello Sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/Fxoxd0ovKn4?si=1tDMawOXarNXaHkP")
                    

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                
                
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()

                

                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                           
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"SIR, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())


                elif "search a song" in query:
                    speak("Sure, what song would you like to search for on YouTube?")
                    song_name = takeCommand()
                    search_on_youtube(song_name)
                
                elif ("meeting" in query):
                    speak("Ok sir opening meeet")
                    webbrowser.open("https://meet.google.com/")

                elif ("Gmail" in query):
                    speak("Ok Sir opening meeet")
                    webbrowser.open("https://mail.google.com/")    


                elif "check internet speed" in query:
                    check_internet_speed()
                    speak("Here are the current internet speed metrics.")

                elif "show my location" in query:
                    current_location = get_current_location()
                    print("Your current location is:", current_location)
                    speak(f"Your current location is {current_location}.")

                elif "open my location in maps" in query:
                    current_location = get_current_location()
                    open_location_in_maps(current_location)
                    speak("Opening your location in Google Maps.")

                elif "generate qr code" in query:
                    speak("Sure, please provide the text or URL for the QR code.")
                    text_or_url = takeCommand().lower()
                    filename = "qr_code.png"  # Default filename
                    generate_qr_code(text_or_url, filename)
                    speak("QR code generated successfully.")

                elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
                    
               



          

# https://newsapi.org/register/success
# https://newsapi.org/s/india-entertainment-news-api
# https://www.wolframalpha.com/

                


 