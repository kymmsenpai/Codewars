import sort_my_animals

class Animal:
    def __init__(self, name, number_of_legs):
        self.name = name
        self.number_of_legs = number_of_legs
    def to_dict(lst_obj):
        lst = [{
            'name' : lo.name,
            'number_of_legs' : lo.number_of_legs
        } for lo in lst_obj]
        return lst


animals = [
        Animal("Cat", 4),
        Animal("Snake", 0),
        Animal("Dog", 4),
        Animal("Centipede", 50),
        Animal("Human", 2),
        Animal("Bird", 2),
        Animal("Cow", 4),
        Animal("Ant", 6)
    ]

sort_leg_name = Animal.to_dict(sort_my_animals.sort_animals(animals))
print(sort_leg_name)