
import unittest
from src.models.classes import Person, Drink


class Test_Models(unittest.TestCase):
    def test_person(self):


    
        expected = {"name":"John", "id":0}

        actual = Person(0, "John").__dict__


        self.assertEqual(expected, actual)



    def test_drink(self):
        expected = {"name":"Desparado", "id":3}

        actual = Drink(3, "Desparado").__dict__


        self.assertEqual(expected, actual)


    

    


    




    
if __name__ == "__main__":
    unittest.main()




    










   

    
