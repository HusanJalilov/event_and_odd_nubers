#A four-digit integer is given. Find the number of even digits in it.
A=1244
#Create a variable "var_int" and assign it a four-digit integer value.
x1=A%10
A=A//10
x2=A%10
A=A//10
x3=A%10
A=A//10
x4=A%10
A=A//10
var_int=int(not(bool(x1%2)))+int(not(bool(x2%2)))+int(not(bool(x3%2)))+int(not(bool(x4%2)))
print(var_int)
#Print the number of even digits in the variable "var_int".