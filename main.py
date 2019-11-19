#This is main file to run PYthon file.
import add
import subtraction
import multiplication
import div
print("<-- Addition subtraction Program -->\n1.Addition\n2.Subtraction\n3.multiplication\n4.division")
inp = int(input("Enter your choice-->"))

if(inp==1):
	print(add.add())
elif(inp==2):
	print(subtraction.sub())
elif(inp==3):
	print(multiplication.multiply())
elif(inp==4):
	print(div.div())
else:
	print("Wrong choice")
