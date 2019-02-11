"""
Cassie Wang
CSCI051P
4/9/2018
This program is object-oriented and defines a new class of objects called Menus. Each menu is for a specific meal,
comprised of a variety of appetizers, entrees, and desserts. Menus can be added to or have items removed from it. Menus
can also display the options for one course of the selected meal. Menus can also randomly choose one dish from each
course and generate a random meal. This program has a set meal for breakfast, lunch, and dinner. It asks the user which
menus they would like to see and if they would like to make changes to any of the menus. Then it randomly generates
a breakfast, lunch, and dinner for the user from the set menus.
"""
from random import*


class Menu:
    """
    Represents the appetizer, main, and dessert courses of a menu.
    attr: meal, appetizer, main, dessert
    """
    def __init__(self, meal = "breakfast", app = "toast", entree = "cereal", dessert = "fresh fruit"):
        """
        Defines the attributes of Menu.
        meal(str): Can be breakfast, brunch, lunch, or dinner
        app(str): optional, default set to "toast". A string of appetizer options
        entree(str): a string of entree options
        dessert(str): optional, default set to "fresh fruit". A string of dessert options
        """
        self.meal = meal
        self.app = app
        self.entree = entree
        self.dessert = dessert

    def add_option(self, food, course):
        """
        Adds one food option for selected course of a meal.
        Args:
            course(str): Appetizer, Entree, or Dessert. Course to add food option to.
            food(str): one food item to be added to a specified course
        Returns:
            None
        """
        # Puts string of food items for specified course into a list, separating food items by commas
        new_app_list = []
        app_list = self.app.split(", ")
        for elem in app_list:
            new_app_list.append(elem)

        new_entree_list = []
        entree_list = self.entree.split(", ")
        for elem in entree_list:
            new_entree_list.append(elem)

        new_dessert_list = []
        dessert_list = self.dessert.split(", ")
        for elem in dessert_list:
            new_dessert_list.append(elem)

        # Adds food item to course list, joins items back together as a string, and updates the global variable
        if course == "appetizer" and "Appetizer" and "appetizers" and "Appetizers":
            new_app_list.append(food)
            self.app = ", ".join(new_app_list)

        elif course == "entree" and "Entree" and "entrees" and "Entrees":
            new_entree_list.append(food)
            self.entree = ", ".join(new_entree_list)

        elif course == "dessert" and "Dessert" and "desserts" and "Desserts":
            new_dessert_list.append(food)
            self.dessert = ", ".join(new_dessert_list)

    def remove_option(self, food, course):
        """
        Gets rid of one food option from selected course of the meal.
        Args:
            food(str): one food item to be removed from course menu
            course(str): Appetizer, Entree, or Dessert. Course to remove food from.
        Returns:
            None
        """
        # Puts string of food items for specified course into a list, separating food items by commas
        new_app_list = []
        app_list = self.app.split(", ")
        for elem in app_list:
            new_app_list.append(elem)

        new_entree_list = []
        entree_list = self.entree.split(", ")
        for elem in entree_list:
            new_entree_list.append(elem)

        new_dessert_list = []
        dessert_list = self.dessert.split(", ")
        for elem in dessert_list:
            new_dessert_list.append(elem)

        # Removes food item from course list, joins items back together as a string, and updates the global variable
        if course == "appetizer" and "Appetizer" and "appetizers" and "Appetizers":
            new_app_list.remove(food)
            self.app = ", ".join(new_app_list)
        elif course == "entree" and "Entree" and "entrees" and "Entrees":
            new_entree_list.remove(food)
            self.entree = ", ".join(new_entree_list)
        elif course == "dessert" and "Dessert" and "desserts" and "Desserts":
            new_dessert_list.remove(food)
            self.dessert = ", ".join(new_dessert_list)

    def display_app(self):
        """
        Returns all appetizers for the selected meal.
        Args:
            None
        Returns:
            (str): all the appetizers for specified meal
        """
        return self.app

    def choose_app(self):
        """
        Randomly selects and returns one item from the appetizer list for the meal
        Args:
            None
        Returns:
            (str): one item from appetizer list
        """
        app_list = self.app.split(", ") # Puts string of food items into list of strings to index into
        item = randint(0,len(app_list)-1) # Randomly chooses a number within length of list and indexes into list
        return app_list[item]

    def display_entree(self):
        """Returns all entrees for the selected meal.
        Args:
            None
        Returns:
           (str): all the entrees for specified meal
        """
        return self.entree

    def choose_entree(self):
        """
        Randomly selects and returns one item from the main list for the meal
        Args:
            None
        Returns:
            (str): one item from main course list
        """
        entree_list = self.entree.split(", ")
        item = randint(0, len(entree_list)-1)
        return entree_list[item]

    def display_dessert(self):
        """
        Returns all desserts for the selected meal.
        Args:
            None
        Returns:
            (str): all the desserts for specified meal
        """
        return self.dessert

    def choose_dessert(self):
        """
        Randomly selects and returns one item from the dessert list for the meal
        Args:
            None
        Returns:
            (str): one item from the dessert list
        """
        dessert_list = self.dessert.split(", ")
        item = randint(0, len(dessert_list)-1)
        return dessert_list[item]

    def random_meal(self):
        """
        Generates a random meal by calling on previous functions and returns one appetizer, entree, and dessert from
        menu of specified meal.
        Args:
            None
        Returns:
            (str): a meal consisting of one appetizer, one entree, and one dessert
        """
        meal = self.meal
        # Randomly selects one food item for each course
        rand_app = self.choose_app()
        rand_entree = self.choose_entree()
        rand_dessert = self.choose_dessert()
        return "For " + meal + ", you will be having " + rand_app + ", " + rand_entree + ", " + "and " + rand_dessert
        + ".\n"



    def __str__(self):
        """
        Takes the Menu and returns it as a string
        Args:
            None
        Returns:
            (str): menu in string form
        """
        return(self.meal + "\n\tAppetizers: " + self.app + "\n\tEntrees: " + self.entree + "\n\tDesserts: "+
                self.dessert + "\n")


