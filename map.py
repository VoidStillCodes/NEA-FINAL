import random

#-- Map class --#
class Map:
    def __init__(self):
        self.map = []
        self.width = 1400//32
        self.height = 800//32
        self.generate_map()
    
    def display_map(self):
        for row in self.map:
            print("".join(str(cell) for cell in row))
        
    def generate_map(self):
        self.walls()
        self.dungeon_tiles()
    
    def walls(self):
        #adds walls to the map
        for y in range(self.height):
            row = []
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    row.append(1)  # Wall
                else:
                    row.append(0)  # Empty space
            self.map.append(row)
    
    def dungeon_tiles(self):
        #adds a single dungeon tile to the map
        empty_positions = []
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                if self.map[y][x] == 0:
                    empty_positions.append((x, y))
        if not empty_positions:
            return
        x, y = random.choice(empty_positions)
        self.map[y][x] = 2

#testing 
if __name__ == "__main__":
    game_map = Map()
    game_map.display_map()

        