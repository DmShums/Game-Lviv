"""Game module"""

class Room:
    """Room module"""
    def __init__(self, room):
        """Inititalize variables"""
        self.room = room
        self.description = ""
        self.character = None
        self.item = None
        self.linked_room = {}
        self.place = None
        self.support = None

    def set_description(self, text):
        """Set description of a specific room"""
        self.description = text

    def get_details(self):
        """Get description of a specific room"""
        print(f"Character: {self.character}\nItem: {self.item}\n{self.description}\n")

    def link_room(self, other_obj, direction):
        """Link room of self class with other class"""
        self.linked_room[direction] = other_obj

    def set_character(self, char):
        """Set character to room"""
        self.character = char

    def get_character(self):
        """Get character that is room inhabitant"""
        return self.character

    def set_support(self, char):
        self.support = char

    def get_support(self):
        if self.support is not None:
            self.support.help()
        else:
            print("There is no help :(")

    def set_item(self, itm):
        """Set item in the room"""
        self.item = itm

    def get_item(self):
        """Get item in the room"""
        return self.item

    def move(self, plc):
        """Move module"""
        if self.linked_room.get(plc) is not None:
            return self.linked_room.get(plc)
        return self


class Item:
    """Item module"""
    def __init__(self, itm):
        """Init module"""
        self.itm = itm
        self.description = ""

    def set_description(self, desc):
        """Module to describe"""
        self.description = desc

    def get_name(self):
        """Get name of the item"""
        return self.itm

    def describe(self):
        """Get description"""
        return self.description


class Character:
    """Character module"""
    def __init__(self, name, description):
        """Init module"""
        self.name = name
        self.description = description

    def set_conversation(self, text):
        """Module to save chat between characters"""
        self.convers = text

    def describe(self):
        """Get description"""
        print(self.description)



class Enemy(Character):
    """Enemy module"""
    class_death = 0

    def __init__(self, name, description):
        """Init module"""
        super().__init__(name, description)
        self.convers = ""
        self.weakness = ""

    def set_conversation(self, text):
        """Module to save chat between character and enemy"""
        super().set_conversation(text)

    def set_weakness(self, text):
        """Module to define wekness of the enemy"""
        self.weakness = text

    def describe(self):
        """Get description"""
        super().describe()

    def talk(self):
        """Return enemy's lines"""
        print(self.convers)

    def fight(self, fght_with):
        """Fight module"""
        if fght_with == self.weakness:
            Enemy.class_death += 1
            return True
        return False

    def get_defeated(self):
        """Count +1 after each defeated enemy"""
        return Enemy.class_death


class Batyar(Enemy):
    """Batyar enemy module"""
    def __init__(self, name, description):
        """Init module"""
        super().__init__(name, description)
        self.convers = ""
        self.weakness = ""

    def set_conversation(self, text):
        """Module to save chat between character and enemy"""
        super().set_conversation(text)

    def set_weakness(self, text):
        """Module to define wekness of the enemy"""
        self.weakness = text

    def describe(self):
        """Get description"""
        super().describe()

    def talk(self):
        """Return enemy's lines"""
        print(self.convers)

    def fight(self, fght_with):
        """Fight module"""
        if fght_with == self.weakness:
            Enemy.class_death += 1
            return True
        return False


class Laydak(Enemy):
    """Laydak enemy module"""
    def __init__(self, name, description):
        """Init module"""
        super().__init__(name, description)
        self.convers = ""
        self.weakness = ""

    def set_conversation(self, text):
        """Module to save chat between character and enemy"""
        super().set_conversation(text)

    def set_weakness(self, text):
        """Module to define wekness of the enemy"""
        self.weakness = text

    def describe(self):
        """Get description"""
        super().describe()

    def talk(self):
        """Return enemy's lines"""
        print(self.convers)

    def fight(self, fght_with):
        """Fight module"""
        if fght_with == self.weakness:
            Enemy.class_death += 1
            return True
        return False


class Friend(Character):
    """Friend module"""
    def __init__(self, name, description):
        """Init module"""
        super().__init__(name, description)
        self.convers = ""

    def set_conversation(self, text):
        """Module to save chat between character and enemy"""
        super().set_conversation(text)

    def describe(self):
        """Get description"""
        super().describe()

    def talk(self):
        """Return enemy's lines"""
        print(self.convers)


class Student(Friend):
    """Student friend module"""
    def __init__(self, name, description):
        """Init module"""
        super().__init__(name, description)
        self.convers = ""

    def set_conversation(self, text):
        """Module to save chat between character and enemy"""
        super().set_conversation(text)

    def describe(self):
        """Get description"""
        super().describe()

    def talk(self):
        """Return enemy's lines"""
        print(self.convers)

    def help(self):
        """Help main character"""
        print(self.name)
        print(self.description)
        print("Hint: To hit Batyar use long heavy broom of babcia Halia")


class Kavaler(Friend):
    """Student friend module"""
    def __init__(self, name, description):
        """Init module"""
        super().__init__(name, description)
        self.convers = ""

    def set_conversation(self, text):
        """Module to save chat between character and enemy"""
        super().set_conversation(text)

    def describe(self):
        """Get description"""
        super().describe()

    def talk(self):
        """Return enemy's lines"""
        print(self.convers)

    def help(self):
        """Help main character"""
        print(self.name)
        print(self.description)
        print("Hint: To run away from Laydak give him beer")
