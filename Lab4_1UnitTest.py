import unittest
from Lab4_1 import CircularLinkedList

class TestCircularLinkedList(unittest.TestCase):
    
    def test_sum_positive(self):
        circular_list = CircularLinkedList()
        circular_list.append(5)
        circular_list.append(-3)
        circular_list.append(10)
        circular_list.append(-7)
        self.assertEqual(circular_list.sum_positive(), 15)
    
if __name__ == '__main__':
    unittest.main()
