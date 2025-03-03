name = "Aya"
age = 22
country = "Egypt"
print("\" Hello \'" + name + "\', How You Doing \\ Your Age Is: \"" + str(age) + "\"\"+ And Your Country Is: " + country)
print("\" Hello \'" + name + "\', How You Doing \\ \n \"\"\" Your Age Is: \"" + str(age) + "\"\"+\n And Your Country Is: " + country)

name1= "Elzero"
print("Second letter is \""+name1[1]+"\"")
print("Third letter is \""+name1[2]+"\"")
print("Last letter is \""+name1[5]+"\"")
print(name1[1:4])
print(name1[0::2])
print(name1[-2::-2])

name2 = "#@#@Elzero#@#@"
print(name2.strip("#@"))

num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))    
print(num4.zfill(4))
print(num5.zfill(4))

name_one = "Osama"
name_two = "Osama_Elzero"

print("@" * (20 - len(name_one)) + name_one)
print("@" * (20 - len(name_two)) + name_two)

name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())


msg = "I Love Python And Although Love Elzero Web School"
print(msg.count("Love"))

print(name1.index("z"))

msg1 = "I <3 Python And Although <3 Elzero Web School"
print(msg1.replace("<3", "Love",1))
print(msg1.replace("<3", "Love"))

print(f"My Name Is {name},And my Age Is {age},And My Country Is {country}")