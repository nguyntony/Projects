class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('final scene')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class TitleScreen(Scene):

    def enter(self):
        print("welcome to the game.")
        print(f"{a_map["list1"][0]}")
        return 'list'[0]


class WaterTraining(Scene):

    def enter(self):
        print("you have arrived to the northern water tribe")

        action = input("should we train? ")

        if action == "yes":
            return 'boss battle'


class FinalScene(Scene):

    def enter(self):
        print("the end")
        return 'final scene'


class BossBattle(Scene):

    def enter(self):
        print("prepare for the final battle")
        return 'final scene'


class Map(object):

    scenes = {
        'title screen': TitleScreen(),
        'water training': WaterTraining(),
        'list1': ['final scene', 'boss battle'],
        'final scene': FinalScene(),
        'boss battle': BossBattle()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("title screen")
a_game = Engine(a_map)
a_game.play()
