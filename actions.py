# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Yousef"
my_age = 35
my_bio = "Failure is not an option!"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
    # your code goes here!
    print("==========================")
    print("What Would you like to do:")
    print("==========================")
    print("1) Creat a new club\nOr\n")
    print("2) Browse and join clubs\nOr\n")
    print("3) View existing clubs\nOr\n")
    print("4) Display memebers of club\nOr\n")
    print("-1) Close the application\n")
    user_input = input("pick a number from 1 - 4 or -1 to exit the application >>>")
    return user_input

def create_club():
    # your code goes here!
    club_name = input("Type the name of your club >>>")
    club_bio = input("Type a description of your club\n>>>")
    new_club = Club(club_name,club_bio)
    new_club.recruit_member(myself)
    new_club.assign_president(myself)

    print("Enter the numbers of the people you want to recruit to your club or -1 to stop")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    for person in population:
    	print("[%d] %s" %(population.index(person)+1, person.name))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    user_input = ""
    while user_input != "-1":
    	user_input = input(">>>")
    	if user_input.isdigit() and int(user_input) <= 15:
    		new_club.recruit_member(population[int(user_input)-1])

    clubs.append(new_club)
    print("Here is your club details:\n\tName: %s\n\tDescription: %s" %(new_club.name, new_club.description))
    print("Members:\n")
    new_club.print_member_list()
    

def view_clubs():
    # your code goes here!
    for club in clubs:
    	print("Name :%s \nDescription: %s \nMembers: %d \n\n" %(club.name , club.description, len(club.membersList)))
    

def view_club_members():
    # your code goes here!
    view_clubs()
    flag = False
    while not flag:
    	user_input = input("Enter the name of the club you would like to see its memebers\n>>>")
    	for club in clubs:
    		if club.name.lower() == user_input.lower():
    			club.print_member_list()
    			flag = True
    			
def join_clubs():
    # your code goes here!
    view_clubs()
    flag = False
    while not flag:
    	user_input = input("Enter the name of the club you would like join it\n>>>")
    	for club in clubs:
    		if user_input.lower() == club.name.lower():
    			club.recruit_member(myself)
    			flag = True

def application():
    introduction()
    # your code goes here!
    option = ""
    while option != "-1":
    	option = options()
    	if option == "1":
    		create_club()
    	elif option == "2":
    		join_clubs()
    	elif option == "3":
    		view_clubs()
    	elif option == "4":
    		view_club_members()
    	elif option == "-1":
    		break