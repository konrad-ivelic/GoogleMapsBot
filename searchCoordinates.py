from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from googleMapsBot import googleMapsBrowserBot

import time
import sys

#Recover coordinates file from command window
coordinates_file = sys.argv[1]

#Initialize browser
browser = webdriver.Chrome()

#Initializes browser bot
gMapsBot = googleMapsBrowserBot(browser)
gMapsBot.open()
time.sleep(2)

#Change to satellite view
gMapsBot.toggle_satelite_view()
time.sleep(2)

#Go over all the coordinates in the file and take a screenshot for each of them
counter = 1
with open(coordinates_file,"r") as file:
    #For each coordinate in the file
    for line in file.readlines():

        #Search coordinates
        coordinates = line[:-1]
        gMapsBot.search(coordinates)
        time.sleep(2)

        #Zoom in thrice
        for i in range(0,3):
            gMapsBot.zoom_in()
            time.sleep(1)

        #Close side bar tab
        gMapsBot.toggle_side_bar()
        time.sleep(1)

        #Erase tags from map
        gMapsBot.erase_tags()
        time.sleep(1)

        #Center the image by dragging the map
        gMapsBot.center_map()

        #Take and save screenshot
        gMapsBot.take_screenshot(f"image{counter}.png")

        #Open side bar again to do a new search
        gMapsBot.toggle_side_bar()
        time.sleep(1)

        #Clear text box and add 1 to the counter
        gMapsBot.clear_search()
        counter += 1

#Close the browser
gMapsBot.close()