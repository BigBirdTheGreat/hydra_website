import pyautogui, time

pyautogui.FAILSAFE = True

a = "Never_Gonna_Give.txt"
b = "Shrek.txt"

number = False
spamscript = False
spamword = True

if spamscript == True:
    text = open(a, "r")
    try:

        time.sleep(6) 
        for line in text:
            pyautogui.typewrite(line)
            pyautogui.press("enter")
        text.close()
        print("closed")
    except: 
        text.close()
        print("closed")
    finally: 
        text.close()
        print("closed")

if spamword == True:
    text = "I want immunity"
    
    time.sleep(3)
    
    count = 0
    repeattimes = 500
    
    for i in range (0, repeattimes):
        count += 1
        print(count)
        
        if count == 10:
            time.sleep(5)
            pyautogui.typewrite(text)
            pyautogui.press("enter")
            time.sleep(0.3)
            count = 0
        else:
            pyautogui.typewrite(text)
            pyautogui.press("enter")
            time.sleep(0.3)

if number == True:
    time.sleep(3)
    count = 0
    
    startnum = 10
    endnum = 100
    increaseby = 2
    
    for i in range (startnum, endnum, increaseby):
        count += 1
        
        if count == 10:
            time.sleep(5)
            pyautogui.typewrite(str(i))
            pyautogui.press("enter")
            time.sleep(1)
            count = 0
        else:
            pyautogui.typewrite(str(i))
            pyautogui.press("enter")
            time.sleep(1)