#A four-digit integer is given. Find the number of even digits in it.
var_int=1234
#Create a variable "var_int" and assign it a four-digit integer value.
x1=var_int%10
var_int=var_int//10
x2=var_int%10
var_int=var_int//10
x3=var_int%10
var_int=var_int//10
x4=var_int%10
var_int=var_int//10
s=int(bool(x1%2))+int(bool(x2%2))+int(bool(x3%2))+int(bool(x4%2))
print(s)
#Print the number of even digits in the variable "var_int".