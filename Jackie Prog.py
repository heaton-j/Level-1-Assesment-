#Find the gender
gender_list = ["Boy", "Girl", "Unisex"]

def gender():
    print(gender_list)
    user_gender = input("What gender would you like?")
    if user_gender in gender_list:
        print("The gender you picked is {}".format(user_gender))
    else:
        print("Your previous input is not available, These are the options available {}".format(gender_list))
gender()

#Find type of name
category_list = ["Popular", "Traditional", "Unique"]

def category():
    print(category_list)
    user_category = input("What category would you like?")
    if user_category in category_list:
        print("The category you picked is {}".format(user_category))
    else:
        print("Your previous input is not available")
        print("these are the options available {}".format(category_list))
category()

#List all possible names + definitions

names_list = [
"Felix", "Jasper", "Kenji", "Asnee", "Arthur", "James", "William", "Fredrick", "Vincent", "Jack",
"Lucas", "Oliver", "Liam", "Michael", "Annalise", "Genevieve", "Willow", "Hana", "Mei", "Iris", "Elizabeth", "Victoria",
"Charlotte", "Marie", "Audrey", "Ava", "Emma", "Sarah", "Evelyn", "Bella", "Luna",  "Aspen",  "Phoenix", "Lumi", "Nico",
"Armani", "Hura", "Azure", "Harper", "Jamie", "Alex", "Sam", "Freddie", "Riley"
]

definitions_list = [
"Happy", "Treasurer", "Strong", "Lightning", "Bear or Thor,the eagle", "Hebrew origin of ‘Jacob’", "Supplanter",
"Resolute protection", "Peaceful ruler", "Conquer", "Supplanter", "Bright, Shining", "Peaceful",
"Strong-willed warrior", "Who is like God?", "Graced with God's bounty", "Woman of the race",
"Freedom", "Flower", "Beautiful", "Rainbow", "Gift of God", "Victory", "Free", "Star of the sea",
"Noble strength", "Life", "Princess", "Wished for child", "Beautiful", "Moon", "Quaking tree", "Blood red",
"Snow", "People of victory"
]

#Ask user if they want to see the definition of the names

def definitions():
       definition = input("Would you like to see the definitions of your names?")
       if definition == "Yes":
         print("You will get the definitions of your names")
       else:
         print("You will not get the definitions of your names")
definitions()

#print out final names for user to see

def final_names():
    if user_gender = "Girl"
    if user_gender = "Popular"
    print(names_list[0,4])
final_names()
