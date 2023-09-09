class utils:
    @staticmethod
    def reversed(number):
        if type(number) is not int:
            raise TypeError("input is not int.")
        string = str(number)
        rev_string = string[::-1]
        rev_num = int(rev_string)
        return rev_num
    
    @staticmethod
    def formatter(number):
        if type(number) is not int:
            raise TypeError("input is not int.")
        bin_num = bin(number)
        oct_num = oct(number)
        return bin_num, oct_num
