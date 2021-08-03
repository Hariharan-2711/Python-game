import os
import random
import game_configuration as gc

from pygame import image, transform

animals_count = dict((a, 0) for a in gc.ASSET_FILES)

def available_animals():
    return [a for a, c in animals_count.items() if c<2]

class Animal:
    def __init__(self, index):
         #index value ranges from 0 to 15. Based on index value we can place animals on game board
         #index 0-3 will refer to the tiles in the first row, index 4-7 will refer to the tiles in 2nd row
         #similarly, index 8-11, 12-15 will refer to 3rd and 4th row resp. Hence totally we have 16.
         
         self.index = index
         self.row = index // gc.NUM_TILES_SIDE
         self.col = index % gc.NUM_TILES_SIDE
         self.name = random.choice(available_animals())
         animals_count[self.name] += 1 #update the count status of the particular animal which was chosen random
         
         self.image_path = os.path.join(gc.ASSET_DIR, self.name)
         self.image = image.load(self.image_path) #loading the image
         self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2*gc.MARGIN, gc.IMAGE_SIZE - 2*gc.MARGIN)) #transform the image into 128*128 size and also reduce 2*4 from 128*128 for margin
         #print(self.image)
         self.box = self.image.copy()
         self.box.fill((200, 200, 200)) #200, 200, 200 refers to the RGB value of fill color in the box
         self.skip = False #flag set to False initially. This flag is used to skip animals which are matched previously. If it is True then it means that the animal is matched.
         