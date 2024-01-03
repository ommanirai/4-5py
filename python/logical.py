'''
logical operator in python
logical and 
logical or 
logical not
'''

#logical and
'''
condition1  condition2  result(condition1 and condition2)
T           T           T and T => T
T           F           T and F => F
F           T           F and T => F
F           F           F and F => F
'''
n1 = 12
n2 = 50
condition1 = n1 > 10 
condition2 = n1 > 15
condition3 = n2 > 50

# print(condition1)

result = condition1 and condition2 and condition3

# print(result)

username = 'ram'
password = 'ram234'

login_success = username=='ram' and password=='ram123'
# print(login_success)


#logical or
'''
condition1  condition2   result(condition1 or condition2)
T           T            T or T => T
T           F            T or F => T
F           T            F or T => T
F           F            F or F => F
'''
name = 'Hari'
address = 'Lalitpur'
res = name == "hari" or address == "Lalitpur"
# print(res)
# print( name == "hari" or address == "Lalitpur")

results = name == "Hari" or address == "Lalitpur" or login_success
results = True and (True or False)
# print(results)

a = True and True and results
# print(a)


# logical not
'''
condition1  result(not condition)
T           not T => F
F           not F => T
'''
b = True
print(not b)