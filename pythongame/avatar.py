from textwrap import dedent
from os import system, name
import time
from random import randint


class User(object):

    def __init__(self):
        self.name = "Player1"
        self.hp = 100

        self.attack = ["Basic Attack"]
        self.attack_desc = {
            'Hurricane Barrage': '[ AVATAR ] You hurl devastating wind currents towards the Fire Lord.',
            'Octo Stance': '[ AVATAR ] You attack the Fire Lord with several water whips at all directions.',
            'Earthquake': '[ AVATAR ] The ground near the Fire Lord shakes, as small boulders hit him from the impact.',
            'Lightning Strike': '[ AVATAR ] You strike a powerful jolt of electricity at the Fire Lord'
        }
        self.defend = ["Block"]
        self.defend_desc = {
            'Leaping Whirlwind': '[ AVATAR ] You launch yourself into the air, attempting to dodge the Fire Lord\'s attack.',
            'Overheat': '[ AVATAR ] You blast a scorching fire from your palms, attempting to absorb the Fire Lord\'s attack.',
            'Land Rift': '[ AVATAR ] You shift the land around the Fire Lord, causing him to not land a direct hit.',
            'Cryo Shield': '[ AVATAR ] You shield yourself with a thick armor of ice, minimizing the damage from the Fire Lord\'s attack.'
        }

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
                            print("You dealt 20 damage.")
                            damage = 20
                            enemy.hp -= damage
                        elif luck > 6:
                            print("You dealt 30 damage.")
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


class Enemy(object):

    def __init__(self):
        self.name = "Fire Lord Ozai"
        self.hp = 100
        self.skills = [
            "He takes a deep breath then hurls a giant fireball at you.",
            "He harnesses the power from his surroundings and shoots lightning at you.",
            "He jumps into the air and unleashes an onslaught of quick fire bullets.",
            "He unleashes a series of lightning orbs at you."
        ]

    def enemy_attacks(self):
        random_num = randint(0, 3)
        hit = 20

        print(f"\n[ FIRE LORD OZAI ] {enemy.skills[random_num]}")
        print(f"You took {hit} damage.\n")

        player.hp -= hit

    def player_blocked(self):
        random_num = randint(0, 3)
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
                        block = 10
                        hit -= block
                        print(
                            f"\n[ FIRE LORD OZAI ] {enemy.skills[random_num]}\n")
                        while ability > 1:
                            skilldesc = player.defend[ability - 1]
                            print(player.defend_desc[skilldesc])
                            break
                        # print(
                        #     "You attempt to shield yourself from the incoming attack.")
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
        if name == "nt":
            _ = system('cls')
        else:
            _ = system('clear')

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

        print("Journey without it and you will never prevail, but if you have too much of it you will surely fail.\n")

        while True:
            user_answer = input("> ").lower()
            if user_answer == answer:
                print("That's right!")
                break
                # have the game continue
            else:
                print("Try again.\n")

    def second_puz(self):
        # second puzzle will be a memorization game.
        print(dedent("""Using the keys 'WASD' repeat the sequence that is on the scroll.\n
        \t\t-------------------------------------\n
        \t\t\t\t W = Up\n
        \t\tA = Left\tS = Down\tD = Right\n
        \t\t-------------------------------------"""))
        input("\nPress 'RETURN' when you are ready.")

        answer = "wssadwda"
        seconds = 5
        attempts = 3

        print(
            f"[ UP, DOWN, DOWN, LEFT, RIGHT, UP, RIGHT, LEFT ]\n\nYou have {seconds} seconds to memorize this sequence.")

        while True:
            time.sleep(seconds)
            Scene.clear(self)

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
                        Scene.clear(self)
            break

    def third_puz(self):
        # guessing game
        print("There are five pillars before you, you're not sure what to do...After a couple of moments of scanning around you notice some writing on a stone tablet:\n\nYou must light the pillars in the correct order to unlock the treasure you seek. If they are not, the pillars will reset.\n")

        input("Press 'RETURN' when you're ready.")

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
        print("You are trapped in a maze alone... or so you think.\n\nA powerful sprite appears, it can harness different elements, thus allowing it to change forms to unleash devatasting attacks. You notice that the sprite has a weak spot. Hit the weak spot 3 times to defeat the sprite!")
        input(dedent("""
        Choose an element between fire, water or earth. If you're lucky the correct element will give you an advantageous edge over the sprite.

        Press 'RETURN' when you're ready.
        """))

        opponent_elements = ["water", "fire", "earth"]
        opponent = opponent_elements[randint(0, 2)]
        choice = input(
            "Choose an element (Fire, Water, or Earth):\n> ").lower()
        # choice = choice.lower()
        rounds = 0

        while rounds < 3:
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
                    print("[Outcome] You hurl a barrage of small fireballs at the water sprite, it blocks your attack with a powerful wave. You get hurt by following water whip.")
            else:
                print("Select one of the three elements.\n", opponent_elements)
            if rounds < 3:
                choice = input("\nChoose an element.\n> ").lower()
                opponent = opponent_elements[randint(0, 2)]
                Scene.clear(self)


