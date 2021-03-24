import cataliistNester
movies =[
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]
]

"""
for each in movies:
    if isinstance(each,list):
        for inner_each in each:
            if isinstance(inner_each,list):
                for deeper_each in inner_each:
                    print(deeper_each)
            else:
                print(inner_each)        
    else:
        print(each)        
"""

print(cataliistNester.nested(movies))
