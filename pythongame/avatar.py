from textwrap import dedent
from os import system, name
import subprocess as sp
import time


class Scene(object):

    some_dict = {
        'key': ["a", "b"],
        'key3': 'askjflskdj'
    }

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


class Puzzle(object):

    def first_puz(self):
        # first puzzle is a simple riddle that the user must guess.
        answer = "confidence"

        print("Here is a riddle...")
        print("Journey without it and you will never prevail, but if you have too much of it you will surely fail.\n")

        while True:
            user_answer = input().lower()
            if user_answer == answer:
                print("That's right!")
                break
                # have the game continue
            else:
                print("Try again.\n")

    def second_puz(self):
        # second puzzle will be a memorization game.
        print("There are several floating orbs surrounding you, you're not quite sure what to do...After a couple moments of scanning the room you notice that one of the orbs is a different color than the others. You levitated a rock to break the different-colored orb.")
        print()
        print("The orb shatters to pieces revealing a scroll with a some sort of sequence. As you try to read the scroll, it suddenly catches on fire. You have to quickly memorize the sequence, are you ready?")
        input(dedent("""
        Using the keys 'WASD' repeat the sequence that is on the scroll.\n
        \t\t-------------------------------------\n
        \t\t\t\t W = Up\n
        \t\tA = Left\tS = Down\tD = Right\n
        \t\t-------------------------------------
        Press 'RETURN' when you are ready.
        """))

        answer = "wssadwad"
        seconds = 5
        attempts = 3

        def clear():
            if name == "nt":
                _ = system('cls')
            else:
                _ = system('clear')

        print(
            f"[ UP, DOWN, DOWN, LEFT, RIGHT, UP, RIGHT, LEFT ]\n\nYou have {seconds} seconds to memorize this sequence.")

        while True:
            time.sleep(seconds)
            clear()

            while attempts > 0:
                user_attempt = input(
                    "Type out the sequence here using 'WASD'\n")
                if user_attempt == answer:
                    print("You got it!")
                    break
                else:
                    print("Try again.\n")
                    attempts -= 1

                    if attempts == 0:
                        seconds += 2
                        attempts = 3
                        print("This is your last chance to see the scroll.")
                        print(
                            f"[ UP, DOWN, DOWN, LEFT, RIGHT, UP, RIGHT, LEFT ]\n\nYou have {seconds} seconds to memorize this sequence.")
                        time.sleep(seconds)
                        clear()
            break

    def third_puz(self):
        # guessing game
        print(dedent("""
        There are five pillars before you, you're not sure what to do...After a couple of moments of scanning around you notice some writing on a stone tablet:
        \t\tYou must light the pillars in the correct order to unlock the treasure you seek.
        """))
        input(dedent("""
        You have to light the pillars in a particular order, if you do not, the pillars will dim and reset.

        Press 'RETURN' when you're ready.
        """))

        pillars = [1, 2, 3, 4, 5]
        answer = [3, 5, 1, 4, 2]
        i = 0

        pillars_img = "- - - - -"
        imglist = pillars_img.split()

        print(f"Which pillar do you want to light?\n{pillars}\n")

        while True:
            i += 1
            attempt = input()
            attempt = int(attempt)

            if attempt == answer[i - 1]:
                pillars.remove(attempt)
                imglist[attempt - 1] = "*"
                final = " ".join(imglist)

                if i == 5:
                    # they answer correctly and got it all right.
                    imglist[attempt - 1] = "*"
                    final = " ".join(imglist)
                    print(f"\n[ {final} ]")
                    print("You got it.\n")
                    break

                print("-" * 20)
                print(
                    f"\nThe pillar lights.\n\n[ {final} ]\n\nWhich pillar do you want to light?\n{pillars}\n")

            else:
                i = 0
                pillars = [1, 2, 3, 4, 5]
                imglist = pillars_img.split()
                final = " ".join(imglist)
                print("-" * 20)
                print(
                    f"\nThe pillars all dim.\n\n[ {final} ]\n\nWhich pillar do you want to light?\n{pillars}")

    def fourth_puz(self):
        print(dedent("""
        You are trapped in a maze...the only way out is to wield the correct element in each room. You will be ambushed by a surprise attack, wield the correct element to proceed to the next room.
        """))
        input(dedent("""
        Choose an element between fire, water or earth. If you're lucky the correct element will get you out of a sticky situation.

        Press 'RETURN' when you're ready.
        """))


class TitleScreen(Scene):

    def enter(self):
        print("welcome to the game.")
        puzzles.first_puz()
        # print(f"{a_map["list1"][0]}")
        # return Map.scenes["key"][0]
        return 'water training'


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
        'key': ['final scene', 'boss battle'],
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


# class Puzzles(object):

#     def first_puz


a_map = Map("title screen")
a_game = Engine(a_map)
puzzles = Puzzle()
a_game.play()
