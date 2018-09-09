# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        self.president = None
        self.members = []
        self.name = name
        self.description = description

    def assign_president(self, person):
        if person in self.members:
            self.president = person
        else:
            print("%s is not a member of this club. The president must first be a member before being assigned as the president." % person.name)

    def recruit_member(self, person):
        if person not in self.members:
            self.members.append(person)

    def get_average_age(self):
        total_age = 0
        number_of_members = len(self.members)
        for person in self.members:
            total_age += person.age

        average_age = total_age/number_of_members
        return average_age

    def print_member_list(self):
        print("Members: ")
        for person in self.members:
            if person is self.president:
                print("- %s (%s years old, President) - %s" % (person.name, person.age, person.bio))
            else:
                print("- %s (%s years old) - %s" % (person.name, person.age, person.bio))
            print()

        print("Average age in this club: %syr" % self.get_average_age())
