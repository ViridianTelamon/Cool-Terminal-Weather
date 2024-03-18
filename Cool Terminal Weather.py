import requests
import time
import sys
import os

print("""
 _____             _   _____                   _             _   _    _            _   _               
/  __ \           | | |_   _|                 (_)           | | | |  | |          | | | |              
| /  \/ ___   ___ | |   | | ___ _ __ _ __ ___  _ _ __   __ _| | | |  | | ___  __ _| |_| |__   ___ _ __ 
| |    / _ \ / _ \| |   | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | | | |/\| |/ _ \/ _` | __| '_ \ / _ \ '__|
| \__/\ (_) | (_) | |   | |  __/ |  | | | | | | | | | | (_| | | \  /\  /  __/ (_| | |_| | | |  __/ |   
 \____/\___/ \___/|_|   \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|_|  \/  \/ \___|\__,_|\__|_| |_|\___|_|   """)

print("\nBy:  ViridianTelamon.")

website = "https://wttr.in/"

weather = f"{website}"

while True:
    menu = input("\nEnter W For Weather And Enter C To Choose The Weather Location And Enter E To Exit This Program:  ")

    menu = menu.lower()

    if menu == "w":
        try:
            information = requests.get(weather)
            information = information.text
        except:
            information = "Error."

        information = f"\n{information}"

        #information = information[information.rfind("\n")]

        print("\n".join(information.split("\n")[:-2]))
    elif menu == "c":
        weather_location = input("\nEnter In The Weather Location That You Want To See The Weather Of For This Program:  ")

        #weather_location = weather_location.lower()

        try:
            information = requests.get(f"{weather}{weather_location}")
            information = information.text
        except:
            information = "Error."

        information = f"\n{information}"

        print("\n".join(information.split("\n")[:-2]))
    elif menu == "e":
        break
    else:
        continue