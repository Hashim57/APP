import os
import csv

from models.persistdb import db, query, update


# from models.classes import Person, Preference, Round, Drink

# from models.persist import write_prefs, read_rows, write_row
mydb = db()

get_all_people = "SELECT * FROM person"
get_all_drinks= "SELECT * FROM drink"
get_people_with_prefs = """
SELECT person.id, person.name 
FROM person 
LEFT JOIN drink ON drink.id = person.name

"""

people = query(mydb, get_all_people)
drinks = query(mydb, get_all_drinks)
prefs = query(mydb, get_people_with_prefs)

mycursor = mydb.cursor()


def save_people():
    
    update(mydb, people)


def save_drinks():
   
    update(mydb, drinks )

def save_prefs():
    
    update(mydb, prefs)
    







# def get_prefs():
    
#     data = {}
#     rows = read_rows("prefs.csv")
#     for row in rows:

            
         
#         person = people[int(row[0])]

          
#         drink = drinks[int(row[1])]

          
#         saved_prefs = Preference(person, drink)

          
#         data.update({person.id:saved_prefs})
            
        
#     return data
    

# def get_people():
#     data = []

#     rows= read_rows("people.csv")

    
#     for row in rows:
#         saved_person = Person(int(row[0]), row[1])

        
#         data.append(saved_person)
        
#     return data

# def get_drinks():

#     data = []

#     rows= read_rows("drinks.csv")

    
#     for row in rows:
#         saved_drink = Drink(int(row[0]), row[1])

#         data.append(saved_drink)
#     return data

def create_pref():
    people = query(mydb, get_all_people)
    print_list(people, "People" )
    try:
        person_id = int(input("Enter Name ID: "))

    except:
        print("Please try again")
    drinks = query(mydb, get_all_drinks)
    print_list(drinks, "Drinks")

    try:
        drink_id = int(input("Enter Drink ID: "))
    except:
        print("Please try again")

    insert_query = f"INSERT INTO prefs (person_id, drink_id) VALUES ('{person_id}', '{drink_id}')"
    
    # drinks.append(drink)
    
    mycursor.execute(insert_query)

    mydb.commit()

    mycursor.close()

    
    # add_to_prefs = f"UPDATE prefs SET drink_id = {drink_id} WHERE person_id = {person_id}"
    # update(mydb, add_to_prefs)
    

        
    
        
            
    
   
        
    
    
    
        




def save_and_exit():
    save_people()
    save_drinks()
    save_prefs()
    exit()



# people = get_people()
# drinks = get_drinks()
# prefs = get_prefs()


def clearScreen():
    os.system("clear")        




def print_list(the_list, title):
    clearScreen()
    print(f"+===============+\n\n | {title.upper()} \n\n=================|") 
    if len(the_list) == 0:
        
        return
    items = the_list

    
    for item in items:
   
        print(item)


def insert_person(data):
  
    query = "INSERT INTO person (name) VALUES (%s)"
    
    recordTuple = (data) 
        # people.append(person)
        
    mycursor.execute(query, recordTuple)

    mydb.commit()

    mycursor.close()

    
    
    # new_person = Person(len(people), name)

    # people.append(new_person)

    # print("You have been assigned an ID number please note this down ")

    # return new_person


    

def insert_drink(data):
    
    query = "INSERT INTO drink (name) VALUES (%s)"
    
    # drinks.append(drink)
    
    recordTuple = (data)
    mycursor.execute(query, recordTuple)

    mydb.commit()

    mycursor.close()
    # new_drink = Drink(len(drinks), name)

    # drinks.append(new_drink)


    # return new_drink
    

    



menu = ''' Welcome to Carib Life v1.0
           Please, select an option by entering a number:

           [1] - List People
           [2] - List Drinks
           [3] - List Favourites
           [4] - Create person
           [5] - Create Drink
           [6] - Preferences
           [7] - exit

           '''   


clearScreen()

def app():
    while True:
        print(menu)
        try:
            option=int(input('Enter your selection: '))

        except:
            print('Please enter a number')
            option = 0
        if option == 1:
            print_list(people, 'people')
        elif option == 2:
            print_list(drinks, 'drinks')
        elif option == 3:
            print_list(prefs, "prefs")
        elif option == 4:
            name = input("Please enter name")
            insert_person([(name)])
        elif option == 5:
            name = input("Please enter drink")
            insert_drink([(name)])
        elif option == 6:
            create_pref()

        
            # chosen_person = None
            # chosen_drink = None

            # print_list(people, "People")
            # while chosen_person == None:
            #     try:
            #         person_idx = int(input("\nChoose a person:"))
            #         chosen_person = people[person_idx]
            #     except:
            #         print("Please Try Again")

            # print_list(drinks, "Drinks" )
            # while chosen_drink == None:
            #     try:
            #         drink_idx = int(input("\nChoose a drink:"))
            #         chosen_drink = drinks[drink_idx]
            #     except:
            #         print("Please try again")   

            # create_pref([(person_idx, drink_idx)])
            
            
            print_list(prefs, "prefs")
            

                
                    
        elif option == 7:

            print('Programme Exited')
            
            break
            
if __name__ == '__main__':
    app()

   
   