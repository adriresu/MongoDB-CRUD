import pymongo
import time

def checkIfExists(name):
    name = collection.find_one({"name": name})
    if name is not None:
        return_value = name["name"]
    else:
        return_value = False
    return return_value

#First menu
print("HELLO WORLD, THIS IS A CRUD PROGRAM!!!!")
while True:
    time.sleep(1)
    print("1- Create")
    print("2- Read")
    print("3- Update")
    print("4- Delete")
    print("5- Exit")

    try:
        number = int(input("Choose your option:\n"))
    except ValueError as e:
        print("Only numbers between 1 and 4 are valid")
        continue

#Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["Reinoso"]
    collection = db["reinosoCollection"]

    #CRUD
    #CREATE
    if number == 1:
        name = input("Write a name:\n")
        try:
            age = int(input("Write an age:\n"))
        except ValueError as e:
            print("Only numbers are valid")
            age = int(input("Write an age:"))
        person = {"name": name, "age": age}
        collection.insert_one(person)
    #READ
    elif number == 2:
        name = input("From who do you want to know the age?\n")
        print(collection.find_one({"name": name})["age"]) if checkIfExists(name) else print("Not found")
    #UPDATE
    elif number == 3:
        name = input("From who do you want to change the age?\n")
        if checkIfExists(name) is None:
            print("Not found")
        else:
            try:
                age = int(input("What is the new age?\n"))
            except ValueError as e:
                print("Only numbers are valid")
                age = int(input("What is the new age?\n"))
            collection.update_one({"name": name}, {"$set": {"age": age}})
    #DELETE
    elif number == 4:
        print("DELETE")
        name = input("De quien quieres borrar la informacion?\n")
        if checkIfExists(name) is None:
            print("Not found")
        else:
            collection.delete_one({"name": name})
    #EXIT
    elif number == 5:
        break
    else:
        print("ERROR, select a number between 1 and 4")

client.close()

