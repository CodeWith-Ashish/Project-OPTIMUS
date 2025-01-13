# Imporing Modules -------------------------------------------------------------------------------------------------------------------------------

import pyttsx3
import speech_recognition as sr
import os
import requests
from bs4 import BeautifulSoup
import pyautogui
from time import sleep  
import datetime 
import speedtest
from deep_translator import GoogleTranslator

# Defining Functions -----------------------------------------------------------------------------------------------------------------------------

pyautogui.FAILSAFE = False
speech_rate = 175
user_home = os.path.expanduser('~')
user = os.path.split(user_home)[-1]
username = user

def speak(text):
    engine=pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice',Id)
    engine.setProperty('rate',speech_rate)
    print(f"====> OPTIMUS : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()

def speechrecognition(): # Voice input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
    try:
        print("Recognizing...")
        print()
        query = r.recognize_google(audio,language="en")
        return query.lower()
    except:
        return ""
    
def open_app(name,task): # For opening applications
    speak(f"Opening {name}")
    os.system(f"start {task}")
def close_app(name,process): # For closing applications
    speak(f"Closing {name}")
    os.system(f"taskkill /f /im {process}")
    
def MainExecution(Query):
    Query = str(Query).lower()

# 1) Normal Interactions -------------------------------------------------------------------------------------------------------------------------------
    
    if "hello" in Query:
        speak("Hello sir, how are you?")

    elif "how r u" in Query:
        speak("I am fine, thankyou")

    elif "what about you" in Query:
        speak("I am also fine, thankyou")

    elif "wake up jarvis" in Query:
        speak("I am always here sir.")

    elif "are you here" in Query:
        speak("Yes sir, I am always here.")
             
    elif "introduce yourself" in Query or "something about you" in Query:
        speak("I am Jarvis. Just a Rather Very Intelligent System. I am a Voice-Based Assistant developed in Python Programming Language.")
        
    elif "bye" in Query:
        speak("Nice to meet you, Have a nice day.")
        
    elif "who developed you" in Query:
        speak("I am developed by Ashish.")

    elif "thanks" in Query:
        speak("You're welcome sir")

# 2) Access of System Applications -----------------------------------------------------------------------------------------------------------------------------------------------------
    
    elif ("open notepad" in Query or
           "open paint" in Query or
           "open wordpad" in Query or
           "open snipping tool" in Query or
           "open calculator" in Query or
           "open cmd" in Query or
           "open terminal" in Query or
           "open control panel" in Query or
           "open file explorer" in Query or
           "open settings" in Query or
           "open windows security" in Query or
           "open task manager" in Query or
           "open registory editor" in Query or
           "open edge" in Query or
           "open character map" in Query
           ):
        
        sys_apps = {
        "notepad": "notepad.exe",
        "paint": "mspaint.exe",
        "wordpad": "wordpad.exe",
        "snipping tool": "SnippingTool.exe",
        "calculator": "calc.exe",
        "cmd": "cmd",
        "terminal": "powershell.exe",
        "control panel": "control.exe",
        "file explorer": "explorer.exe",
        "settings": "ms-settings:",
        "windows security": "ms-settings:windowsdefender",
        "task manager": "taskmgr.exe",
        "registry editor": "regedit.exe",
        "edge": "msedge.exe",
        "character map": "charmap.exe"
        }

        name = Query.replace('open','').replace(' ','')
        if name in sys_apps:
            task = sys_apps[name]
            open_app(name,task)

    elif ("close notepad" in Query or
           "close paint" in Query or
           "close wordpad" in Query or
           "close snipping tool" in Query or
           "close calculator" in Query or
           "close cmd" in Query or
           "close terminal" in Query or
           "close control panel" in Query or
           "close file explorer" in Query or
           "close settings" in Query or
           "close windows security" in Query or
           "close task manager" in Query or
           "close registory editor" in Query or
           "close edge" in Query or
           "close character map" in Query
           ):
        
        sys_apps = {
        "notepad": "notepad.exe",
        "paint": "mspaint.exe",
        "wordpad": "wordpad.exe",
        "snipping tool": "SnippingTool.exe",
        "calculator": "CalculatorApp.exe",
        "cmd": "cmd",
        "terminal": "powershell.exe",
        "control panel": "control.exe",
        "file explorer": "explorer.exe",
        "settings": "SystemSettings.exe",
        "windows security": "ms-settings:windowsdefender",
        "task manager": "taskmgr.exe",
        "registry editor": "regedit.exe",
        "edge": "msedge.exe",
        "character map": "charmap.exe"
        }
    
        name = Query.replace('close','').replace(' ','')
        if name in sys_apps:
            task = sys_apps[name]
            close_app(name,task)

# 3) Some Pre-defined Applications -------------------------------------------------------------------------------------------------------------------------------------------------------

    # MS Word
    elif "open ms word" in Query or "open word" in Query or "close ms word" in Query or "close word" in Query:
        if "open ms word" in Query or "open word" in Query:
            speak("Opening MS Word")
            try:
                os.system("start winword")
            except:
                speak("MS Word not found. May be its not installed on your device")
        elif "close ms word" in Query or "close word" in Query:
            close_app("MS Word","winword.exe")


    # Excel
    elif "open excel" in Query or "close excel" in Query:
        if "open excel" in Query:
            speak("Opening Excel")
            try:
                os.system("start excel.exe")
            except:
                speak("Excel not found. May be its not installed on your device")
        elif "close excel" in Query:
            close_app("Excel","excel.exe")


    # Powerpoint
    elif "open powerpoint" in Query or "close powerpoint" in Query:
        if "open powerpoint" in Query:
            speak("Opening Powerpoint")
            try:
                os.system("start Powerpnt.exe")
            except:
                speak("Powerpoint not found. May be its not installed on your device")
        elif "close powerpoint" in Query:
            close_app("Powerpoint","Powerpnt.exe")


    # Chrome
    elif "open chrome" in Query or "close chrome" in Query:
        if "open chrome" in Query:
            open_app("Chrome","chrome.exe")
        elif "close chrome" in Query:
            close_app("Chrome","chrome.exe")


    # Whatsapp
    elif "open whatsapp" in Query or "close whatsapp" in Query:
        if "open whatsapp" in Query:
            speak("Opening Whatsapp")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\WhatsApp - Shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("https://web.whatsapp.com/")
                pyautogui.press("enter")
        elif "close whatsapp" in Query:
            close_app("Whatsapp","WhatsApp.exe")


    # Instagram
    elif "open instagram" in Query or "close instagram" in Query:
        if "open instagram" in Query:
            speak("Opening Instagram")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\Instagram - Shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("https://www.instagram.com/?hl=en")
                pyautogui.press("enter")
        elif "close instagram" in Query:
            close_app("Instagram","pwahelper.exe")


    # Telegram
    elif "open telegram" in Query or "close telegram" in Query:
        if "open telegram" in Query:
            speak("Opening Telegram")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\Telegram - Shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("https://web.telegram.org/")
                pyautogui.press("enter")
        elif "close telegram" in Query:
            close_app("Telegram","Telegram.exe")


    # YouTube
    elif "open youtube" in Query or "close youtube" in Query:
        if "open youtube" in Query:
            speak("Opening Youtube")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\YouTube - Shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("https://www.youtube.com/")
                pyautogui.press("enter")
        elif "close youtube" in Query:
            close_app("Youtube","msedge.exe")


    # Chat GPT
    elif "open chat gpt" in Query or "close chat gpt" in Query:
        if "open chat gpt" in Query:
            speak("Opening Chat GPT")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\ChatGPT - Shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("https://chat.openai.com/")
                pyautogui.press("enter")
        elif "close chat gpt" in Query:
            close_app("Chat GPT","msedge.exe")


    # Google Drive
    elif "open google drive" in Query or "close google drive" in Query:
        if "open google drive" in Query:
            speak("Opening Google Drive")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\Google Drive - Shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("https://drive.google.com/")
                pyautogui.press("enter")
        elif "close google drive" in Query:
            close_app("Google Drive","msedge.exe")


    # Gmail
    elif "open gmail" in Query or "close gmail" in Query:
        if "open gmail" in Query:
            speak("Opening Gmail")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\Gmail - Shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("https://mail.google.com/mail/u/0/")
                pyautogui.press("enter")
        elif "close gmail" in Query:
            close_app("Gmail","msedge.exe")


    # Google Keep Notes
    elif "open keep notes" in Query or "close keep notes" in Query:
        if "open keep notes" in Query:
            speak("Opening Keep Notes")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\Google Keep - Shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("https://keep.google.com/")
                pyautogui.press("enter")
        elif "close keep notes" in Query:
            close_app("Keep Notes","msedge.exe")


    # Physics Wallah
    elif "open pw" in Query or "open physics wallah" in Query or "close pw" in Query or "close physics wallah" in Query:
        if "open pw" in Query or "open physics wallah" in Query:
            speak("Opening PW")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\Physics Wallah - shortcut.lnk")
            except:
                os.system("start msedge")
                sleep(4)
                pyautogui.typewrite("pw.live")
                pyautogui.press("enter")
        elif "close pw" in Query or "close physics wallah" in Query:
            close_app("PW","msedge.exe")


    # Python
    elif "open python" in Query or "close python" in Query:
        if "open python" in Query:
            speak("Opening Python")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\IDLE (Python 3.12 64-bit) - Shortcut.lnk")
            except:
                speak("Python not found. May be you are using older version or its not installed on your device")
        elif "close python" in Query:
            close_app("Python","pythonw.exe")


    # MySQL
    elif "open mysql" in Query or "close mysql" in Query:
        if "open mysql" in Query:
            speak("Opening MySQL")
            try:
                os.startfile(f"C:\\Users\\{username}\\Shortcuts\\MySQL 8.0 Command Line Client - Shortcut.lnk")
            except:
                speak("MySQL not found. May be you are using older version or its not installed on your device")
        elif "close mysql" in Query:
            close_app("MySQL","WindowsTerminal.exe")

# 4) Access of User Applications ----------------------------------------------------------------------------------------------------------------------------

    elif "launch" in Query:
        app = Query.replace('launch','').capitalize()
        speak(f"Launching {app}")
        pyautogui.press("super")
        sleep(0.5)
        pyautogui.typewrite(app)
        sleep(1)
        pyautogui.press("enter")

# 5) Files & Folder Access -------------------------------------------------------------------------------------------------------------------------
    
    elif "open downloads" in Query:
        speak("Opening Downloads folder")
        os.startfile(f"C:\\Users\\{username}\\Downloads")

    elif "open documents" in Query:
        speak("Opening Documents folder")
        os.startfile(f"C:\\Users\\{username}\\OneDrive\\Documents")

    elif "open pictures" in Query:
        speak("Opening Pictures folder")
        os.startfile(f"C:\\Users\\{username}\\OneDrive\\Pictures")

    elif "open music" in Query:
        speak("Opening Music folder")
        os.startfile(f"C:\\Users\\{username}\\Music")

    elif "open videos" in Query:
        speak("Opening Videos folder")
        os.startfile(f"C:\\Users\\{username}\\Videos")

    elif "open saved pictures" in Query:
        speak("Opening saved pictures")
        os.startfile(f"C:\\Users\\{username}\\OneDrive\\Pictures\\Saved Pictures")

    elif "open screenshots" in Query:
        speak("Opening screenshots")
        os.startfile(f"C:\\Users\\{username}\\OneDrive\\Pictures\\Screenshots")

    elif "open user folder" in Query:
        speak("Opening user folder")
        os.startfile(f"C:\\Users\\{username}")

    elif "open recycle bin" in Query:
        speak("Opening recycle bin")
        os.startfile('shell:RecycleBinFolder')

# 6) Keyboard configuration --------------------------------------------------------------------------------------------------------------------------

    # Numlock, Capslock, Scroll-lock   
    elif "num lock" in Query:
        speak("Ok")
        pyautogui.press("numlock")
    elif "caps lock" in Query:
        speak("Ok")
        pyautogui.press("capslock")
    elif "scroll lock" in Query:
        speak("Ok")
        pyautogui.press("scrolllock")


    # Usual Keys
    elif "press enter" in Query:
        pyautogui.press("enter")
    elif "press space" in Query:
        pyautogui.press("space")
    elif "press backspace" in Query:
        pyautogui.press("backspace") 
    elif "press tab" in Query:
        pyautogui.press("tab")
    elif "press esc" in Query or "press escape" in Query:
        pyautogui.press("esc")
    elif "press left" in Query:
        pyautogui.press("left")
    elif "press right" in Query:
        pyautogui.press("right")
    elif "press up" in Query:
        pyautogui.press("up")
    elif "press down" in Query:
        pyautogui.press("down")


    # Function Keys
    elif "press f1" in Query or "open help" in Query:
        pyautogui.press("F1")
    elif "press f2" in Query:
        pyautogui.press("F2")
    elif "press f3" in Query:
        pyautogui.press("F3")
    elif "press f4" in Query:
        pyautogui.press("F4")
    elif "press f5" in Query or "refresh" in Query:
        pyautogui.press("F5")
    elif "press f6" in Query:
        pyautogui.press("F6")
    elif "press f7" in Query:
        pyautogui.press("F7")
    elif "press f8" in Query:
        pyautogui.press("F8")
    elif "press f9" in Query:
        pyautogui.press("F9")
    elif "f10" in Query:
        pyautogui.press("F10")
    elif "full screen mode" in Query:
        pyautogui.press("f11")
    elif "inspect this page" in Query:
        pyautogui.press("f12")


    # Some Usual Shortcuts
    elif "select all" in Query:
        pyautogui.hotkey('ctrl','a')
        speak("selected")
    elif "copy selection" in Query:
        pyautogui.hotkey('ctrl','c')
        speak("selection Copied")
    elif "cut selection" in Query:
        pyautogui.hotkey('ctrl','x')
        speak("Done")
    elif "paste" in Query:
        pyautogui.hotkey('ctrl','v')
        speak("Pasted Successfully")
    elif "undo" in Query:
        pyautogui.hotkey('ctrl','z')
    elif "redo" in Query:
        pyautogui.hotkey('ctrl','y')
    elif "delete this" in Query or "delete selection" in Query:
        speak("Ok")
        pyautogui.press("delete")


    # Few Shortcuts for MS Word
    elif "bold text" in Query:
        pyautogui.hotkey('ctrl','b')
    elif "italic text" in Query:
        pyautogui.hotkey('ctrl','i')
    elif "underline text" in Query:
        pyautogui.hotkey('ctrl','u')
    elif "left align" in Query:
        pyautogui.hotkey('ctrl','l')
    elif "right align" in Query:
        pyautogui.hotkey('ctrl','r')
    elif "centre align" in Query:
        pyautogui.hotkey('ctrl','e')
    
# 7) Window Operations -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif "new tab" in Query:
        pyautogui.hotkey('ctrl','t')
    elif "new window" in Query:
        pyautogui.hotkey('ctrl','n')
    elif "private window" in Query:
        pyautogui.hotkey('ctrl','shift','n')
    elif "close window" in Query or "close app" in Query or "close this app" in Query:
        speak("Closing...")
        pyautogui.hotkey('alt','F4')

    elif "close this tab" in Query or "close tab" in Query:
        speak("Closing")
        pyautogui.hotkey('ctrl','w')
    elif "open last tab" in Query:
        pyautogui.hotkey('ctrl','shift','t')

    elif Query == "play" or Query == "pause":
        pyautogui.press("space")
    elif Query == "mute" or Query == "unmute":
        pyautogui.press("m")

# 8) System Operations ------------------------------------------------------------------------------------------------------------------------------------------
   
    elif "switch window" in Query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        sleep(1)
        pyautogui.keyUp("alt")

    elif "show desktop" in Query:
        speak("Navigating desktop")
        pyautogui.hotkey('win','d')

    elif "shutdown the system" in Query:
        speak("Shutting down the system")
        os.system("shutdown /s /t 0")

    elif "restart the system" in Query:
        speak("Restarting...")
        os.system("shutdown /r /t 0")
        
    elif "sleep the system" in Query:
        speak("Sending system to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "turn on dark mode" in Query or "turn off dark mode" in Query:
        if "turn on dark mode" in Query:
            speak("Turning on dark mode...")
            os.system('powershell -Command "Set-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name AppsUseLightTheme -Value 0"')
        elif "turn off dark mode" in Query:
            speak("Turning off dark mode...")
            os.system('powershell -Command "Set-ItemProperty -Path HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize -Name AppsUseLightTheme -Value 1"')

# 9) Screenshot and Camera --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif "take screenshot" in Query or "take a screenshot" in Query:
        speak("Ok, please tell me the name for this screenshot file.")
        name = speechrecognition().lower()
        speak("Hold on, I am taking screenshot.")
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("Screenshot saved.")

    elif "take a picture" in Query or "click a picture" in Query:
        speak("Ok")
        pyautogui.press("super")
        sleep(0.5)
        pyautogui.typewrite("camera")
        sleep(0.7)
        pyautogui.press("enter")
        sleep(2)
        pyautogui.press("enter")

# 10) Miscellaneous Commands --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    # Rename files or folders
    elif "rename" in Query:
        pyautogui.press("F2")
        speak("Tell me the new name for this")
        new_name = speechrecognition().capitalize()
        pyautogui.typewrite(new_name)
        pyautogui.press("enter")
        speak("Rename successful")
        
    # Create new folder
    elif "create new folder" in Query:
        speak("Ok, tell me the name for the new folder")
        folder_name = speechrecognition().capitalize()
        pyautogui.hotkey('ctrl','shift','n')
        sleep(1)
        pyautogui.typewrite(folder_name)
        sleep(0.5)
        pyautogui.press("enter")
        speak("Done, new folder created")

    # Empty recycle bin
    elif "clear recycle bin" in Query:
        speak("Ok")
        os.startfile("shell:RecycleBinFolder")
        sleep(1)
        pyautogui.hotkey('ctrl','a')
        sleep(0.5)
        pyautogui.press("delete")
        sleep(2)
        pyautogui.press("enter")
        speak("Done")
        pyautogui.hotkey('alt','f4')

    # Open any drive
    elif "open" in Query and "drive" in Query:
        drive = Query.replace("open","").replace("drive","").replace(" ","").upper()
        speak(f"Opening {drive} drive")
        path = f"{drive}:\\"
        path = path.replace(" ","")
        try:
            os.startfile(path)
        except:
            speak(f"{drive} drive not found")
        
# 11) Voice Typing ----------------------------------------------------------------------------------------------------------------------------------------
        
    elif "activate typing mod" in Query or "type" in Query:
        if "type" in Query:
            typing = Query.replace("type","")
            pyautogui.typewrite(typing)
        else:
            speak("Initializing typing mode.")
            speak("Typing mode activated. Speak what you want to type.")
            while True:
                typing = speechrecognition().replace("full stop",". ").replace("space"," ").replace("comma",",")
                if typing == "stop typing mode":
                    speak("Typing mode deactivated")
                    break
                pyautogui.typewrite(typing)

# 12) Mathematical Calculations --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif "calculate" in Query:
        print("Query :",Query)
        expression = Query.replace('calculate','').replace('bracket open','(').replace('bracket close',')').replace('plus','+').replace('minus','-').replace('into','*').replace('by','/').replace('multiplied by','*').replace('divided by','/')
        print("Expression :",expression)
        try:
            answer = eval(expression)
            speak(answer)
        except:
            speak("Invalid input, please try again")

# 13) Date & Time Access --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif "date" in Query:
        from datetime import datetime
        today = datetime.today().strftime("%B %d %Y")
        speak(f"Today's date is {today}")

    elif "time" in Query:
        from datetime import datetime
        time = datetime.now().strftime("%I:%M %p")
        speak(f"The time now is {time}") 

# 14) Weather Information ----------------------------------------------------------------------------------------------------------------------------------------

    elif "temperature" in Query or "weather condition" in Query:
        search = "temperature"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div",class_="BNeawe").text
        speak(f"Current {search} is {temp}")

# 15) Search Information from Internet ---------------------------------------------------------------------------------------------------------------------------
    
    elif "tell me" in Query:
        Query = Query.replace('tell me','')
        url = f"https://www.google.com/search?q={Query}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        result = data.find("div",class_="BNeawe").text
        speak(result)
        
# 16) Google Search ----------------------------------------------------------------------------------------------------------------------------------------------

    elif "search on google" in Query:
        speak("Google is listening you, speak what you want to search")
        search = speechrecognition()
        speak("Searching...")
        os.system("start msedge.exe")
        sleep(4)
        pyautogui.typewrite(search)
        pyautogui.press("enter")
        sleep(1)
        speak("Here is the result")

# 17) Youtube Search ------------------------------------------------------------------------------------------------------------------------------------------

    elif "search on youtube" in Query:
        speak("Ok, tell me what you want to search on youtube")
        Q = speechrecognition()
        speak("Searching...")
        try:
            os.startfile(f"C:\\Users\\{username}\\Shortcuts\\YouTube - Shortcut.lnk")
            sleep(5)
        except:
            os.system("start msedge")
            sleep(4)
            pyautogui.typewrite("https://www.youtube.com/")
            pyautogui.press("enter")
        sleep(5)
        pyautogui.press("/")
        pyautogui.typewrite(Q)
        sleep(2)
        pyautogui.press("enter")
        speak("Here is the result")

# 18) Interaction with ChatGPT ----------------------------------------------------------------------------------------------------------------------------------------------------

    elif "ask chat gpt" in Query:
        speak("Ok, tell me what is your query")
        Query = speechrecognition()
        speak("Asking your query from Chat GPT...")
        try:
            os.startfile(f"C:\\Users\\{username}\\Shortcuts\\ChatGPT - Shortcut.lnk")
        except:
            os.system("start msedge")
            sleep(4)
            pyautogui.typewrite("https://chat.openai.com/")
            pyautogui.press("enter")
        sleep(5)
        pyautogui.typewrite(Query)
        sleep(3)
        pyautogui.press("enter")
        sleep(1)
        speak("Here is the result")

# 19) Send Whatsapp Message ----------------------------------------------------------------------------------------------------------------------------------------

    elif "send whatsapp message" in Query:
        speak("Sure, tell me the receiver's name")
        name = speechrecognition()
        speak("Opening whatsapp...")
        try:
            os.startfile(f"C:\\Users\\{username}\\Shortcuts\\WhatsApp - Shortcut.lnk")
            sleep(3)
            pyautogui.typewrite(name)
            sleep(2)
            pyautogui.press("down")
            sleep(1)
            pyautogui.press("enter")
            speak("Typing mode initiated. Now tell me the message you want to send")
            while True:
                message = speechrecognition()
                message = message.replace("full stop",". ").replace("space"," ").replace("comma",",")
                if message == "message complete":
                    speak("Ok")
                    sleep(1)
                    pyautogui.press("enter")
                    speak("Message Sent")
                    break
                pyautogui.typewrite(message.capitalize())
        except:
            speak("Some error occured, may be whatsapp is not installed on your device. Please make sure you have latest version of whatsapp to use this feature.")

# 20) Send Email ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif "send email" in Query:
        speak("Sure, tell me the receiver's EMail ID")
        id = input("Recipient Email : ")
        id = id.replace('at','@').replace('dot','.').replace(" ","")
        speak("Sending email...")
        os.system("start msedge")
        sleep(4)
        pyautogui.typewrite("https://mail.google.com/mail/u/0/#inbox?compose=new")
        pyautogui.press("enter")
        sleep(8)
        pyautogui.typewrite(id)
        sleep(3)
        pyautogui.press("enter")
        sleep(0.5)
        pyautogui.press("tab")
        speak("Tell me the subject of this EMail")
        subject = speechrecognition()
        subject = subject.capitalize()
        if subject == "No subject" or subject == "Leave subject empty":
            speak("Ok")
            pyautogui.press("tab")
        else:
            pyautogui.typewrite(subject)
        pyautogui.press("tab")
        speak("Typing mode initiated. Now tell me the message you want to send")
        while True:
            message = speechrecognition()
            message = message.replace("full stop",". ").replace("space"," ").replace("comma",",")
            if message == "message complete":
                speak("Ok")
                sleep(1)
                pyautogui.hotkey('ctrl','enter')
                sleep(1)
                pyautogui.press("enter")
                speak("Email Sent")
                break
            pyautogui.typewrite(message.capitalize())

# 21) Play Music --------------------------------------------------------------------------------------------------------------------------------------------------------

    elif "play music" in Query or "play some music" in Query:
        speak("Ok")
        speak("Playing music...")
        os.startfile(f"C:\\Users\\{username}\\Music")
        sleep(1)
        pyautogui.hotkey('ctrl','a')
        pyautogui.press("enter")

# 22) Internet Speed ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif "internet speed" in Query:
        speak("Ok, getting internet speed, it will take atleast 45 seconds.")
        print("Runing internet speed test...")
        net_speed = speedtest.Speedtest()
        up = net_speed.upload()*0.000000125
        up = round(up, 2)
        down = net_speed.download()*0.000000125
        down = round(down, 2)
        print("Internet speed test completed")
        print()
        speak(f"Upload Speed is {up} MB per second")
        speak(f"Download Speed is {down} MB per second")

# 23) Language Translator ----------------------------------------------------------------------------------------------------------------------------------------------

    elif "translate language" in Query:
        speak("Sure, enter the text below which you want to translate")
        text = input("Enter the text you want to translate : ")
        print()
        speak("Ok, now enter the target language.")
        target_language = input("Enter the language : ")
        result = GoogleTranslator(source='auto', target=target_language).translate(text)
        speak("Here is the result")
        print(result)

# 24) Program Control Centre -------------------------------------------------------------------------------------------------------------------------
    
# a) Restart or Terminate (close) the program
    elif "restart program" in Query or "reset yourself" in Query or "restart your program" in Query:
        speak("Ok")
        speak("Restarting program...")
        pyautogui.hotkey('ctrl','shift','F5')
    elif "terminate" in Query or "you can sleep" in Query:
        speak("Ok, Have a good day !!!")
        pyautogui.hotkey("win","d")
        os._exit(0) 

# b) Automate the editing of speech rate 
    elif "change your speech rate" in Query:
        speak("Initializing System Manipulation...")
        speak("What should be the new speech rate?")
        new_speed = speechrecognition()
        speak("Ok, hold on")
        a = str(speech_rate)
        old_speed = len(a)
        pyautogui.hotkey('ctrl','g')
        pyautogui.typewrite("17")
        pyautogui.press("enter")
        pyautogui.press("end")
        if old_speed == 1:
            pyautogui.press("backspace")
        elif old_speed == 2:
            pyautogui.press("backspace")
            pyautogui.press("backspace")
        elif old_speed == 3:
            pyautogui.press("backspace")
            pyautogui.press("backspace")
            pyautogui.press("backspace")
        elif old_speed == 4:
            pyautogui.press("backspace")
            pyautogui.press("backspace")
            pyautogui.press("backspace")
            pyautogui.press("backspace")
        sleep(1)
        pyautogui.typewrite(new_speed)
        speak("System manipulation completed")
        speak("Restarting the program...")
        pyautogui.hotkey('ctrl','shift','F5')

# 25) Greet on Running Program ------------------------------------------------------------------------------------------------------------------------

hr = int(datetime.datetime.now().hour)
if hr>=0 and hr<12:
    speak("Good Morning")
elif hr>=12 and hr<17:
    speak("Good Afternoon")
else: 
    speak("Good Evening")
speak("How can I help you?")

while True:
    Query = speechrecognition()
    MainExecution(Query)