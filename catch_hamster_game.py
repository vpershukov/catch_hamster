from random import randint

class Player:
    position = [0, 0]

class Hamster:
    position = [0, 0]
    health = 1
    def __init__(self, hamster_id, map):
        self.hamster_id = hamster_id
        self.health = 1
        self.position = self.get_empty_position(map)

    def get_empty_position(self, map):
        map_height = len(map.split("\n"))
        map_width = len(map.split("\n")[0])
        while True:
            coordinates = [randint(0, map_width - 1), randint(0, map_height - 1)]
            if map.split("\n")[coordinates[1]][coordinates[0]] == "*":
                return coordinates

    def hamster_catched(self):
        self.health -= 1
        print("Hamster number {hamster_id} catched.".format(hamster_id=self.hamster_id))

class Game:
    hamsters_count = 4
    map = """*****\n*****\n*****"""
    gameon = True
    num_of_lines = len(map.split("\n"))
    len_of_line = len(map.split("\n")[0])
    def __init__(self):
        self.player = Player()
        self.hamsters = []
        for i in range(self.hamsters_count):
            self.hamsters.append(Hamster(hamster_id=i+1, map=self.get_map_with_all_hamsters(True)))

    def add_point(self, position, name, map):
        map_in_list = map.split("\n")
        row = map_in_list[position[1]]
        row = row[:position[0]] + name + row[position[0]+1:]
        map_in_list[position[1]] = row
        return "\n".join(map_in_list)

    def render_map(self):
        map = self.map
        map = self.add_point(position=self.player.position, name="x", map=map)
        for hamster in self.hamsters:
            if hamster.health > 0:
                map = self.add_point(position=hamster.position, name=str(hamster.hamster_id), map=map)
        print(map)

    def move_player(self, direction):
        """direction = w, a, s, d"""
        if direction == "s":               # down
            if self.player.position[1] == self.num_of_lines - 1:
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

    def get_map_with_all_hamsters(self, start_game=False):
        map = self.map
        for hamster in self.hamsters:
            map = self.add_point(position=hamster.position, name=str(hamster.hamster_id), map=map)
        if start_game:
            map = self.add_point(position=self.player.position, name="x", map=map)
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
        while self.gameon:
            command = input("Type your command: ")
            if command not in ["s", "w", "a", "d"]:
                print("Wrong command.")
            else:
                self.move_player(command)
                self.render_map()
            if len([hamster for hamster in self.hamsters if hamster.health > 0]) == 0:
                print("Wow, you won! So success, many congratulations.")
                self.gameon = False

game = Game()
game.start()
