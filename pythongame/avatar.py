from textwrap import dedent
import time
from random import randint
import random
from subprocess import call
import os


class User(object):

    def __init__(self):
        self.name = "Player1"
        self.hp = 100

        self.attack = ["Basic Attack"]
        self.attack_desc = {
            'Hurricane Barrage': '[ AVATAR ] You hurl devastating wind currents towards the Fire Lord.',
            'Tidal Whip': '[ AVATAR ] You attack the Fire Lord with several water whips at all directions.',
            'Geo Smash': '[ AVATAR ] The ground near the Fire Lord shakes, as small boulders hit him from the impact.',
            'Electro Shock': '[ AVATAR ] You strike a powerful jolt of electricity at the Fire Lord.'
        }
        self.defend = ["Block"]
        self.defend_desc = {
            'Leaping Whirlwind': '[ AVATAR ] You launch yourself into the air, attempting to dodge the Fire Lord\'s attack.',
            'Scorching Vortex': '[ AVATAR ] You blast a scorching fire from your palms, attempting to absorb the Fire Lord\'s attack.',
            'Terraform': '[ AVATAR ] You shift the land around the Fire Lord, causing him to not land a direct hit.',
            'Cryo Shield': '[ AVATAR ] You shield yourself with a thick armor of ice, minimizing the damage from the Fire Lord\'s attack.'
        }
        self.airskills = ["Hurricane Barrage", "Leaping Whirlwind"]
        self.waterskills = ["Tidal Whip", "Cryo Shield"]
        self.earthskills = ["Geo Smash", "Terraform"]
        self.fireskills = ["Electro Shock", "Scorching Vortex"]

    def show_offensive(self):
        for i, skill in enumerate(player.attack):
            print(f"{i+1}. {skill}")

    def show_defensive(self):
        for i, skill in enumerate(player.defend):
            print(f"{i+1}. {skill}")

    def player_attacks(self):
        if len(player.attack) == 1:
            print("[ AVATAR ] You dealt 10 damage.")
            damage = 10
            enemy.hp -= damage

        elif len(player.attack) != 1:
            print("- Abilities -\n")
            player.show_offensive()

            print("\nPlease select an ability.")
            while True:
                try:
                    ability = int(
                        input("\n> "))
                    if ability > 1:
                        while ability > 1:
                            skilldesc = player.attack[ability - 1]
                            print(player.attack_desc[skilldesc])
                            break
                        luck = randint(1, 10)
                        if luck <= 6:
                            print("You dealt 15 damage.")
                            damage = 15
                            enemy.hp -= damage
                        elif luck > 6:
                            print("You landed a critical hit. You dealt 30 damage.")
                            damage = 30
                            enemy.hp -= damage
                    elif ability == 1:
                        print("[ AVATAR ] You dealt 10 damage.")
                        damage = 10
                        enemy.hp -= damage
                    break
                except ValueError:
                    print("Please select an ability number.")
                except IndexError:
                    print("Please select an ability number.")

    def skill_selection(self, skill_list):

        while True:
            try:
                choice = int(input("> "))

                if choice == 1:
                    player.attack.append(skill_list[0])
                    choice = skill_list[0]
                    break
                elif choice == 2:
                    player.defend.append(skill_list[1])
                    choice = skill_list[1]
                    break
                else:
                    print("Please select the number 1 or 2.")

            except ValueError:
                print("Please select the number 1 or 2.")

        print(f"You have successfully learned {choice}.")


class Enemy(object):

    def __init__(self):
        self.name = "Fire Lord Ozai"
        self.hp = 100
        self.skills = [
            "He quickly takes a deep breath then exhales a giant fireball at you.",
            "He harnesses power from within then shoots lightning at you.",
            "He jumps into the air and unleashes an onslaught of quick fire bullets.",
            "He hurls a series of lightning bullets at you.",
            "He throws out a barrage of flamethrowers from his fists.",
            "He entraps you inside of a scorching flame vortex.",
            "He lashes you with blazing fire whips.",
            "He launches a series of fiery missles."
        ]

    def enemy_attacks(self):
        random_num = randint(0, len(enemy.skills) - 1)
        hit = 15

        print(f"\n[ FIRE LORD OZAI ] {enemy.skills[random_num]}")
        print(f"You took {hit} damage.\n")

        player.hp -= hit

    def player_blocked(self):
        random_num = randint(0, len(enemy.skills) - 1)
        hit = 20
        if len(player.defend) == 1:
            print(
                f"\n[ FIRE LORD OZAI ] {enemy.skills[random_num]}\n")
            print(
                "[ AVATAR ] You attempt to shield yourself from the incoming attack.")
            block = 5
            hit -= block

            print(f"You took {hit} damage.")
            player.hp -= hit

        elif len(player.defend) != 1:
            print("- Abilities -\n")
            player.show_defensive()

            print("\nPlease select an ability.")
            while True:
                try:
                    ability = int(input("\n> "))
                    if ability > 1:
                        block = 15
                        hit -= block
                        print(
                            f"\n[ FIRE LORD OZAI ] {enemy.skills[random_num]}\n")
                        while ability > 1:
                            skilldesc = player.defend[ability - 1]
                            print(player.defend_desc[skilldesc])
                            break
                        print(f"You took {hit} damage.")
                        player.hp -= hit
                    elif ability == 1:
                        print(
                            f"\n[ FIRE LORD OZAI ] {enemy.skills[random_num]}\n")
                        print(
                            "[ AVATAR ] You attempt to shield yourself from the incoming attack.")
                        block = 5
                        hit -= block
                        print(f"You took {hit} damage.")
                        player.hp -= hit
                    break
                except ValueError:
                    print("Please select an ability number.")
                except IndexError:
                    print("Please select an ability number.")


