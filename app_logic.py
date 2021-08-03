import pygame
import game_configuration as gc

from animal_class import Animal
from pygame import display, event, image
from time import sleep

def find_index(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return index

pygame.init()

display.set_caption('Matching Pairs')

screen = display.set_mode((512, 512))

matched = image.load('other_assets/matched.png') #returns a surface
#screen.blit(matched, (0, 0)) 
# (0, 0) is the co-ordinate at the top left corner. i.e starting of the screen
#since the 'matched' image is 512X512 in size it will fill the entire screen by starting from (0, 0).
#So no need to provide the ending co-ordinates of the matched image in the screen.
#display.flip() #updates the display so that the image can be viewed

running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)] #initializing all the animal tiles with index by calling the animal class. The tiles list contains all the 16 objects of the animal class
#print(tiles)

current_images = []

#blit method displays a surface on another surface

while running:
    current_events = event.get()
    #print(current_events)
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #print(mouse_x, mouse_y)
            index = find_index(mouse_x, mouse_y)
            #print(index)
            
            #if index in current_images:
            #    screen.blit(tiles[index].box, (tiles[index].row*(gc.IMAGE_SIZE+gc.MARGIN), tiles[index].col*(gc.IMAGE_SIZE+gc.MARGIN)))
            #else:
            if index in current_images: #logic for fading the tile if selected already
                current_images.remove(index)
            else:
                current_images.append(index)
            #if index not in current_images: 
                #The above if else and this if does the same. The purpose of this is to avoid matching the same tile or the tile with the same index consecutively
                #current_images.append(index)
            #current_images.append(index)
            if(len(current_images) > 2):
                current_images = current_images[1:] #ignore or fade the first tile(image) which was clicked
            #for index_i in current_images:
            #    tiles[index_i].open = True
    
    screen.fill((255, 255, 255))
    
    total_skipped = 0 #variable to keep count of matched tiles
    
    #displaying the tiles without margin space between tiles
    #for tile in tiles: #updates the screen with all the 16 images of tiles on the screen
    #    screen.blit(tile.image, (tile.col*gc.IMAGE_SIZE, tile.row*gc.IMAGE_SIZE+gc.MARGIN))
    
    for i, tile in enumerate(tiles): #updates the screen with all the 16 images of tiles on the screen
        image_i = tile.image if tile.index in current_images else tile.box
        #image_i = tile.image if tile.open==True else tile.box
        
        #image_i = tile.image if i in current_images else tile.box (both above and this statement are same)
        #screen.blit(tile.image, (tile.col*(gc.IMAGE_SIZE+gc.MARGIN), tile.row*(gc.IMAGE_SIZE+gc.MARGIN))) This displays all the tile images regardless whether clicked or not
        #screen.blit(image_i, (tile.col*(gc.IMAGE_SIZE+gc.MARGIN), tile.row*(gc.IMAGE_SIZE+gc.MARGIN)))#This displays the tile images even if it is matched already
        
        if not tile.skip: #if(tile.skip==False)
            #screen.blit(image_i, (tile.row*(gc.IMAGE_SIZE+gc.MARGIN), tile.col*(gc.IMAGE_SIZE+gc.MARGIN)))#Providing the parameters as row, col in the blit() function will provide inappropriate results
            screen.blit(image_i, (tile.col*(gc.IMAGE_SIZE+gc.MARGIN), tile.row*(gc.IMAGE_SIZE+gc.MARGIN)))
        else:
            total_skipped += 1
    
    display.flip()
        
    #Logic for matching
    if len(current_images) == 2:
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.4)
            screen.blit(matched, (0, 0))
            display.flip()
            sleep(0.4)
            current_images = [] #Not necessary
            
    if total_skipped == len(tiles):
        running = False

print('Good Bye!')