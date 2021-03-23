def nested(the_list):
    for each in the_list:
        if isinstance(each,list):
            nested(each)
        else:
            print(each)