import unittest
from unittest.mock import patch, Mock


class Drink():
    pass



def print_item(item = Drink):
        print(item)


class Test_core(unittest.TestCase):

    @patch("builtins.print")
    def test_print_item(self, mock_print):


        mock_item = ["Pina Colada"]

        print_item(mock_item)

    


        self.assertEqual(mock_print.call_count, 1) 





        


if __name__ == "__main__":
    unittest.main()


