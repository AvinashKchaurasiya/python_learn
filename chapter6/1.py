# conditional 
age = int(input("Enter your age : "))
if(age < 0):
    print("Kya bakwas kr rha hai be tera ba negative age me gya tha")
elif(age == 0):
    print("Tu aaj hi paida huwahai be")
elif(age >= 18 and age < 40):
    print("You are an adult")
elif(age >= 40):
    print("Now you are budhawu")
else:
    print("You are a chhota bachha")