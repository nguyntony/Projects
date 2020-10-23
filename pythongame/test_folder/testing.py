import subprocess as sp
import time
from colorama import Fore, Back, Style


class Map:

    list1 = {
        "first_air": ["air", "earth", "fire", "water"]
    }

    # choice = input("i want you to say air ")
    # if choice == list1["first_air"][0]:
    #     print("you are right!")


# class AnotherClass:

#     print(Map.list1["first_air"][0])


# a_map = Map()
# print(a_map.list1["first_air"][0])

# time.sleep(5)
# sp.call('clear', shell=True)
# # if running on windows you need to use cls
# print("What is the pattern?")
# input("The pattern is...")

print(Back.GREEN + " ")

# caution = "With great power comes with great responsiblity."
# print("Which element would you like master first?")
# element_type = ["Water", "Fire", "Earth", "Air"]

# for element in element_type:
#     print(f"[ {element} ]", end=" ")

# while True:
#     choice = input("\n> ").lower()

#     if choice == "water":
#         print(
#             "Water represents soul, it has a strong connection with healing, intuition and emotion.\n", caution)
#         player.bender = "waterbender"
#         break
#     elif choice == "fire":
#         print(
#             "Fire represents spirit, it has a strong connection with passion, desire and motivation.\n", caution)
#         player.bender = "firebender"
#         break
#     elif choice == "earth":
#         print(
#             "Earth represents body, it has a strong connection with health, security and stability.\n", caution)
#         player.bender = "earthbender"
#         break
#     elif choice == "air":
#         print(
#             "Air represents mind, it has as strong connection with perception, communication and strategy.\n", caution)
#         player.bender = "airbender"
#         break
#     else:
#         print("Please select an element.")
