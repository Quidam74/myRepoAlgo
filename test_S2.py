""" Basic introduction to unit testing with Python

@brief get started with python testing by looking at https://docs.pytest.org/en/latest/getting-started.html#getstarted. Note that any script to be ran within the python testing framework (pytest) should follow the standard test discovery rules (https://docs.pytest.org/en/latest/goodpractices.html#test-discovery)
"""

import os
print('Starting test script from working directory : '+os.getcwd())

def test_basicTrue():
    """ one of the simplest test that does nothing except saying it works..."""
    assert True


#testing session 1 functions
def load_s1_script():
    """
        utility function that tris to load the script written along the first lesson
        @throws an ImportError exception if the script file does not exist
        @return the script as a loaded module
    """
    S1_script_filename='assignments/Session1/S1_algotools.py'
    print('Trying to load target scripts:'+S1_script_filename)
    import imp
    s1_algotools=imp.load_source('session_1_script', S1_script_filename)
    return  s1_algotools



#load the scripts to check
def test_session1script_exists():
    try:
        load_s1_script()
        assert True
    except  ImportError:
        print('Expected script not found, carrefuly check the assignement instructions ')
        assert False

def check_s1_selective_average(testList):
    ##
    # utility function that asserts if load_S1_script().average_above_zero works fine
    # @param testList a list of values onto average_above_zero is applied
    # @test ensures the function returns the correct average value
    import numpy as np
    #another way to process the positive elements average to compare with
    positive_elements_float_array=np.array([i for i in testList if i >= 0], dtype=float)
    reference_average_value=np.mean(positive_elements_float_array)
    assert load_s1_script().average_above_zero(testList) ==reference_average_value

def test_s1_selective_average_non_zeros_values():
    ##
    # @test validates average_above_zero works fine with integer values >0
    check_s1_selective_average([1,2,3,4,-7])


def test_s1_selective_average_with_negative_values():
    ##
    # @test validates average_above_zero works fine with integer values <=0
    check_s1_selective_average([0,-7])

def test_s1_selective_average_with_string_values():
    ##
    # @test validates average_above_zero works fine with integer values <=0
    check_s1_selective_average(['ab','c'])

def test_s1_selective_average_with_string_values():
    ##
    # @test validates average_above_zero works fine with an empty list
    try:
        check_s1_selective_average([])
        assert False
    except ValueError:
        assert True
        
        
#  =========================== test about reverse_table
def test_reverse_table_value():
    ##
    # @test validates reverse_table works fine with correct array
    assert load_s1_script().reverse_table([1, 1, 2, 3, 5, 8]) == [8, 5, 3, 2, 1, 1]

def test_reverse_table_of_table():
    ##
    # @test validates reverse_table works fine with array in array
    assert load_s1_script().reverse_table([[1, 1], 2, 3, [5, 8]]) == [[5,8], 3, 2, [1, 1]]
def test_reverse_table_with_string():
    ##
    # @test validates reverse_table works fine with string instead of array
    try:
        load_s1_script().reverse_table('array')
        assert False
    except TypeError:
        assert True

          
#  =========================== test about roi_bbox



"""
def test_roi_bbox_value():
    ##
    # @test validates roi_bbox works fine with correct array
    import numpy as np
    image = np.array([[  0, 0, 0, 0, 0, 0],
                   [  0, 1, 0, 0, 0, 0],
                   [  0, 0, 0, 1, 0, 0],
                   [  0, 0, 0, 0, 0, 0],
                   [  0, 0, 1, 0, 0, 0],
                   [  0, 0, 0, 0, 0, 0]])

    assert load_s1_script().roi_bbox(image) == np.array([[1, 1],
                                                         [1, 3],
                                                         [4, 1],
                                                         [4, 3]])

def test_roi_bbox_of_table():
    ##
    # @test validates reverse_table works fine with array in array
    assert load_s1_script().reverse_table([[1, 1], 2, 3, [5, 8]]) == [[5,8], 3, 2, [1, 1]]
def test_roi_bbox_with_string():
    ##
    # @test validates reverse_table works fine with string instead of array
    try:
        load_s1_script().reverse_table('array')
        assert False
    except TypeError:
        assert True
        """
        