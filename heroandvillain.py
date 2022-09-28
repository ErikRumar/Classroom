class Hero():
    def init(self, name: str, secret_identity: str, weakness: str, catch_phrase: str,\
     exposed: bool, rivals: list,) -> None:
        self.name = name
        self.secret_identity = secret_identity
        self.weakness = weakness
        self.catch_phrase = catch_phrase
        self.exposed = exposed
        self.rivals = rivals
    
    def say_catch_phrase(self):
        print(self.catch_phrase)

    def expose(self):
        self.exposed = True

    def get_identity(self):
        return self.secret_identity


class Villain:
    def __init__(self, name: str, secret_identity: str, hideout: str, secret_plan: str, \
        evil_speech: str, henchmen: list, nemesis: Hero) -> None:
        self.name = name
        self.secret_identity = secret_identity
        self.hideout = hideout
        self.secret_plan = secret_plan
        self.evil_speech = evil_speech
        self.henchmen = henchmen
        self.nemesis = nemesis

    def get_identity(self):
        return self.secret_identity

    def reveal_plan(self):
        print("MUHAHAHAHAHAHAHA", self.secret_plan, "HAHAAH", self.evil_speech)

    def recruit_henchman(self, new_hench):
        self.henchmen.append(new_hench)


class Henchman:
    def __init__(self, name: str, works_for: Villain, salary: int, role: str) -> None:
        self.name = name
        self.works_for = works_for
        self.salary = salary
        self.role = role