class Scene(object):

    def clear(self):
        call('clear' if os.name == 'posix' else 'cls')

    def enter(self):
        print("This scene is not yet configured.")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('boss battle')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Puzzle(object):

    def first_puz(self):

        riddles = {
            'confidence': "Journey without it and you will never prevail, but if you have too much of it you will surely fail.\n",
            'your name': "It belongs to you, but other people use it more than you do.\n",
            'piano': "What has many keys but can't open a single lock?\n",
            'footsteps': "The more you take, the more you leave behind. What am I?\n",
            'tomorrow': "What is always coming but never arrives?\n"
        }

        riddles_key = ["confidence", "your name",
                       "piano", "footsteps", "tomorrow"]
        random_num = randint(0, len(riddles_key) - 1)
        answer = riddles_key[random_num]
        chosen_riddle = riddles[answer]

        print(chosen_riddle)

        attempts = 0
        while True:
            user_answer = input("Answer:\n> ").lower()

            if user_answer == answer:
                print("That's right!")
                break
                # have the game continue
            elif attempts >= 1:
                print("Maybe try googling the answer...\n")
            else:
                print("Try again.\n")
                attempts += 1

    def second_puz(self):
        # second puzzle will be a memorization game.
        print(dedent("""Using the keys 'WASD' repeat the sequence that is on the scroll.\n
        \t\t-------------------------------------\n
        \t\t\t\t W = Up\n
        \t\tA = Left\tS = Down\tD = Right\n
        \t\t-------------------------------------"""))
        input("\nPress 'RETURN' when you are ready.")

        answer = []
        sequence = ["up", "down", "left", "right",
                    "up", "down", "right"]
        random.shuffle(sequence)

        for i in sequence:
            if i == "up":
                answer.append("w")
            elif i == "down":
                answer.append("s")
            elif i == "left":
                answer.append("a")
            else:
                answer.append("d")

        sequence = ", ".join(sequence)
        answer = "".join(answer)

        seconds = 5
        attempts = 2

        print(
            f"\n{[sequence.upper()]}\n\nYou have {seconds} seconds to memorize this sequence.")

        while True:
            time.sleep(seconds)
            Scene.clear(self)

            while attempts > 0:
                user_attempt = input(
                    "Type out the sequence here using 'WASD'\n> ")
                if user_attempt == answer:
                    print("You got it!")
                    break
                else:
                    print("Try again.\n")
                    attempts -= 1

                    if attempts == 0:
                        seconds += 2
                        attempts = 2
                        print(
                            "You somehow manage to take another glimpse of the scroll.")
                        print(
                            f"{[sequence.upper()]}\n\nYou have {seconds} seconds to memorize this sequence.")
                        time.sleep(seconds)
                        Scene.clear(self)
            break

    def third_puz(self):
        # guessing game
        print("There are five pillars before you, you're not sure what to do...After a couple of moments of scanning around you notice some writing on a stone tablet:\n\nYou must light the pillars in the correct order to unlock the treasure you seek. If they are not, the pillars will reset.\n")

        input("Press 'RETURN' when you're ready.")

        pillars = [1, 2, 3, 4, 5]
        answer = [3, 5, 1, 4, 2]
        random.shuffle(answer)

        i = 0

        pillars_img = "- - - - -"
        imglist = pillars_img.split()

        print(f"Which pillar do you want to light?\n{pillars}\n")

        while True:
            i += 1
            while True:
                try:
                    attempt = input("> ")
                    attempt = int(attempt)
                    break
                except ValueError:
                    print("Please select a number.")
            Scene.clear(self)

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

                print(
                    f"The pillar lights.\n\n[ {final} ]\n\nWhich pillar do you want to light?\n{pillars}\n")

            else:
                i = 0
                pillars = [1, 2, 3, 4, 5]
                imglist = pillars_img.split()
                final = " ".join(imglist)
                print(
                    f"The pillars all dim.\n\n[ {final} ]\n\nWhich pillar do you want to light?\n{pillars}")

    def fourth_puz(self):
        print("You are trapped in a maze alone... or so you think.\n\nA powerful sprite appears, it can harness different elements, thus allowing it to change forms to unleash devatasting attacks. You notice that the sprite has a weak spot. Hit the weak spot 3 times to defeat the sprite!")
        input(dedent("""
        Choose an element between fire, water or earth. If you're lucky the correct element will give you an advantageous edge over the sprite.

        Press 'RETURN' when you're ready.
        """))

        opponent_elements = ["water", "fire", "earth"]
        opponent = opponent_elements[randint(0, 2)]
        hint_color = ""

        choice = input(
            "Choose an element (Fire, Water, or Earth):\n> ").lower()
        Scene.clear(self)
        rounds = 0
        tries = 0

        while rounds < 3:
            tries += 1
            print(f"> {choice}\n")
            if choice == "water":
                if opponent == "fire":
                    print(
                        "[Outcome] You summon a powerful water whip that greatly damages the fire sprite.")
                    rounds += 1
                    print(f"\n   ----- SUCCESS! {rounds} of 3 -----")
                elif opponent == "water":
                    print(
                        "[Outcome] You and the water sprite both attack each other with a chilling ice dagger. You both are evenly matched.")
                elif opponent == "earth":
                    print("[Outcome] You try to attack the sprite with a thrashing wave, the earth sprite blocks the attack and pummels you with a barrage of rocks.")
            elif choice == "earth":
                if opponent == "water":
                    print("[Outcome] You launch yourself into the air and smash the ground, the attack sends a shockwave across the landscape which greatly injures the water sprite.")
                    rounds += 1
                    print(f"\n   ----- SUCCESS! {rounds} of 3 -----")
                elif opponent == "earth":
                    print(
                        "[Outcome] You and the earth sprite hurl pebble bullets at one another. You both are evenly matched.")
                elif opponent == "fire":
                    print("[Outcome] You try to lunge a flurry of rocks at the fire sprite, it dodges your attack easily and burns you with a ferocious flamethrower.")
            elif choice == "fire":
                if opponent == "earth":
                    print(
                        "[Outcome] You quickly do a series of kicks which ends with a sweeping flame kick, you greatly damage the earth sprite.")
                    rounds += 1
                    print(f"\n   ----- SUCCESS! {rounds} of 3 -----")
                elif opponent == "fire":
                    print(
                        "[Outcome] You and the fire sprite both hurl a quick fireball at one another. You both are evenly matched.")
                elif opponent == "water":
                    print("[Outcome] You hurl a barrage of small fireballs at the water sprite, it blocks your attack with a powerful wave. The sprite then attacks you with a follow-up water whip.")
            else:
                print("Select one of the three elements.\n", opponent_elements)

            opponent = opponent_elements[randint(0, 2)]

            if tries >= 5 and rounds < 3:
                if opponent == "water":
                    hint_color = "blue"
                elif opponent == "fire":
                    hint_color = "red"
                elif opponent == "earth":
                    hint_color = "green"

                print(
                    f"\nHINT: You notice that the sprite's crystal is glowing {hint_color}.")

            if rounds < 3:
                choice = input("\nChoose an element.\n> ").lower()
                Scene.clear(self)


