# Custom Exception class
class ListDivideException(Exception):
    pass

# Function to count divisible numbers
def list_divide(numbers,divide=2):
    return len([num for num in numbers if num % divide ==0])

# Function to test list_divide
def test_list_divide():
    try:
        assert list_divide([1, 2 , 3, 4, 5]) == 2
        assert list_divide([2, 4, 6, 8, 10,]) == 5
        assert list_divide([30, 54, 63, 98, 100], divide=10) ==2
        assert list_divide([]) == 0
        assert list_divide([1, 2, 3, 4, 5,], 1) ==5
    except AssertionError:
        raise ListDivideException("Test failed!")

# Run the test function
if __name__ == "__main__":
    test_list_divide()

