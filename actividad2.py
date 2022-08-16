edad = int(input("cual es tu edad"))
for i in range(0,edad): 
    print(i)
    

file = open("escribir.txt","w")
file.write(input("dime tu nombre"))
file.write(input("dime tu apellido materno"))
file.write(input("dime una UA de este periodo"))
file.write(input("dime una UA de este periodo"))
file.write(input("dime una UA de este periodo"))

file.close()