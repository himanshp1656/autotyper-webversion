from django.shortcuts import render
import pyautogui
import time
import random
import json
import keyboard
import threading

# # Flag to stop the typing
# stop_typing = False

def mimicHumanTyping(data, base_speed=0.2, variance=0.05):
    # global stop_typing
    for char in data:
        # if stop_typing:
        #     print("Typing stopped.")
        #     break
        
        
        # Random delay to vary typing speed
        delay = base_speed + random.uniform(-variance, variance)
        time.sleep(delay)
        
        # Occasionally introduce a longer pause
        if random.random() < 0.1:  # 10% chance to pause
            time.sleep(random.uniform(0.5, 1.5))
            
        # Simulate a typo and correction
        if random.random() < 0.2:  # 20% chance of typo
            typo_char = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^')
            pyautogui.typewrite(typo_char)
            time.sleep(random.uniform(0.05, 0.2))  # Wait between 0.7 to 1.12 seconds
            pyautogui.press('backspace')
            
        pyautogui.typewrite(char)
    
        # pyautogui.typewrite(char, interval=random.uniform(0.05, 0.2))  # Random interval between keystrokes

# def stop_on_esc():
#     global stop_typing
#     keyboard.wait('esc')
#     keyboard.clear_all_hotkeys()
#     stop_typing = True
#     print("Esc key pressed. Stopping...")

def home(request):
    global stop_typing
    if request.method == "POST" and request.POST.get('alldata', '[]'):
        # print(request.POST)
        data = request.POST.get('alldata', '[]')
        data_list = json.loads(data)
        print(data_list)
        for everydata in data_list:
            keyboard.add_hotkey(everydata["keyCombination"], lambda text=everydata["text"]: mimicHumanTyping(text))
        
        if len(data_list) > 0:
            stop_typing = False
            # esc_thread = threading.Thread(target=stop_on_esc)
            # esc_thread.start()
            # esc_thread.join()
            keyboard.wait('esc')
            keyboard.clear_all_hotkeys()
    else:
        data_list = []

    return render(request, 'index.html', {"data_list": data_list})
