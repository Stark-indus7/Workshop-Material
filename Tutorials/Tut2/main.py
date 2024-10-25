# Unique Word Counter
# list1 = []

# limit = int(input("Enter The Limit : "))
# for i in range(limit):


profile = []

def Add():
    for i in range(2):
        id = input("Enter your ID: ")
        name = input("ENter Your Name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your E-mail: ")
        
        profile.append({"ID":id,"NAME":name,"AGE":age,"EMAIL":email})

        show_profile()

def show_profile():
    for j in profile:
        print(f"""
            ID : {j["ID"]}
            Name : {j["NAME"]}
            Age : {j["AGE"]}
            Email : {j["EMAIL"]}
            """)

def update():
    print(profile)
    search = int(input("Enter The number Of Profile You Want to update : "))
    get_profile = profile[search - 1]
    print(get_profile.keys())
    key = input("Enter The Key To update : ")
    value = input("Enter The Value : ")
    get_profile[key] = value
    print(get_profile)
    print(profile)

            
