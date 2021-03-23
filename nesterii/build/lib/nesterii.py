"""
This is nesterii.py
The script prints lists that may or may not be included nested lists

Usages:
nested(argument)
argument - argument could be list or list with nested list

Output:
Prints each item recursively on each line
"""

def nested(the_list):
    for each in the_list:
        if isinstance(each,list):
            nested(each)
        else:
            print(each)
