"""
Muneeb Khan
Class: CS 521 - Summer 2
Date:8/21/2021
Final Term Project
This project is a movie catalogue which shows different available movies, along
with its details and price.

"""
from Movie import Movie

def PrintMovieDetails(Movie):
    """ Prints all the details of the movie based on the movie user chooses """
    print("Name: ",Movie.getName())
    print("Category: ",Movie.getCategory())
    print("Description: ",Movie.getDescription())
    print("Price: ",Movie.getPrice())
    print("Price With GST: ",Movie.getPriceWithGST())


def SearchBasedOnNameOrCategory(searchString,listOfMovies):
    """Used to check if searchString is present in any movie 
    name or category
    :return true/false"""

    printed = False
    for movie in listOfMovies:
        if searchString.lower() in movie.getName().lower(
                ) or searchString.lower() in movie.getCategory().lower():
            PrintMovieDetails(movie)
            printed = True
            break
    if printed == False:
        print("No results Found")

def displayMovies(listOfMovies):
    """Used to display the movies one after another"""

    movie_number = 0
    menu_options = ("N","P","M","n","p","m")
    while True:
        print("Movie ", movie_number + 1, " of ", len(listOfMovies))
        print("--------------------------")
        PrintMovieDetails(listOfMovies[movie_number])
        print("___________________________\n"
              "Enter N or n for Next Item\n"
              "Enter P or p for Previous Item\n"
              "Enter M or m to return to Main Menu\n")
        nav_selection = input()

        if nav_selection == "N" or nav_selection == "n":
            print("Inside N")
            print(movie_number, len(listOfMovies))
            if movie_number+1 == len(listOfMovies):
                # print(movie_number)
                # movie_number -= 1
                # print(movie_number)
                print("Inside if")
                print("No further Movies\n")
                continue
            else:
                print("Inside else")
                movie_number += 1
                continue
        elif nav_selection == "P" or nav_selection == "p":
            if movie_number == 0:
                print("No previous movie available\n")
                continue
            else:
                movie_number -= 1
                continue
        elif nav_selection == "m" or nav_selection == "M":
            break

        elif nav_selection not in menu_options:
            print("Wrong Input. Try Again.")
            continue

def displayMovieDetails(listOfMovies):
    """Used to display the info of particular movie"""
    while True:
        for i in range(len(listOfMovies)):
            print(i + 1, listOfMovies[i].getName())

        print("Enter M to return to the Main Menu\n"
              "Please enter your selection")
        nav_selection = input()
        if nav_selection == "M" or nav_selection == "m":
            break
        elif nav_selection.isdigit() and int(nav_selection) >= 0 and int(
                nav_selection) <= len(listOfMovies):
            print("Product ",nav_selection,"of",len(listOfMovies))
            print("--------------------------------")
            PrintMovieDetails(listOfMovies[int(nav_selection) - 1])
            print("--------------------------------")
        else:
            print("Wrong Input, Try again.")
            continue

        nav_selection = input("Enter M or m for previous Menu. Any key to continue\n")
        if nav_selection == "M" or nav_selection == "m":
            break
        else:
            continue

def search(listOfMovies):
    """Used to give the functionality of search engine to the user."""
    while True:
        search = input("Please enter your search input: ")
        SearchBasedOnNameOrCategory(search, listOfMovies)
        print("1, Search again\n"
              "2, Return to Main Menu")
        nav_selection = input()
        if nav_selection == "1":
            continue

        elif nav_selection == "2":
            break

        else:
            print("Wrong Input. Try Again.")
            continue


def countCategory(listOfMovies):
    """Counts the total categories and print them"""
    while True:

        category = set()

        for movie in listOfMovies:
                category.add(movie.getCategory())

        print("There are ",len(category)," categories available to watch.")
        for i in range(len(category)):
            print(category.pop())

        print("1, Return to Main Menu\n")
        nav_selection = input()
        if nav_selection == "1":
            break

        else:
            print("Wrong Input. Try Again.")
            continue

def moviesPerCategory(listOfMovies):
    """Prints out the all the movies of each category"""

    while True:

        movies_per_category = dict()

        for movie in listOfMovies:
            if movie.getCategory() in movies_per_category:
                movies_per_category[movie.getCategory()].append(movie.getName())
            else:
                movies_per_category[movie.getCategory()] = [movie.getName()]

        for key,val in movies_per_category.items():
            print(key,": ",val)

        print("1, Return to Main Menu\n")
        nav_selection = input()
        if nav_selection == "1":
            break

        else:
            print("Wrong Input. Try Again.")
            continue

if __name__ == "__main__":
    file = None
    # opening file
    try:
        file = open("input.txt")
    except Exception as e:
        print(e)
    else:
        print("File opened Successfully!! ")

    # reading file and store each line as element of list and assign to file_data
    file_data = file.readlines()

    #close file and delete headings from list
    file.close()
    del file_data[0]


    listOfMovies = list()
    # iterate through each element(line) in file_data
    for item in file_data:
        #  split the line and store each info to movie_list
        movie_list = item.strip().split(",")
        #create a object of Movie passing movie info as argument and append the
        #object to listOfMovies
        listOfMovies.append(Movie(movie_list[0],movie_list[1
                                                ],movie_list[2],movie_list[3]))

    # loop for Main Menu
    while True:
        print("\nMain Menu\n"
              "___________\n"
              "1, Display all movies available one by one\n"
              "2, Show full details of a movie based on the user's selection\n"
              "3, Search based on Name or Category substring\n"
              "4, How many categories of Movies are available\n"
              "5, Display Movies per Category\n"
              "Q, Enter Q to Quit\n")
        selection = input("Please input your selection: ")

        if selection == "1":
            displayMovies(listOfMovies)


        elif selection == "2":
            displayMovieDetails(listOfMovies)


        elif selection == "3":
            search(listOfMovies)


        elif selection == "4":
            countCategory(listOfMovies)


        elif selection == "5":
            moviesPerCategory(listOfMovies)

        elif selection == "Q":
            break

        else:
            print("Wrong Input, Try Again.")


