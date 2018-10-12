#tests.py

'''
About tests.py:
This module contains all the unit tests for testing both the main solution and the helper functions in solution/helpers.py
'''

class TestSolution(unittest.TestCase):
    
    def test_time_range_is_integer_tuple(self):
        self.assertEqual(convert_time_range_to_integers('9:00-10:00'), (540,600))
        
    def test_clean_time_range_string_removes_whitespace(self):
        self.assertEqual(clean_time_range_string('9:00  -  10:00pm '), '9:00-10:00')
    

if '__name__'=='__main__':
    
suite=unittest.TestLoader().loadTestsFromTestCase(TestSolution)
unittest.TextTestRunner(verbosity=2).run(suite) 