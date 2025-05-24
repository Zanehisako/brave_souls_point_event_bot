import pyautogui
import time
import pytesseract

from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

pyautogui.PAUSE = 2

def get_tickets():
        pyautogui.screenshot('tickets_number.png',region=[920,20,40,30])
        ticketsNumber = int(pytesseract.image_to_string('tickets_number.png',lang='eng',config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'))
        print("ticketsNumber:",ticketsNumber)
        return ticketsNumber
    # except:
    #     print("error ticktes screen capture")

def single_run_point_event():
    state = 0
    while state != -1:
        match state:
            case 0:
                nightmareButtonLocationX,nightmareButtonLocationY = pyautogui.locateCenterOnScreen("Nightmare_event_button.png",confidence=0.5)
                try:
                    pyautogui.click(x=nightmareButtonLocationX,y=nightmareButtonLocationY)
                    state=1
                except:
                    print("didnt find the nightmare button")
            case 1:
                prepareForQuestLocationX,prepareForQuestLocationY = pyautogui.locateCenterOnScreen("prepare_for_quest_button.png",confidence=0.5)
                try:
                    pyautogui.click(x=prepareForQuestLocationX,y=prepareForQuestLocationY)
                    state=2
                except:
                    print("didnt find the prepare for quest button")
            case 2:
                try:
                    startQuestButtonLocationX,startQuestButtonLocationY = pyautogui.locateCenterOnScreen("start_quest_button.png",confidence=0.5)
                    pyautogui.click(x=startQuestButtonLocationX,y=startQuestButtonLocationY)
                    state=3
                except:
                    print("didnt find the start for quest button")
            case 3:
                try:
                    pyautogui.locateCenterOnScreen("boss_battle.png",confidence=0.5)
                    time.sleep(3.5)
                    try:
                        ultimateLocationX,ultimateLocationY = pyautogui.locateCenterOnScreen("ultimate_button.png",confidence=0.5)
                        pyautogui.click(x=ultimateLocationX,y=ultimateLocationY,clicks=2,interval=0.5)
                    except:
                        print("didnt find the ultimate button")
                    state=4
                except:
                    print("still no boss")
            case 4:
                try:
                    tapScreenLocationX,tapScreenLocationY = pyautogui.locateCenterOnScreen("TAP_SCREEN.png",confidence=0.5)
                    pyautogui.click(x=tapScreenLocationX,y=tapScreenLocationY,clicks=2,interval=1)
                    print("taped once")
                    tapScreenLocationX,tapScreenLocationY = pyautogui.locateCenterOnScreen("TAP_SCREEN.png",confidence=0.5)
                    pyautogui.click(x=tapScreenLocationX,y=tapScreenLocationY)
                    state=5
                except:
                    print("didnt find the TAP SCREEN button")

            case 5:
                try:
                    closeLocationX,closeLocationY = pyautogui.locateCenterOnScreen("close_button.png",confidence=0.5)
                    pyautogui.click(x=closeLocationX,y=closeLocationY)
                    print("clicked CLOSE once")
                    try:
                        closeLocationX,closeLocationY = pyautogui.locateCenterOnScreen("close_button.png",confidence=0.5)
                        pyautogui.click(x=closeLocationX,y=closeLocationY)
                    except:
                        print("no second Lottery rewards")
                    state=6
                except:
                    print("didnt find the close button")

            case 6:
                try:
                    eventsLocationX,eventsLocationY = pyautogui.locateCenterOnScreen("events_button.png",confidence=0.5)
                    pyautogui.click(x=eventsLocationX,y=eventsLocationY)
                    state=-1
                except:
                    print("didnt find the events button")
    print("the single run finished successfully")

def multiple_runs():
    noTicketsLeft= False
    numberTickets =get_tickets()
    while(noTicketsLeft != True):
        if (numberTickets>=10):
            single_run_point_event()
            time.sleep(3)
            numberTickets =get_tickets()
        else:
            try:
                #checks if there are no ticket gifts
                pyautogui.locateCenterOnScreen("no_tickets.png",minSearchTime=3,confidence=0.5)
                print("no more tickets")

                #clicks the close button
                pyautogui.click(x=965,y=975)

                noTicketsLeft=True

            except:
                #clicks the menu button
                pyautogui.click(x=1875,y=60)

                #clicks the gift-box button
                pyautogui.click(x=1825,y=350)

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
#single_run_point_event()
multiple_runs()
