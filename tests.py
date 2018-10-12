#tests.py

'''
About tests.py:
This module contains all the unit tests for testing both the main solution and the helper functions in solution/helpers.py
'''
#Standard library imports
import unittest

#Local application imports
from solution.helpers import convert_time_range_to_integers,\
                             clean_time_range_string,\
                             generate_sets_from_tuple_ranges,\
                             subtract_sets,\
                             determine_split_indices,\
                             split_list_on_index,\
                             split_results_on_split_indices,\
                             convert_integer_to_string_time
from solution.solution import subtract_time_ranges


class TestSolution(unittest.TestCase):
    
    def test_time_range_is_integer_tuple(self):
        self.assertEqual(convert_time_range_to_integers('9:00-10:00'), (540,600))
        
    def test_clean_time_range_string_removes_whitespace(self):
        self.assertEqual(clean_time_range_string('9:00  -  10:00pm '), '9:00-10:00')

    def test_list_of_sets_created(self):
        list_=[(1,5),(0,8),(12,12)]
        output=[{1,2,3,4,5}, {0,1,2,3,4,5,6,7,8}]
        self.assertEqual(generate_sets_from_tuple_ranges(list_),output)

    def test_subtract_sets_01(self):
        A=[{1,2,3,4,5},{10,11,12,13,14,15}]
        B=[{1,2,3},{14,15,16}]
        output=[[4,5],[10,11,12,13]]
        self.assertEqual(subtract_sets(A,B), output)

    def test_subtract_sets_02(self):
        A=[{1,2,3,4,5},{10,11,12,13,14,15}]
        B=[{1,2,3,4,5},{14,15,16}]
        output=[[10,11,12,13]]
        self.assertEqual(subtract_sets(A,B), output)

    def test_split_indices_01(self):
        A=[[1,2,3,5,6,7],[9,10]]
        output=[[2],[]]
        self.assertEqual(determine_split_indices(A),output)

    def test_split_indices_02(self):
        A=[[1,2,3,5,6,7,9,10,11],[9,10,12,13]]
        output=[[2,5],[1]]
        self.assertEqual(determine_split_indices(A),output)

    def test_split_list_on_index_01(self):
        A=[1,2,3,5,6,7,9,10,11]
        indices=[2,5]
        holder=[]
        output=[[1,2,3],[5,6,7],[9,10,11]]
        self.assertEqual(split_list_on_index(A,indices,holder), output)     

    def test_split_list_on_index_02(self):
        A=[1,2,3,4,5,6,7,8]
        indices=[]
        holder=[]
        output=[[1,2,3,4,5,6,7,8]]
        self.assertEqual(split_list_on_index(A,indices,holder), output)

    def test_convert_integer_to_string_time(self):
        minutes=140
        output='02:20'           
        self.assertEqual(convert_integer_to_string_time(minutes),output)

    def test_subtract_time_ranges_01(self):
        A=['9:00-10:00']
        B=['9:00-9:30']
        output=['9:30-10:00']
        self.assertEqual(subtract_time_ranges(A,B),output)

    def test_subtract_time_ranges_02(self):
        A=['9:00-10:00', '10:00-11:00']
        B=['9:00-9:30']
        output=['9:30-10:00','10:00-11:00']
        self.assertEqual(subtract_time_ranges(A,B),output)        

if __name__=='__main__':
    
    suite=unittest.TestLoader().loadTestsFromTestCase(TestSolution)
    unittest.TextTestRunner(verbosity=2).run(suite) 