import random

def is_positive(num):
    return num>0
    # return true if num is positive, otherwise return false

    
def is_even(num):
    return num%2==0
    # return true if num is even, otherwise return false


def is_positive_and_even(num):
    return num>0 and num%2==0
    # return true if num is positive and even, otherwise return false


def is_positive_or_even(num):
    return num>0 or num%2==0
    # return true if num is positive or even, otherwise return false

