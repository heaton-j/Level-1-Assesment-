#Find the gender
gender_list = ["Boy", "Girl", "Unisex"]

def gender():
    print(gender_list)
    user_gender = input("What gender would you like?")
    if user_gender in gender_list:
        print("The gender you picked is {}".format(user_gender))
        user_gender = gender
    else:
        print("Your previous input is not available, These are the options available {}".format(gender_list))
        gender()
gender()

#Find type of name
category_list = ["Popular", "Traditional", "Unique"]

def category():
    print(category_list)
    user_category = input("What category would you like?")
    if user_category in category_list:
        print("The category you picked is {}".format(user_category))
        return user_category
    else:
        print("Your previous input is not available")
        print("these are the options available {}".format(category_list))
        category()
category()

#List all possible names

boy_unique = ["Felix", "Jasper", "Kenji", "Asnee"]

boy_traditional = ["Arthur", "James", "William", "Fredrick", "Vincent"]

boy_popular = ["Jack","Lucas", "Oliver", "Liam", "Michael"]

girl_unique = ["Annalise", "Genevieve", "Willow", "Hana", "Mei", "Iris"]

girl_traditional = ["Elizabeth", "Victoria","Charlotte", "Marie", "Audrey"]

girl_popular = ["Ava", "Emma", "Sarah", "Evelyn", "Bella", "Luna"]

unisex_unique = ["Aspen",  "Phoenix", "Lumi", "Nico","Armani"]

unisex_traditional = ["Hura", "Dana", "Kennedy"]

unisex_popular = ["Jamie", "Alex", "Sam", "Freddie", "Riley"]

#list all possible definitions

boy_unique_definitions = ["Happy", "Treasurer", "Strong", "Lightning"]

boy_tradtional_definitions = ["Bear or Thor,the eagle", "Supplanter","Resolute protection", "Peaceful ruler", "Conquer"]
                                                                                
boy_popular_definitions = ["Supplanter", "Bright, Shining", "Peaceful","Strong-willed warrior", "Who is like God?"]

girl_unique_definitions = ["Graced with God's bounty", "Woman of the race","Freedom", "Flower", "Beautiful", "Rainbow"]

girl_traditional_definitions = ["Gift of God", "Victory", "Free", "Star of the sea", "Noble strength"]

girl_popular_definitions = ["Life", "Life", "Princess", "Wished for child", "Beautiful", "Moon"]

unisex_unique_definitions = ["Quaking tree", "Blood red","Snow", "People of victory", "Warrior"]

unisex_traditional_definitions = ["Misshapen head", "Generosity", "Free woman"]

unisex_popular_definitions = ["Supplanter", "Warrior", "Told by God", "Peace Ruler", "Valiant"]

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
    if user_gender == 'Girl':
        if user_category == 'Unique':
            print(girl_unique)
        elif user_category == 'Traditional':
            print(girl_traditional)
        elif user_category == 'Popular':
            print(girl_popular)
    if user_gender == 'Boy':
        if user_category == 'Unique':
            print(boy_unique)
        elif user_category == 'Traditional':
            print(boy_traditional)
        elif user_category == 'Popular':
            print(boy_popular)
    if user_gender == 'Unisex':
        if user_category == 'Unique':
            print(unisex_unique)
        elif user_category == 'Traditional':
            print(unisex_traditional)
        elif user_category == 'Popular':
            print(unisex_popular)

final_names()
