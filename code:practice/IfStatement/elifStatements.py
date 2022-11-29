# elifStatements.py
# @ author : amy
# date : 02. 11. 22


#challenage1
magnitude = float(input("Please enter magnitude of the earthquake\n\n"))

if magnitude >=10.0:
 print("Meteoric.\n\n")
elif magnitude >=8 and magnitude <10:
    print("Great.\n\n")
elif magnitude >=7 and magnitude <8:
    print("Major.\n\n")
elif magnitude >=6 and magnitude <7:
    print("Strong.\n\n")
elif magnitude >=5 and magnitude <6:
    print("Moderate.\n\n")
elif magnitude >=4 and magnitude <5:
    print("Light.\n\n")
elif magnitude >=3 and magnitude <4:
    print("Minor.\n\n")
elif magnitude >=2 and magnitude <2:
    print("Very minor.\n\n")
else:
    print("Micro.\n\n")


#Challange3
letter = (input("Please enter a letter of the alphabet.\n\n"))

if letter.lower()==("a" or "e" or "i" or "o" or "u"):
    print("The letter you have entered is vowel.\n\n")
elif letter.lower() == "y":
    print("Sometimes y is a vowel, and sometimes y is consonant.\n\n")
else:
    print("The letter is a consonant.\n\n")


#Challange5

year = int(input("Please enter a your Birth year.\n\n"))

if year % 12 == 0:
  print(year,"is the year of the Monkey.\n\n")
elif year % 12 == 1:
  print(year,"is the year of the Rooster.\n\n")            
               
elif year % 12 == 2:
  print(year,"is the year of the Dog.\n\n")
elif year % 12 == 3:
  print(year,"is the year of the Pig.\n\n")
elif year % 12 == 4:
  print(year,"is the year of the Rat.\n\n")
elif year % 12 == 5:
  print(year,"is the year of the Ox.\n\n")
elif year % 12 == 6:
  print(year,"is the year of the Tiger.\n\n")
elif year % 12 == 7:
  print(year,"is the year of the Hare.\n\n")
elif year % 12 == 8:
  print(year,"is the year of the Dragon.\n\n")
elif year % 12 == 9:
  print(year,"is the year of the Snake.\n\n")
elif year % 12 == 10:
  print(year,"is the year of the Horse.\n\n")
elif year % 12 == 11:
  print(year,"is the year of the Sheep.\n\n")
else:
    print("You have entered an incorrect year. Please enter again.\n\n")

       
     