def main():
    """
    Sets a breakfast, lunch, and dessert menu, specifying the meal, appetizer, main course, and dessert. Asks the user
    which menus they would like to see. Then asks user if they would like to make any changes to any of the courses of
    any of the meals. Then randomly generates a breakfast, lunch, and dinner for the user.
    Args:
        None
    Returns:
        None
    """
    breakfast = Menu(app="bacon, scrambled eggs, muffins", entree="pancakes, french toast, oatmeal")
    lunch = Menu("lunch", "apple, peppers and hummus, chips and salsa", "BLT sandwiches, mac n' cheese, cheeseburgers, "
                                                                        "PB&J", "chocolate chip cookies, sugar cookies,"
                                                                                " cupcakes")
    dinner = Menu("dinner", "garlic bread, calamari, queso, onion rings", "lasagna, pizza, steak and vegetables, fried "
                                                                          "chicken", "tiramisu, red velvet cake")

    show = True # Indicates whether user would like to see another menu or not
    while show:
        show_menu = input("Would you like to see the menu for breakfast, lunch or dinner?\n\t")
        if show_menu == "breakfast" and "Breakfast":
            print(breakfast)
        elif show_menu == "lunch" and "Lunch":
            print(lunch)
        elif show_menu == "dinner" and "Dinner":
            print(dinner)

        another_menu = input("Would you like to see the menu for another meal?\n\t")
        if another_menu == "yes" and "Yes":
            show = True # Indicates to show another menu
        elif another_menu == "no" and "No":
            show = False # Indicates not to show another menu

    change_menu = input("Would you like to change any menu?\n\t")
    if change_menu == "yes" and "Yes":
        change = True # Indicates whether user would like to change the menu
        while change:
            # Gathers details of what meal and course user would like to add or remove to and with what food item
            menu_choice = input("Would you like to change the breakfast, lunch, or dinner menu?\n\t")
            change_food = input("Would you like to add or remove a food item?\n\t")
            course = input("Would you like to change the appetizer, entree, or dessert menu?\n\t")
            food = input("What food item would you like to add or remove? Please choose one for now.\n\t")

            # Makes appropriate change as specified by user and prints updated menu
            if menu_choice == "breakfast" and "Breakfast":
                if change_food == "add" and "Add":
                    breakfast.add_option(food, course)
                else:
                    breakfast.remove_option(food, course)
                print("Here is the updated menu:\n\t Appetizers: " + breakfast.display_app() + "\n\tEntrees: "
                      + breakfast.display_entree() + "\n\tDesserts: " + breakfast.display_dessert())
            elif menu_choice == "lunch" and "Lunch":
                if change_food == "add" and "Add":
                    lunch.add_option(food, course)
                else:
                    lunch.remove_option(food, course)
                print("Here is the updated menu:\n\t Appetizers: " + lunch.display_app() + "\n\tEntrees: "
                      + lunch.display_entree() + "\n\tDesserts: " + lunch.display_dessert())
            elif menu_choice == "dinner" and "Dinner":
                if change_food == "add" and "Add":
                    dinner.add_option(food, course)
                else:
                    dinner.remove_option(food, course)
                print("Here is the updated menu:\n\t Appetizers: " + dinner.display_app() + "\n\tEntrees: "
                      + dinner.display_entree() + "\n\tDesserts: " + dinner.display_dessert())

            more_change = input("Would you like to make another change to a menu?\n\t")
            if more_change == "yes" and "Yes":
                change = True # Indicates user still wants to make a change and to loop through previous process
            else:
                change = False # Indicates user does not want to make anymore changes

    # Generates random breakfast, lunch, and dinner for user
    print("\n****************************************************\nNow generating your meals for today... \n\n" +
          breakfast.random_meal() + ".\n" + lunch.random_meal() + ".\n" + dinner.random_meal() + ". Bon appetit!")


if __name__ == "__main__":
    main()

