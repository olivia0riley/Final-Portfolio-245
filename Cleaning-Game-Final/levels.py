import pygame
from spritesheet_functions import SpriteSheet
from vector import Vector
from vector import Vector
from roomba_rework_2 import Roomba
from room import Room
from mess import Mess


class Levels:
    
    def __init__(self, width, height, icl, icr):

        # Index of current level
        self.icl = icl
        # Index of current room
        self.icr = icr

        self.levels = []

        
        ## Level_0
        self.level_0 = []


        # Make rooms
        room0a = Room (width, height)

        #Place Roombas

        #Place messes
        room0a.messes.append(Mess(507, 400, room0a))

        # Append room0a to level_0 list
        self.level_0.append(room0a)

        # Append level_0 to levels list
        self.levels.append(self.level_0)
        
        


        ## Level 1
        self.level_1 = []


        # Room1a
        room1a = Room (width, height)

        #Place Roombas
        room1a.roombas.append(Roomba(200,300,1))
        room1a.roombas.append(Roomba(500,200,1))

        #Place messes
        room1a.messes.append(Mess(500,300,room1a))
        room1a.messes.append(Mess(300, 220, room1a))

        # Append room1a to level_1 list
        self.level_1.append(room1a)

        # Append level_1 to levels list
        self.levels.append(self.level_1)




        ## Level_2
        self.level_2 = []


        # Room2a
        room2a = Room (width, height)

        #Place Roombas
        room2a.roombas.append(Roomba(240, 520, 2))

        #Place messes
        room2a.messes.append(Mess(600, 320, room2a))

        # Append room2a to level_2 list
        self.level_2.append(room2a)  

        # Append level_2 to levels list
        self.levels.append(self.level_2)




        ## Level_3
        self.level_3 = []


        # Make rooms
        room3a = Room (width, height)

        #Place Roombas
        room3a.roombas.append(Roomba(128, 400, 3))
        room3a.roombas.append(Roomba(885, 400, 4))

        #Place messes
        room3a.messes.append(Mess(173, 168, room3a))
        room3a.messes.append(Mess(841, 581, room3a))

        # Append room3a to level_3 list
        self.level_3.append(room3a)


        # Append level_3 to levels list
        self.levels.append(self.level_3)




        ## Level_4
        self.level_4 = []

        # Make Rooms
        room4a = Room (width,height)

        # Place Roombas 
        room4a.roombas.append(Roomba(400, 530, 5))
        room4a.roombas.append(Roomba(700, 100, 1))
        room4a.roombas.append(Roomba(300, 545, 2))

        # Place Messes
        room4a.messes.append(Mess(235, 400, room4a))
        room4a.messes.append(Mess(450, 500, room4a))

        # Append room4a to level_4 list
        self.level_4.append(room4a)

        # Append Level_4 to levels list
        self.levels.append(self.level_4)
        
        


        ## Level_5
        self.level_5 = []

        # Make rooms
        room5a = Room(width,height)

        # Place Roombas 
        room5a.roombas.append(Roomba(857, 400, 1))
        room5a.roombas.append(Roomba(430, 202, 2))
        room5a.roombas.append(Roomba(631, 640, 3))

        # Place Messes
        room5a.messes.append (Mess(570, 390, room5a))
        room5a.messes.append (Mess(530, 200, room5a))
        room5a.messes.append (Mess(670, 378, room5a))

        # Append room 5a to level_5 list
        self.level_5.append(room5a)

        # Append Level_5 to levels list
        self.levels.append(self.level_5)




        ## Level_6
        self.level_6 = []

        # Make rooms
        room6a = Room(width,height)

        # Place Roombas 
        room6a.roombas.append(Roomba(127, 500, 1))
        room6a.roombas.append(Roomba(400, 602, 2))
        room6a.roombas.append(Roomba(201, 540, 4))

        # Place Messes
        room6a.messes.append (Mess(100, 350, room6a))
        room6a.messes.append (Mess(200, 200, room6a))
        room6a.messes.append (Mess(400, 278, room6a))

        # Append room 6a to level_6 list
        self.level_6.append(room6a)

        # Append Level_6 to levels list
        self.levels.append(self.level_6)




        ## Level_7
        level = []

        # Make rooms
        room = Room (width, height)

        #Place Roombas
        room.roombas.append(Roomba(500, 625, 1))
        room.roombas.append(Roomba(128, 625, 5))
        room.roombas.append(Roomba(500, 625, 1))
        room.roombas.append(Roomba(855, 625, 1))
        room.roombas.append(Roomba(855, 425, 1))
        room.roombas.append(Roomba(855, 225, 2))
        room.roombas.append(Roomba(855, 125, 5))

        #Place messes
        room.messes.append(Mess(841, 120, room))
        room.messes.append(Mess(841, 581, room))
        #room.messes.append(Mess(150, 120, room))
        room.messes.append(Mess(150, 581, room))

        # Append room to level_7 list
        level.append(room)

        # Append level_7 to levels list
        self.levels.append(level)
        



        ## Level_8
        level = []

        # Make rooms
        room = Room (width, height)

        #Place Roombas
        room.roombas.append(Roomba(128, 123, 2))
        room.roombas.append(Roomba(350, 123, 5))
        room.roombas.append(Roomba(500, 123, 5))
        room.roombas.append(Roomba(640, 123, 5))
        room.roombas.append(Roomba(350, 265, 5))
        room.roombas.append(Roomba(500, 265, 5))
        room.roombas.append(Roomba(640, 265, 5))
        room.roombas.append(Roomba(128, 425, 5))
        room.roombas.append(Roomba(128, 265, 5))

        #Place messes
        room.messes.append(Mess(150, 120, room))


        # Append room to level_8 list
        level.append(room)

        # Append level_8 to levels list
        self.levels.append(level)




        ## Level_9
        level = []

        # Make rooms
        room = Room (width, height)

        #Place Roombas
        room.roombas.append(Roomba(507, 375, 1))

        #Place messes
        room.messes.append(Mess(507, 375, room))


        # Append room to level_8 list
        level.append(room)

        # Append level_8 to levels list
        self.levels.append(level)

        ## Level_10
        level = []

        # Make rooms
        room = Room (width, height)

        #Place Roombas
        room.roombas.append(Roomba(500, 625, 1))
        room.roombas.append(Roomba(128, 625, 5))
        room.roombas.append(Roomba(500, 625, 3))
        room.roombas.append(Roomba(855, 625, 4))
        room.roombas.append(Roomba(855, 425, 4))
        room.roombas.append(Roomba(855, 225, 2))
        room.roombas.append(Roomba(855, 125, 5))
        room.roombas.append(Roomba(500, 265, 5))
        room.roombas.append(Roomba(640, 265, 3))
        room.roombas.append(Roomba(128, 425, 4))
        room.roombas.append(Roomba(128, 265, 5))

        #Place messes
        room.messes.append(Mess(841, 120, room))
        room.messes.append(Mess(841, 581, room))
        room.messes.append(Mess(150, 120, room))
        room.messes.append(Mess(150, 581, room))

        # Append room to level_7 list
        level.append(room)

        # Append level_7 to levels list
        self.levels.append(level)


        # level blueprint
        """
        ## Level_X
        self.level = []


        # Make room
        room = Room (width, height)

        #Place Roombas
        roomXa.roombas.append(Roomba(128 to 885, 123 to 625, type))

        #Place messes
        roomXa.messes.append(Mess(173 to 841, 168 to 581, room))

        # Append room to level_X list
        self.level.append(room)

        # Append level_X to levels list
        self.levels.append(level)




        """