class OpeningScene(Scene):

    def enter(self):

        Scene.clear(self)

        print("Chosen one, what is your name?")

        username = input("> ").capitalize()
        player.name = username

        print(f"{player.name}, you are the Avatar and it is your destiny to restore peace and balance to the world. Fire Lord Ozai has created an army to conquer the world. You must master all four elements: air, water, earth and fire and defeat the Fire Lord.\n")

        print("On your journey you will face many challenges, it is your destiny to overcome these adversities and obtain the Lost Scrolls. Each scroll contains secret abilities that only the Avatar can learn. Retrieve the four scrolls and defeat the Fire Lord before all hope is lost.\n")

        print("Your adventure begins NOW, head to the Northern Air Temple to meet your first mentor.")

        input("\nPress 'RETURN' when you're ready.")
        Scene.clear(self)

        return 'air room'


class AirRoom(Scene):

    def enter(self):

        print("After several weeks of traveling you finally reach the Northern Air Temple. A young monk approaches you.\n\n'Hi there! I'm Aang, I'll be teaching you airbending! Wanna go penguin sliding first?!'\n")
        print("\t\t\t\t--- A month of training has passsed. ---\n")

        print(f"'{player.name}, I taught you everything that I know. You've shown great progress! You are ready to begin obtain one of the Lost Scrolls.'\n")

        print("You travel into the wild, heading to the direction that Aang told you. You spend hours trying to find the temple but you cannot. You decided to take a rest under a gigantic tree. Moments later, a group of lemurs fly pass you. You get lost in their synchronous flight...\n\nThen suddenly, one of the lemurs appear by your side. It looks like it wants you to follow it. You quickly follow the lemur through the forest and finally...you found the temple that Aang described. The lemur landed on an old nomadic statue. The temple glows a soft light, it seems like the temple is acknowledging that the Avatar has arrived.\n\nTo enter the temple you must correctly answer the riddle on the tablet at the bottom of the nomadic statue. It reads...")

        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        puzzles.first_puz()

        print("\nCONGRATULATIONS! You have completed the first puzzle and obtained the Lost Air Scroll.")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        print("You read through the Lost Air Scroll and it offers two abilites, however you are only able to master one of the two abilities. Which skill would you like to master?\n")
        print(f"[ 1. HURRICANE BARRAGE ]\nThis is an offensive ability that generates devastating wind currents around your opponent.\n\n")
        print(f"[ 2. LEAPING WHIRLWIND ]\nThis is a defensive ability that allows you to move quickly through the air, your opponent will have a difficult time landing a direct hit.\n\n")
        print("Please select 1 or 2.")

        player.skill_selection(player.airskills)
        print("Chosen One, continue your journey and travel to the Southern Water Tribe to meet your next mentor.")

        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        return 'water room'


