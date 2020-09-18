import os
import csv

from models.persistdb import db, query, update


# from models.classes import Person, Preference, Round, Drink

# from models.persist import write_prefs, read_rows, write_row
mydb = db()

get_all_people = "SELECT * FROM person"
get_all_drinks= "SELECT * FROM drink"
get_prefs = """
SELECT person.id, person.name, drink.id as drink_id
FROM person
LEFT JOIN drink ON drink.id = person.name

"""

people = query(mydb, get_all_people)
drinks = query(mydb, get_all_drinks)
prefs = query(mydb, get_prefs)

mycursor = mydb.cursor()


def save_people():
    
    update(mydb, people)


def save_drinks():
   
    update(mydb, drinks )

def save_prefs():
    col= []
    person_id= col[0]
    drink_id = col[1]
    add_to_prefs = f'UPDATE person SET drink = {drink_id} WHERE id = {person_id}'
    
    update(mydb, add_to_prefs)
    







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

def create_pref(person, drink):
    try:
    
        query = "INSERT INTO person (perosn_id, drink_id) VALUES (%s, %s)"
        values = ([(person, drink)])
        
        mycursor.execute(query, values)

        mydb.commit()
    except:
        print("Failed to add pref")
    
    
        




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
        
            chosen_person = None
            chosen_drink = None

            print_list(people, "People")
            while chosen_person == None:
                try:
                    person_idx = int(input("\nChoose a person:"))
                    chosen_person = people[person_idx]
                except:
                    print("Please Try Again")

            print_list(drinks, "Drinks" )
            while chosen_drink == None:
                try:
                    drink_idx = int(input("\nChoose a drink:"))
                    chosen_drink = drinks[drink_idx]
                except:
                    print("Please try again")   

            create_pref(chosen_person, chosen_drink)
            
            
            print_list(prefs, "prefs")
            

                
                    
        elif option == 7:

            print('Programme Exited')
            
            break
            
if __name__ == '__main__':
    app()

   
   