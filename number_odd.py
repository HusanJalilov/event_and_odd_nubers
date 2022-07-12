#A four-digit integer is given. Find the number of odd digits in it.
number=1551
#Create a variable "var_int" and assign it a four-digit integer value.
x1=number%10
number=number//10
x2=number%10
number=number//10
x3=number%10
number=number//10
x4=number%10
number=number//10
#Print the number of odd digits in the variable "var_int"
var_int=x1%2+x2%2+x3%2+x4%2
print(var_int)