class WaterRoom(Scene):

    def enter(self):

        print("After a month of traveling you finally make it to the Southern Water Tribe, you're shivering by how cold it is....then suddenly a young woman approaches you.\n\n'You must be cold, here' She hands you a thick coat. 'I'm Katara and I will be teaching you waterbending. It's nice to meet the Avatar~'\n")

        print("\t\t\t\t--- Two months of training has passed ---\n")

        print(
            f"'{player.name}, you are a waterbending master, you have surpassed me. You are ready to obtain the Lost Water Scroll, good luck Avatar!'\n")

        print("You begin your quest to the water temple where Katara described. During your journey, a terrible snowstorm suddenly appears. It quickly becomes dark so you decided to wait out the storm and find shelter. You stumble upon a nearby den to recuperate. It's freezing and you try your best to stay awake but you end up falling asleep. You wake the next day and find yourself in the center of the water temple.")

        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        print("You look around, confused as how you even got to the temple. There are several floating orbs surrounding you, you're not quite sure what to do...\n\nAfter a couple moments of scanning the room you notice that one of the orbs is a different color than the others. You hurl an icicle to break the different-colored orb.\n")
        print("The orb shatters to pieces revealing a scroll with some sort of sequence. As you try to read the scroll, it suddenly catches on fire. You have to quickly memorize the sequence, are you ready?\n")

        input("Press 'RETURN' to continue.")
        Scene.clear(self)

        puzzles.second_puz()

        print("\nCONGRATULATIONS! You have completed the second puzzle and obtained the Lost Water Scroll.")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        print("You read the Lost Water Scroll and it offers two abilites, however you are only able to master one of the two abilities. Which skill would you like to master?\n")
        print(f"[ 1. TIDAL WHIP ]\nThis is an offensive ability that generates multiple water arms to launch a flurry of water whips against your opponent.\n")
        print(f"[ 2. CRYO SHIELD ]\nThis is a defensive ability that creates an ice shield to block your opponent's attacks.\n\n")
        print("Please select 1 or 2.")

        player.skill_selection(player.waterskills)
        print("Chosen One, continue your journey and travel to Ba Sing Se to meet your next mentor.")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        return 'earth room'


