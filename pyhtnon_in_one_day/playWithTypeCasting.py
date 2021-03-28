"""
Disclaimer: int, float and str variables covered
"""

#Define variables
integer_num = 5
float_num = 5.10
string_num = "5"

#Check type of variables
print("type before conversion:")
print("integer_num: " + str(integer_num) + ", " + str(type(integer_num)))
print("float_num: " + str(float_num) + ", " + str(type(float_num)))
print("string_num: " + string_num + ", " + str(type(string_num)))
print("\n")

#Conversion
float_num = int(float_num)
integer_num = str(integer_num)
string_num = int(string_num)

#Check type of variables
print("type after conversion:")
print("integer_num: " + integer_num + ", " + str(type(integer_num)))
print("float_num: " + str(float_num) + ", " + str(type(float_num)))
print("string_num: " + str(string_num) + ", " + str(type(string_num)))
