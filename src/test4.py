import unittest
from unittest.mock import patch, Mock

from core import print_item, Person


class Test_core(unittest.TestCase):

    @patch("builtins.print")
    def test_print_item(self, mock_print):


        mock_item = Mock("Graham")

        print_item(mock_item)


        self.assertEqual(mock_print.call_count, 1) 





        


if __name__ == "__main__":
    unittest.main()
