import unittest
from app import app

class Tests(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
        
   
    def test_positive(self):
        response = self.app.get('/fib/-1')
        self.assertEqual(response.data, 'Number should be positive')
        

    def test_start_bigger_than_one(self):
        response = self.app.get('/fib/1')
        self.assertEqual(response.data, 'Number should be greater than 1')
        

    def test_successful_combinations_fibonacci(self):
        response = self.app.get('/fib/11')
        if self.assertEqual(response.data, '[ [2, 2, 2, 2, 3], [2, 2, 2, 5], [2, 3, 3, 3], [3, 3, 5], [3,8] ]'):
            self.assertEqual(response.status, '200 OK')
            
        else:
            self.assertEqual(response.status, '400 Error')
if __name__ == '__main__':
    unittest.main()
