# Python-game
Matching pairs memory game in python using the pygame library

Game rules - In this game the user will be presented with a list of tiles containing pair of images which will be hidden behind the tile. Whenever the user clicks a tile its underlying image will be shown. The user will be able to flip or view only two consecutive tiles at a time. The task of the user is to match all the tiles as soon as possible.

app_logic.py
   This python program contains the logic for creating a window of 512 X 512 size, displaying the tiles, mapping two consecutive tiles if they are same and flipping of tiles.
   
game_configuration.py
   This python program is the config file of the game where attributes like screen size, image size, total no of tiles and list of assets are maintained.

animal_class.py
   This python program contains the Animal class which shuffles the tiles each time a game is started and contains attributes like row and column to uniquely identify each tile in    the game. It also contains the status flag which denotes whether a tile is matched or not.
   
video demo link: https://youtu.be/doxDp7Pf4zA
