# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
#to check the lenght
names_length = int(len(names))
#random.randint is ued to genrate random value -1 is used bcz index starts with Zero
random_person = random.randint(0,names_length-1)
name_of_the_random_person = names[random_person]
print(f"{name_of_the_random_person} is going to buy the meal today!")