class EarthRoom(Scene):

    def enter(self):

        print("After several weeks of traveling you finally make it to Ba Sing Se, a giant city guarded by a massive fortress around it. You are approached by a young blind girl.\n\n'HEY! My name is Toph. I'm going to be your teacher, let's learn earthbending!'\n")

        print("\t\t\t\t--- Several months of training has passed. ---\n")
        print(
            f"'Good job, {player.name} you finally completed your training. You are ready to begin your next challenge.'\n")

        print("You begin your journey by hiking through mountains, in search of the temple. You find yourself at the peak of one of the tallest mountains in that area. You decided to take a short break when the landscape starts changing.")

        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        puzzles.third_puz()

        print("\nCONGRATULATIONS! You have completed the third puzzle and obtained the Lost Earth Scroll.")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        print("You read the Lost Earth Scroll and it offers two abilites, however you are only able to master one of the two abilities. Which skill would you like to master?\n")
        print(f"[ 1. GEO SMASH ]\nThis is an offensive ability that locks down your opponent by manipulating their surroundings.\n")
        print(f"[ 2. TERRAFORM ]\nThis is a defensive ability that shifts the landscape of the battle and causes your opponent to miss their attack.\n\n")
        print("Please select 1 or 2.")

        player.skill_selection(player.earthskills)
        print("Chosen One, continue your journey and travel to Ember Island to meet your next mentor.")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        return 'fire room'


class FireRoom(Scene):

    def enter(self):
        print("Fortunately, Ember Island was not too far from where you were. After a few days of traveling you finally make it to Ember Island. A young man, with a scar on his face, approaches you.\n\n'Hello, Zuko here, I will be teaching you firebending. We must hurry.'\n")

        print("\t\t\t\t--- A month of training has passsed. ---\n")
        print(
            f"'{player.name}, I have taught you everything that I know, you are more than prepared to take on the final challenge.'\n\n")

        print("You travel to a nearby island that isn't located on any maps. The island is obscured by a heavy fog but you are able to make it to the island safely. As soon as you step onto the island, your challenge begins.\n\n")

        input("Press 'RETURN' to continue.")
        Scene.clear(self)

        puzzles.fourth_puz()

        print("\nCONGRATULATIONS! You have completed the final puzzle and obtained the Lost Fire Scroll.")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        print("You read the Lost fire Scroll and it offers two abilites, however you are only able to master one of the two abilities. Which skill would you like to master?\n")
        print(f"[ 1. ELECTRO SHOCK ]\nThis is an offensive ability that strike your opponent with a powerful jolt of electricity.\n\n")
        print(f"[ 2. SCORCHING VORTEX ]\nThis is a defensive ability that will incinerate anything your opponent throws at you.\n\n")
        print("Please select 1 or 2.")

        player.skill_selection(player.fireskills)
        print("Chosen One, it is time to face the Fire Lord, travel to the Fire Nation to defeat the Fire Lord!")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        return 'boss battle'


class BossBattle(Scene):

    def enter(self):
        print("Fulfill your destiny, restore peace and balance to the world. Prepare for the final battle.\n\nYou will have to fight against the Fire Lord by choosing actions. If you're lucky you may land a critical hit, if you are careless then the entire world will be doomed.\nGood luck Avatar!\n\n")
        print("These are your abilities:\n\n")
        print(f"ATTACK\n{player.attack}\n\n")
        print(f"DEFEND\n{player.defend}\n\n")

        input("Press 'RETURN' to begin the final battle.")
        Scene.clear(self)

        print(f"[ FIRE LORD OZAI ] Avatar, you will be defeated here today, prepare to disappoint all of your loved ones!\n\n")

        while True:

            if enemy.hp <= 0:
                print(
                    "You have defeated the Fire Lord! Peace is restored and you found a well paying job!!")
                return 'final scene'
            elif player.hp <= 0:
                print("You have failed the world...You could not beat Fire Lord Ozai so he has taken over the world. All hope is lost...")
                return 'final scene'

            print(
                f"[\tPlayer's HP: {player.hp}\t\t]\t\t[\tFire Lord's HP: {enemy.hp}\t]")

            print(f"[\t1: ATTACK\t]\t\t\t\t[\t2: DEFEND\t]")
            while True:
                try:
                    print("\nPlease select 1 or 2.")
                    choice = int(input("> "))
                    if choice == 1:
                        player.player_attacks()
                        enemy.enemy_attacks()
                        input("Press 'RETURN' to continue")
                        Scene.clear(self)
                        break

                    elif choice == 2:
                        enemy.player_blocked()
                    else:
                        print("Please select the number 1 or 2.")

                    input("\nPress 'RETURN' to continue")
                    Scene.clear(self)
                    break
                except ValueError:
                    print("Please select the number 1 or 2.")
        return 'final scene'


class Map(object):

    scenes = {
        'opening scene': OpeningScene(),
        'air room': AirRoom(),
        'water room': WaterRoom(),
        'earth room': EarthRoom(),
        'fire room': FireRoom(),
        'boss battle': BossBattle()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


puzzles = Puzzle()
player = User()
enemy = Enemy()
a_map = Map("opening scene")
a_game = Engine(a_map)

a_game.play()
