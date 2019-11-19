#This is main file to run PYthon file.
import add
import subtraction

print("<-- Addition subtraction Program -->\n1.Addition\n2.Subtraction")
inp = int(input("Enter your choice-->"))

if(inp==1):
	print(add.add())
elif(inp==2):
	print(subtraction.subt())
else:
	print("Wrong choice")
