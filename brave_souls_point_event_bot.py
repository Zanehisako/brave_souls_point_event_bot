import pyautogui
import time

pyautogui.PAUSE = 2

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

print("starting the script after 5 sec")
time.sleep(5)
print("script started !")
single_run_point_event()
