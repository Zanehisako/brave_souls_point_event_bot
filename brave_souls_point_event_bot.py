import pyautogui
import time
import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

pyautogui.PAUSE = 2

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
                    pyautogui.locateCenterOnScreen(dir_path+"friend_request.png",minSearchTime=3)
                    pyautogui.click(x=1240,y=825)
                    
                    #request sent screen
                    pyautogui.locateCenterOnScreen(dir_path+"request_sent.png")
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


print("starting the script after 5 sec")
time.sleep(5)
print("script started !")
multiple_runs()