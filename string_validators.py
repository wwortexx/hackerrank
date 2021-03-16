"""
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
"""
if __name__ == '__main__':
    s = input()
    l = list(s)
    first = False
    second = False
    third = False
    fourth = False
    fifth = False
    for c in l:
        if c.isalnum():
            first = True
        if c.isalpha():
            second = True
        if c.isdigit():
            third = True
        if c.isalpha() and c.islower():
            fourth = True
        if c.isalpha() and c.isupper():
            fifth = True
    print(first)
    print(second)
    print(third)
    print(fourth)
    print(fifth)