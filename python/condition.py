'''
condition in python
1. if
syntax:
if condition:
    body of if
2. elif
3. else
if condition:
    body of if
else:
    body of else
'''
n = int(input("enter the number to check odd or even"))
# if n >20:
#     print(n," is greater than 20")
# print("welcome")

if n%3==0 and n%7==0:
    print(n, 'is divisible by both 3 and 7')
else:
    if n%3==0 or n%7==0:
        print(n, 'is divisible by 3 or 7')
        if n%3==0:
            print(n, 'is divisibel by 3')
        else:
            print(n, 'is divisible by 7')
    else:
        print(n, 'is not divisible by both 3 and 7')
        

# if n%2==0: 
#     print(n, 'is even number')
# else:
#     print(n, 'is odd number')

'''
nepali = int(input("ente the marks of nepali"))
english = int(input("enter the marks of english"))
science = int(input("enter the marks of science"))
> 35 => pass
percentage => ((nepali + english + science)/total_marks)*100
90> A
80-90 => B+
70-80 => B
60-70 => C+
<60 => C


<35 => fail


'''