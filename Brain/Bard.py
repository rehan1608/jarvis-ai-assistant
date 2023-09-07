from bardapi import BardCookies
import datetime
from time import sleep

import pyperclip
import pyautogui
import webbrowser
from time import sleep
import json
import keyboard

def CookieScrapper():
    webbrowser.open("https://bard.google.com")
    sleep(5)
    pyautogui.click(x=1735, y=65)
    sleep(1)
    pyautogui.click(x=1510, y=248)
    sleep(1)
    pyautogui.click(x=1451, y=106)
    sleep(1)
    keyboard.press_and_release('ctrl + w')

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        pass

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDValue = next((item for item in json_data if item["name"] == SID), None)
    TSValue = next((item for item in json_data if item["name"] == TS), None)
    CCValue = next((item for item in json_data if item["name"] == CC), None)

    if SIDValue is not None:
        SIDValue = SIDValue["value"]
    else:
        # print(f"SIDValue not found in the JSON data.")
        pass

    if TSValue is not None:
        TSValue = TSValue["value"]
    else:
        # print(f"TSValue not found in the JSON data.")
        pass

    if CCValue is not None:
        CCValue = CCValue["value"]
    else:
        # print(f"CCValue not found in the JSON data.")
        pass

    cookie_dict = {
        "__Secure-1PSID": SIDValue ,
        "__Secure-1PSIDTS": TSValue,
        "__Secure-1PSIDCC": CCValue,
    }

    return cookie_dict

cookie_dict = CookieScrapper()


bard = BardCookies(cookie_dict=cookie_dict)

# Text Modification Function -

def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string


# Quiting function
def exit(q):
    if "quit" in q or "exit" in q:
        print("Quiting Please wait .",end="")
        for i in range(2):
            sleep(1)
            print(".",end="")
        sleep(1)
        return True
    
# Main Execution
while True:
    Question = input("Enter The Query : ")
    RealQuestion = str(Question)
    if exit(RealQuestion):
        break
    results = bard.get_answer(RealQuestion)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = r"DataBase/" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))
