# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Mshary"
my_age = 23
my_bio = "Me, Myself, and I"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    print("-------------------")
    print("Would you like to:")
    print("1) Create a new club.")
    print("or:")
    print("2) Browse and join clubs.")
    print("or:")
    print("3) View existing clubs.")
    print("or:")
    print("4) Display members of a club.")
    print("or:")
    print("-1) Close application.")
    return input("> ")

def create_club():
    name = input("Pick a name for your awesome new club: ")
    description = input("What is your club about?\n")
    new_club = Club(name, description)
    new_club.recruit_member(myself)
    new_club.assign_president(myself)
    print("Enter the numbers of the people you would like to recruit to your new club (-1 to stop):")
    population.print_people()
    num = 0
    while num != "-1":
        num = input("> ")
        if num.isdigit() and int(num) <= len(population.people):
            person = population.people[int(num)-1]
            new_club.recruit_member(person)

    print("Here's your club:")
    print(new_club.name)
    print(new_club.description)
    new_club.print_member_list()
    clubs.append(new_club)


def view_clubs():
    for club in clubs:
        print("\tNAME: %s\n\tDESCRIPTION: %s\n\tMEMBERS: %s\n" % (club.name, club.description, len(club.members)))

def view_club_members():
    view_clubs()
    club_name = input("Enter the name of the club whose members you'd like to see: ")
    for club in clubs:
        if club.name == club_name:    
            club.print_member_list()

def join_clubs():
    view_clubs()
    club_name = input("Enter the name of the club you'd like to join: ")
    for club in clubs:
        if club.name == club_name:
            club.recruit_member(myself)
            print("%s just joined %s!" % (myself.name, club.name))


def application():
    introduction()
    option = ""
    while option != "-1":
        option = options()
        if option.isdigit():
            if int(option) == 1:
                create_club()
            elif int(option) == 2:
                join_clubs()
            elif int(option) == 3:
                view_clubs()
            elif int(option) == 4:
                view_club_members()
