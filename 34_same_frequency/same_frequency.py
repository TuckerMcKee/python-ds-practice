def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)
    for i in range(len(num1_str)):
        if not num1_str.count(num1_str[i]) == num2_str.count(num1_str[i]):
            return False
    return True     
