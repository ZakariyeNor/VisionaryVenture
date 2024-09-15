def add_two_num(num1, num2):
    print("Test the code")

add_two_num()




#Passing parameters and calling from the insode 
def add_two_num(num1, num2):
    print(num1, num2)

add_two_num(2, 3)




#Calling function inside in the function
def add_two_num(num1, num2):
    sum = num1 + num2
    print(sum)

add_two_num(2, 3)








#Calling the function out side of it's scope
def add_two_num(num1, num2):
    sum = num1 + num2
    return sum

result = add_two_num(10, 32)
print(result)

