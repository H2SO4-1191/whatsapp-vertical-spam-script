import pywhatkit as pwk
import time
import random

def main():
    phone_number = "" #Add the phone number here
    messages = [
        "Hello",
        "World",

        #Add different messages here
    ]
    msg_index = 0
    for i in range(1000): #Edit the range as you wish
        try:
            if msg_index > 4: msg_index = 0
            message = messages[msg_index]
            pwk.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)
            print(i)
            msg_index += 1
        except Exception as e:
            print("Failed to send: " + str(e))
    input("Press Enter to exit.")

if __name__ == "__main__":
    main()
