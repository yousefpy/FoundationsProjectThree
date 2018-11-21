# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description

        self.membersList = []
        self.president = ""


    def assign_president(self, person):
        # your code goes here!
        if person in self.membersList:
            self.president = person


    def recruit_member(self, person):
        # your code goes here!
        if person not in self.membersList:
            self.membersList.append(person)


    def print_member_list(self):
        # your code goes here!
        # print("Here is your club details:\nName: %s\n%s" %(self.name, self.description))
        # print("Members:")
        for member in self.membersList:
            if member == self.president:
                print(" - %s (%s years old , President) - %s\n" %(member.name, member.age , member.bio))
            else:
                print(" - %s (%s years old) - %s\n" %(member.name, member.age , member.bio))