import pyautogui
import time
import pytesseract
import os

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

pyautogui.PAUSE = 3

dir_path = 'C:/Users/yassi/OneDrive/Documents/scripts/brave_souls_point_event_bot/images/'

def get_tickets():
        pyautogui.screenshot(dir_path+'tickets_number.png',region=[920,20,40,30])
        ticketsNumber = int(pytesseract.image_to_string(dir_path+'tickets_number.png',lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
        print("ticketsNumber:",ticketsNumber)
        return ticketsNumber
    # except:
    #     print("error ticktes screen capture")

def single_run_point_event():
    state = 0
    while state != -1:
        match state:
            case 0:
                nightmareButtonLocationX,nightmareButtonLocationY = pyautogui.locateCenterOnScreen(dir_path+"Nightmare_event_button.png",confidence=0.5)
                try:
                    pyautogui.click(x=nightmareButtonLocationX,y=nightmareButtonLocationY)
                    state=1
                except:
                    print("didnt find the nightmare button")
            case 1:
                prepareForQuestLocationX,prepareForQuestLocationY = pyautogui.locateCenterOnScreen(dir_path+"prepare_for_quest_button.png",confidence=0.5)
                try:
                    pyautogui.click(x=prepareForQuestLocationX,y=prepareForQuestLocationY)
                    state=2
                except:
                    print("didnt find the prepare for quest button")
            case 2:
                try:
                    startQuestButtonLocationX,startQuestButtonLocationY = pyautogui.locateCenterOnScreen(dir_path+"start_quest_button.png",confidence=0.5)
                    pyautogui.click(x=startQuestButtonLocationX,y=startQuestButtonLocationY)
                    state=3
                except:
                    print("didnt find the start for quest button")
            case 3:
                try:
                    pyautogui.locateCenterOnScreen(dir_path+"boss_battle.png",confidence=0.5)
                    time.sleep(3.5)
                    try:
                        ultimateLocationX,ultimateLocationY = pyautogui.locateCenterOnScreen(dir_path+"ultimate_button.png",confidence=0.5)
                        pyautogui.click(x=ultimateLocationX,y=ultimateLocationY,clicks=2,interval=0.5)
                    except:
                        print("didnt find the ultimate button")
                    state=4
                except:
                    print("still no boss")
            case 4:
                try:
                    #this screen rarely shows up but when it does it fucks everything up
                    pyautogui.locateCenterOnScreen(dir_path+"friend_request.PNG",minSearchTime=3,confidence=0.5)
                    pyautogui.click(x=1240,y=825)
                    
                    #request sent screen
                    pyautogui.locateCenterOnScreen(dir_path+"request_sent.PNG",confidence=0.5)
                    pyautogui.click(x=965,y=750)
                except:
                    print("no friend request")

                try:
                    tapScreenLocationX,tapScreenLocationY = pyautogui.locateCenterOnScreen(dir_path+"TAP_SCREEN.png",confidence=0.5)
                    pyautogui.click(x=tapScreenLocationX,y=tapScreenLocationY,clicks=2,interval=1)
                    tapScreenLocationX,tapScreenLocationY = pyautogui.locateCenterOnScreen(dir_path+"TAP_SCREEN.png",confidence=0.5)
                    pyautogui.click(x=tapScreenLocationX,y=tapScreenLocationY)
                    state=5
                except:
                    print("didnt find the TAP SCREEN button")

            case 5:
                try:
                    closeLocationX,closeLocationY = pyautogui.locateCenterOnScreen(dir_path+"close_button.png",confidence=0.5)
                    pyautogui.click(x=closeLocationX,y=closeLocationY)
                    print("clicked CLOSE once")
                    try:
                        closeLocationX,closeLocationY = pyautogui.locateCenterOnScreen(dir_path+"close_button.png",confidence=0.5)
                        pyautogui.click(x=closeLocationX,y=closeLocationY)
                    except:
                        print("no second Lottery rewards")
                    state=6
                except:
                    print("didnt find the close button")

            case 6:
                try:
                    eventsLocationX,eventsLocationY = pyautogui.locateCenterOnScreen(dir_path+"events_button.png",confidence=0.5)
                    pyautogui.click(x=eventsLocationX,y=eventsLocationY)
                    state=-1
                except:
                    print("didnt find the events button")
    print("the single run finished successfully")

def multiple_runs():
    noTicketsLeft= False
    numberTickets =get_tickets()
    while(noTicketsLeft != True):
        imageOnScreen(dir_path+"loading_main_menu.png")
        time.sleep(5)
        numberTickets =get_tickets()

        if (numberTickets>=10):
            single_run_point_event()
        else:
            #clicks the menu button
            pyautogui.click(x=1875,y=60)

            #clicks the gift-box button
            pyautogui.click(x=1825,y=350)

            #clicks the Soul Tickets menu button
            pyautogui.click(x=765,y=165)

            try:
                #checks if there are no ticket gifts
                pyautogui.locateCenterOnScreen(dir_path+"no_tickets.png",minSearchTime=3,confidence=0.5)
                print("no more tickets")

                #clicks the close button
                pyautogui.click(x=965,y=975)

                noTicketsLeft=True

            except:
                #clicks the claim all button
                pyautogui.click(x=400,y=970)

                #clicks the ok confirme button
                pyautogui.click(x=1235,y=745)

                #clicks the close confirme button
                pyautogui.click(x=965,y=975)

                #clicks the close button
                pyautogui.click(x=965,y=975)

    
    print("out of tickets!\nEnded the runs")
    time.sleep(5)

def start_bleach():
    os.startfile(r"C:/Users/yassi/OneDrive/Desktop/BLEACH.url")
    state = 0
    while(state!=-1):
        match state:
            case 0:
                try:
                    imageOnScreen(dir_path+"loading_main_menu.png")
                    time.sleep(4)
                    mainX,mainY = pyautogui.locateCenterOnScreen(dir_path+"game_start.png",confidence=0.6)
                    pyautogui.click(x=mainX,y=mainY)
                    time.sleep(4)
                    try:
                        downloadButtonX,downloadButtonY = pyautogui.locateCenterOnScreen(dir_path+"yes_download_main_menu.png",confidence=0.9)
                        print("found download button")
                        pyautogui.click(x=downloadButtonX,y=downloadButtonY)
                    except:
                        print("no download to do")
                    time.sleep(5)
                    state = 1

                except:
                    print('didnt find main screen')

            #this case is for checking if there are any daily rewards
            case 1:
                try:
                    closeNewsX,closeNewsY = pyautogui.locateCenterOnScreen(dir_path+"close_news_button.png",minSearchTime=3,confidence=0.5)
                    pyautogui.click(x=closeNewsX,y=closeNewsY)
                except:
                    print("no news")

                try:
                    pyautogui.locateCenterOnScreen(dir_path+"daily_ticket_present.png",minSearchTime=2,confidence=0.5)
                    skipButtonX,skipButtonY = pyautogui.locateCenterOnScreen(dir_path+"skip_button.png",minSearchTime=2,confidence=0.5)
                    pyautogui.click(x=skipButtonX,y=skipButtonY)
                except:
                    pyautogui.click(x=960,y=540)
                    print("no tickets bonus")

                try:
                    loginBonusX,loginBonusY = pyautogui.locateCenterOnScreen(dir_path+"login_bonus.png",minSearchTime=2,confidence=0.5)
                    pyautogui.click(x=loginBonusX,y=loginBonusY)
                except:
                    print("no daily login rewards")


                #this selects the event 
                try:
                    soloButtonX,soloButtonY= pyautogui.locateCenterOnScreen(dir_path+"solo_button.png",confidence=0.5)
                    pyautogui.click(x=soloButtonX,y=soloButtonY)
                    try:
                        eventsButtonX,eventsButtonY= pyautogui.locateCenterOnScreen(dir_path+"events_main_button.png",confidence=0.5)
                        pyautogui.click(x=eventsButtonX,y=eventsButtonY)
                        time.sleep(10)
                        try:
                            currentEventButtonX,currentEventButtonY= pyautogui.locateCenterOnScreen(dir_path+"current_point_event.png",confidence=0.5)
                            pyautogui.click(x=currentEventButtonX,y=currentEventButtonY)
                            try:
                                questButtonX,questButtonY= pyautogui.locateCenterOnScreen(dir_path+"quest_to_be_played.png",confidence=0.9)
                                pyautogui.click(x=questButtonX,y=questButtonY)

                                state=-1

                            except:
                                print("didnt find the quest to play")
                        except:
                            print("didnt find the current event to play")

                    except:
                        print("didnt find the main events button")

                except:
                    print("didnt find solo button")

def exitGame():
    try:
        pyautogui.press('esc')
        foundQuestMenu = False
        while(foundQuestMenu!=True):
            try:
                pyautogui.locateCenterOnScreen(dir_path+"solo_quest_menu.png",confidence=0.5)
                pyautogui.press('esc')
                foundQuestMenu = True
            except:
                time.sleep(1)

        okButtonX,okButtonY = pyautogui.locateCenterOnScreen(dir_path+"ok_button.png",confidence=0.5)
        pyautogui.click(x=okButtonX,y=okButtonY)

        foundMainMenu= False
        while(foundMainMenu!=True):
            try:
                pyautogui.locateCenterOnScreen(dir_path+"game_start.png",confidence=0.6)
                pyautogui.press('esc')
                foundMainMenu= True
            except:
                time.sleep(1)

        okButtonX,okButtonY = pyautogui.locateCenterOnScreen(dir_path+"ok_button.png",confidence=0.5)
        pyautogui.click(x=okButtonX,y=okButtonY)
        
    except:
        print("Error closing the game")

def imageOnScreen(image):
    isOnscreen= False
    try:
        pyautogui.locateCenterOnScreen(dir_path+image,confidence=0.5)
        print("found image")
        while(isOnscreen!=False):
            try:
                pyautogui.locateCenterOnScreen(dir_path+image,confidence=0.5)
                isOnscreen=True
            except:
                isOnscreen=False
    except:
        time.sleep(0.5)





print("starting the script after 5 sec")
time.sleep(5)
print("script started !")
start_bleach()
multiple_runs()
exitGame()

