import utils
def test_reverse():
    #int
    print("reversed(12345)")
    int_result = utils.utils.reversed(12345)
    assert int_result == 54321, "Expected: 54321"
    #string
    try:
        utils.utils.reversed("12345")
    except TypeError:
        print("TypeError raised for string.")
    else:
        raise AssertionError("TypeError not raised")
    #float
    try:
        utils.utils.reversed(12.345)
    except TypeError:
        print("TypeError raised for float.")
    else:
        raise AssertionError("TypeError not raised")
    
def test_formatter():
    #int
    print("formatter(12)")
    bin_result, oct_result = utils.utils.formatter(12)
    assert bin_result == "0b1100", "Expected: 0b1100"
    assert oct_result == "0o14", "Expected: 0o14"
    #string
    try:
        utils.utils.formatter("12345")
    except TypeError:
        print("TypeError raised for string.")
    else:
        raise AssertionError("TypeError not raised")
    #float
    try:
        utils.utils.formatter(12.345)
    except TypeError:
        print("TypeError raised for float.")
    else:
        raise AssertionError("TypeError not raised")

test_reverse()
test_formatter()