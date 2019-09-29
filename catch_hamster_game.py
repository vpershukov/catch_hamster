import random
## TODO: from random import randint, choice

class Player:
    health = 100
    default_damage = 10
    position = [3, 0]

class Hamster:
    position = [0, 0]
    health = 1
    def __init__(self, hamster_id, map):
        self.hamster_id = hamster_id
        self.health = 1 # random.randint(1, 4)
        self.position = self.get_empty_position(map)

    def get_empty_position(self, map):
        map_height = len(map.split("\n"))
        map_width = len(map.split("\n")[0])
        while True:
            coordinates = [random.randint(0, map_width - 1), random.randint(0, map_height - 1)]
            if map.split("\n")[coordinates[1]][coordinates[0]] == "*":
                return coordinates

    def hamster_catched(self):
        self.health -= 1
        print("Hamster number {hamster_id} catched".format(hamster_id=self.hamster_id))

hamster_count = 4

class Game:
    map = """****\n****\n****\n****"""
    num_of_lines = len(map.split("\n"))
    len_of_line = len(map.split("\n")[0])
    def __init__(self):
        self.player = Player()
        self.hamsters = []
        for i in range(hamster_count):
            self.hamsters.append(Hamster(hamster_id=i+1, map=self.get_map_with_all_hamsters()))

    def add_point(self, position, name, map):
        map_in_list = map.split("\n")
        row = map_in_list[position[1]]
        row = row[:position[0]] + name + row[position[0]+1:]
        map_in_list[position[1]] = row
        return "\n".join(map_in_list)

    def render_map(self):
        map = self.map
        map = self.add_point(self.player.position, "x", map)
        for hamster in self.hamsters:
            if hamster.health > 0:
                map = self.add_point(position=hamster.position, name=str(hamster.hamster_id), map=map)
        print(map)

    def move_player(self, direction):
        """direction = w, a, s, d"""
        if direction == "s":               # down
            if self.player.position[1] == self.num_of_lines + 1:
                return False
            else:
                self.player.position[1] += 1
        if direction == "w":               # up
            if self.player.position[1] == 0:
                return False
            else:
                self.player.position[1] -= 1
        if direction == "a":               # left
            if self.player.position[0] == 0:
                return False
            else:
                self.player.position[0] -= 1
        if direction == "d":               # right
            if self.player.position[0] == self.len_of_line - 1:
                return False
            else:
                self.player.position[0] += 1
        self.on_move()

    def get_map_with_all_hamsters(self):
        map = self.map
        for hamster in self.hamsters:
            map = self.add_point(position=hamster.position, name=str(hamster.hamster_id), map=map)
        return map

    def get_hamster_on_position(self, coordinates):
        map = self.get_map_with_all_hamsters()
        return map.split("\n")[coordinates[1]][coordinates[0]]

    def on_move(self):
        hamster_on_field = self.get_hamster_on_position(coordinates=self.player.position)
        if not hamster_on_field == "*":
            self.hamsters[int(hamster_on_field) - 1].hamster_catched()

    def start(self):
        game.render_map()
        while True:
            command = input("Type your command: ")
            if command not in ["s", "w", "a", "d"]:
                print("Wrong command")
            else:
                self.move_player(command)
                self.render_map()

game = Game()
game.start()