class OpeningScene(Scene):

    def enter(self):

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

        while True:
            try:
                choice = int(input("> "))

                if choice == 1:
                    player.attack.append("Hurricane Barrage")
                    choice = "Hurricane Barrage"
                    break
                elif choice == 2:
                    player.defend.append("Leaping Whirlwind")
                    choice = "Leaping Whirlwind"
                    break
                else:
                    print("Please select the number 1 or 2.")

            except ValueError:
                print("Please select the number 1 or 2.")

        print(f"You have successfully learned {choice}.")
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

        print("You read through the Lost Water Scroll and it offers two abilites, however you are only able to master one of the two abilities. Which skill would you like to master?\n")
        print(f"[ 1. OCTO STANCE ]\nThis is an offensive ability that generates multiple water arms to launch a flurry of water whips against your opponent.\n")
        print(f"[ 2. CRYO SHIELD ]\nThis is a defensive ability that creates an ice shield to block your opponent's attacks.\n\n")
        print("Please select 1 or 2.")

        while True:
            try:
                choice = int(input("> "))

                if choice == 1:
                    player.attack.append("Octo Stance")
                    choice = "Octo Stance"
                    break
                elif choice == 2:
                    player.defend.append("Cryo Shield")
                    choice = "Cryo Shield"
                    break
                else:
                    print("Please select the number 1 or 2.")

            except ValueError:
                print("Please select the number 1 or 2.")

        print(f"You have successfully learned {choice}.")
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

        print("You begin your journey by hiking through mountains, in search of the temple. You find yourself at the peak of one of the tallest mountains in that area. You decided to take a short break when the landscape started changing.")

        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        puzzles.third_puz()

        print("\nCONGRATULATIONS! You have completed the third puzzle and obtained the Lost Earth Scroll.")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        print("You read through the Lost Earth Scroll and it offers two abilites, however you are only able to master one of the two abilities. Which skill would you like to master?\n")
        print(f"[ 1. EARTHQUAKE ]\nThis is an offensive ability that locks down your opponent by manipulating their surroundings.\n\n")
        print(f"[ 2. LAND RIFT ]\nThis is a defensive ability that shifts the landscape of the battle and causes your opponent to miss their attack.\n\n")
        print("Please select 1 or 2.")

        while True:
            try:
                choice = int(input("> "))

                if choice == 1:
                    player.attack.append("Earthquake")
                    choice = "Earthquake"
                    break
                elif choice == 2:
                    player.defend.append("Land Rift")
                    choice = "Land Rift"
                    break
                else:
                    print("Please select the number 1 or 2.")

            except ValueError:
                print("Please select the number 1 or 2.")

        print(f"You have successfully learned {choice}.")
        print("Chosen One, continue your journey and travel to Ember Island to meet your next mentor.")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        return 'fire room'


class FireRoom(Scene):

    def enter(self):
        print("Fortunately, Ember Island was not too far from where you were. After a few days of traveling you finally make it to Ember Island. A young man, with a scar on his face, approaches you.\n\n'Hello, Zuko here, I will be teaching  you firebending. We must hurry.'\n")

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

        print("You read through the Lost fire Scroll and it offers two abilites, however you are only able to master one of the two abilities. Which skill would you like to master?\n")
        print(f"[ 1. LIGHTNING STRIKE ]\nThis is an offensive ability that strike your opponent with a powerful jolt of electricity.\n\n")
        print(f"[ 2. OVERHEAT ]\nThis is a defensive ability that will incinerate anything your opponent throws at you.\n\n")
        print("Please select 1 or 2.")

        while True:
            try:
                choice = int(input("> "))

                if choice == 1:
                    player.attack.append("Lightning Strike")
                    choice = "Lightning Strike"
                    break
                elif choice == 2:
                    player.defend.append("Overheat")
                    choice = "Overheat"
                    break
                else:
                    print("Please select the number 1 or 2.")

            except ValueError:
                print("Please select the number 1 or 2.")

        print(f"You have successfully learned {choice}.")
        print("Chosen One, it is time to face the Fire Lord, travel to the Fire Nation to defeat the Fire Lord!")
        input("\nPress 'RETURN' to continue.")
        Scene.clear(self)

        return 'boss battle'


class FinalScene(Scene):

    def enter(self):
        print("The end")
        return 'final scene'


class BossBattle(Scene):

    def enter(self):
        print("Fulfill your destiny, restore peace and balance to the world. Prepare for the final battle.\n\nYou will have to fight against the Fire Lord by choosing actions. If you're lucky you may land a critical hit, if you are careless then the entire world will be doomed.\nGood luck Avatar!\n\n")
        print("These are your abilities:\n\n")
        print(f"ATTACK\n{player.attack}\n\n")
        print(f"DEFEND\n{player.defend}\n\n")

        input("Press 'RETURN' to begin the final battle.")
        Scene.clear(self)

        print(f"[ FIRE LORD OZAI ] Avatar, you will be defeated here today, prepare to disappoint all of your loved ones!\n\n")
        i = 0
        while True:

            if player.hp <= 0:
                print("You have failed the world...You could not beat Fire Lord Ozai so he has taken over the world. All hope is lost...")
                return 'final scene'
            if enemy.hp <= 0:
                print(
                    "You have defeated the Fire Lord! Peace is restored and you found a well paying job!!")
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
        'boss battle': BossBattle(),
        'final scene': FinalScene()
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
