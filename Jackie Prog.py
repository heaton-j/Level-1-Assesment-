# Find the gender the user wants for their names

gender_list = { 1 : "Boy", 2 : "Girl", 3 : "Unisex"}
category_list = ["Popular", "Traditional", "Unique"]

# Find the type of gender the user wants for their name

def gender():
    print(gender_list)
    user_gender = int(input("These are the genders available, What gender would you like to choose?"))
    while user_gender not in gender_list.keys():
        print("Your previous input is not available")
        user_gender = input("Please choose a gender from the list")
    print("The gender you picked is {}".format(gender_list.get(user_gender)))

    return user_gender

# Find type of name the user wants for their name

def category():
    print(category_list)
    user_category = input("What category out of these would you like to choose?")
    while user_category not in category_list:
        print("Your previous input is not available")
        user_category = input("Please choose a category from the list")
    print("The category you picked is {}".format(user_category))
    return user_category


# List all possible names

boy_unique = ["Felix", "Jasper", "Kenji", "Asnee"]
boy_traditional = ["Arthur", "James", "William", "Fredrick", "Vincent"]
boy_popular = ["Jack","Lucas", "Oliver", "Liam", "Michael"]
girl_unique = ["Annalise", "Genevieve", "Willow", "Hana", "Mei", "Iris"]
girl_traditional = ["Elizabeth", "Victoria","Charlotte", "Marie", "Audrey"]
girl_popular = ["Ava", "Emma", "Sarah", "Evelyn", "Bella", "Luna"]
unisex_unique = ["Aspen",  "Phoenix", "Lumi", "Nico","Armani"]
unisex_traditional = ["Hura", "Dana", "Kennedy"]
unisex_popular = ["Jamie", "Alex", "Sam", "Freddie", "Riley"]

# list all possible definitions in correct order to the names

boy_unique_definitions = ["Happy", "Treasurer", "Strong", "Lightning"]
boy_traditional_definitions = ["Bear or Thor,the eagle", "Supplanter","Resolute protection", "Peaceful ruler", "Conquer"]
boy_popular_definitions = ["Supplanter", "Bright, Shining", "Peaceful","Strong-willed warrior", "Who is like God?"]
girl_unique_definitions = ["Graced with God's bounty", "Woman of the race","Freedom", "Flower", "Beautiful", "Rainbow"]
girl_traditional_definitions = ["Gift of God", "Victory", "Free", "Star of the sea", "Noble strength"]
girl_popular_definitions = ["Life", "Life", "Princess", "Wished for child", "Beautiful", "Moon"]
unisex_unique_definitions = ["Quaking tree", "Blood red","Snow", "People of victory", "Warrior"]
unisex_traditional_definitions = ["Misshapen head", "Generosity", "Free woman"]
unisex_popular_definitions = ["Supplanter", "Warrior", "Told by God", "Peace Ruler", "Valiant"]

# print out final names for user to see

def final_names(user_gender, user_category):
    print("These are the names for {} , {}".format(User_Gender, User_Category))
    if User_Gender == "Girl":
        if User_Category == "Unique":
            print(girl_unique)
        elif User_Category == "Traditional":
            print(girl_traditional)
        elif User_Category == "Popular":
            print(girl_popular)
    if User_Gender == "Boy":
        if User_Category == "Unique":
            print(boy_unique)
        elif User_Category == "Traditional":
            print(boy_traditional)
        elif User_Category == "Popular":
            print(boy_popular)
    if User_Gender == "Unisex":
        if User_Category == "Unique":
            print(unisex_unique)
        elif User_Category == "Traditional":
            print(unisex_traditional)
        elif User_Category == "Popular":
            print(unisex_popular)

# Ask user if they would like to see the definitions for their names

def definitions():
       definition = input("Would you like to see the definitions of your names?")
       if definition == "Yes":
         print("These are the definitions for the following names in order")
       else:
            exit()

# print out the definitions if user wants to access them

def final_definitions(definition, user_gender, user_category):
    if User_Gender == "Girl":
        if User_Category == "Unique":
            print(girl_unique_definitions)
        elif User_Category == "Popular":
            print(girl_popular_definitions)
        elif User_Category == "Traditional":
            print(girl_traditional_definitions)
    if User_Gender == "Boy":
        if User_Category == "Unique":
            print(boy_unique_definitions)
        elif User_Category == "Popular":
            print(boy_popular_definitions)
        elif User_Category == "Traditional":
            print(boy_traditional_definitions)
    if User_Gender == "Unisex":
        if User_Category == "Unique":
            print(unisex_unique_definitions)
        elif User_Category == "Popular":
            print(unisex_popular_definitions)
        elif User_Category == "Traditional":
            print(unisex_traditional_definitions)

# Main
User_Gender = gender()
print(User_Gender)
User_Category = category()
#print(final_names)
final_names(User_Gender, User_Category)
Definition = definitions()
final_definitions(Definition, User_Gender, User_Category)




