from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings

Link="https://gpt4login.com/use-chatgpt-online-free/"

warnings.simplefilter("ignore")

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(Link)

def FileReader():
    File = open("Chatnumber.txt","r")
    Data = File.read()
    File.close()
    return Data

def FileWriter(Data):
    File = open("Chatnumber.txt","w")
    File.write(Data)
    File.close()
    
def ChatGPTBrain(Query):
    Query = str(Query)
    if "exit" in Query or "quit" in Query:
        return False
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/div/textarea").send_keys(Query)
    sleep(1)
    driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[2]/button/span").click()
    Data = str(FileReader())
    
    while True:

        sleep(0.5)
        
        try:
            AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
            Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).is_displayed()
            if str(Answer)=="True":
                break

        except:
            pass

    AnswerXpath = f"/html/body/div[1]/div/div/main/article/div/div/div/div/div/div/div[2]/div/div/div[1]/div[{Data}]/span[2]"
    Answer = driver.find_element(by=By.XPATH,value=AnswerXpath).text
    NewData = int(Data) + 2
    FileWriter(Data=str(NewData))
    return Answer

print("Starting The GPT4-Model.")
FileWriter(Data='3')

while True:
    try:
        file=open(r"../Body/SpeechRecognition.txt","r")
        data=file.read()
        file.close()
        fileHistory=open("HistoryChat.txt","r")
        dataHistory=fileHistory.read()
        fileHistory.close()
        
        if str(data)==str(dataHistory):
            sleep(0.5)
            pass
        else:
            result=ChatGPTBrain(data)
            if result==False:
                break
            print(result)

            fileHistory=open("HistoryChat.txt","w")
            fileHistory.write(data)
            fileHistory.close()
        
            
    except Exception as e:
        print(e)