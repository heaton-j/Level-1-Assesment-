#Find the gender
gender_list = ["Boy", "Girl", "Unisex"]

def gender():
    print(gender_list)
user_gender = input("What gender would you like?")
if user_gender in gender_list:
    print("The gender you picked is {}".format(user_gender))
else:
    print("Your previous input is not available")
    print("These are the options available {}".format(gender_list))
gender()



