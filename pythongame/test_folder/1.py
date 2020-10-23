class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        exit(1)


class User(object):

    def __init__(self, name, bender):
        self.name = name
        self.bender = bender


class TitleScreen(Scene):

    def enter(self):
        print("welcome to the game.")
        username = input("What is your name? ")
        typebender = input("What element ?")

        player = User(username, typebender)

        return 'water training'
