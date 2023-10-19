# GoogleMapsBot

Browser bot that gets into Google Maps and searches for all the coordinates on a given txt file, taking a screenshot of the location.

## About the project

This bot was created to help a friend on his thesis project, he needed to take screenshots of several locations of which he had the coordinates. Therefore, a script was created, on which a Chrome browser is opened on the Google Maps page, then the view is switched to satellital. After that, the bot automatically starts reading a txt file full of coordiates (or places to look for) and searchs for them on the map. After finding one of them, the side tab is closed, the tags are erased and the map is centered. <br>
<br>
After the window is formatted into the desired way, a screenshot is taken and saved with a unique name. <br>
<br>
#### Screenshots example
##### View before erasing tags and centering the map
<img src="https://github.com/konrad-ivelic/GoogleMapsBot/assets/70595431/a494cf36-ed33-47c5-a240-1de9ec573d93" width=75% height=75%> <br>
<br>
##### View after formatting
<img src="https://github.com/konrad-ivelic/GoogleMapsBot/assets/70595431/2623c8b2-7074-4a9a-98ed-d899733d459a" width=75% height=75%> <br>
<br>

## Getting Started
### Prerequisites

- Environment running python 3.x
- Windows operatting system (Not sure if it is a required dependency, but it was tried to use it on a Mac and it did not work).

### Installation
#### Github
1. Clone or download the project
2. Install selenium (Version: 4.14.0 was used)

```
pip install selenium
```

## Structure of the code
#### googleMapsBot.py 
### Class

The Class *googleMapsBrowserBot*. This class holds the behaviour of the browser bot specifically designed to do actions on the google maps site. The initiation of the bot is done by the following code:

```
gMapsBot = googleMapsBrowserBot(browser)
```

Where the browser given as a parameter must be a webdriver browser object. Such as: Chrome(), Edge(), Firefox(), Safari(). The bot was specifically designed for Chrome, so it is advised to be used. 

### Methods

- `open(self,maximize = True)` Opens the browser on the google maps page, if maximize is True, the window will be maximized upon initiation.
- `close(self)` Closes the browser.
- `search(self,input)` Searchs for the input on the map.
- `clear_search(self)` Clears the search box.
- `toggle_satelite_view(self)` Toggles the satelite view, if it was not selected before, it is activated, if it was, the satelite view is desactivated.
- `option_on_hovered_menu(self,index)` Selects the index ubicated option on the menu that appears when the satelite view button is hovered. The options are:
  1: Show Relief ; 2: Show traffic ; 3: Show Public Transport ; 4: Show On Bike Route ; 5: More options.
- `zoom_in(self)` Zooms in on the map.
- `zoom_out(self)` Zooms out on the map.
- `toggle_side_bar(self)` Opens or closes the side bar that appears when an input is searched on the map.
- `erase_tags(self)` Erases the tags on the map. It only works if the satelite view option is selected before.
- `center_map(self)` Centers the map by dragging it towards the left.
- `take_screenshot(self,image_name)` Takes screenshot of the map and saves it with the image_name given as parameter.

#### searchCoordinates.py

### About the script

This script reads all the coordinates on a given file and iterates over them. For each of them, the bot searches it on the map, erases the tags from the view, centers the map and takes a screenshot. The text file where the coordinates are stored, must follow the only rule that each line must represent one and only place, if two or more are stored, the search will be unsuccesful. Instead of coordinates, the file can store names of places and the script will still work.

### Instructions to run the script

To run the script, the following instruction must be called:

```
python3 searchCoordinates.py coordinates.txt
```

Where coordinates.txt must store the coordinates that want to be search and taken screenshot of.
