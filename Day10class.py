# age = float(input("Enter your age: "))
# if age > 18.0:
#     print("You are a adult")
# elif age < 18.0:
#     print("You are a teenager")
# else:
#     print("You are a child")

# for i in range(0,5):
#     print(i)

# count = 0
# while count<=3:
#     print("Learning while loop:",count)
#     count=count+1

# for i in range (2,5):
#     for j in range(1,4):
#         print(i,j)

# import random

# number = random.randint(1, 100)
# attepts = 0

# print ("Welcome to the Guess the Number Game!",number)

# while True:
#     guess = int(input("Enter your guess: "))
#     attepts += 1
    
#     if guess < number:
#         print("Too low! Try again.")
#     elif guess > number:
#         print("Too high! Try again.")
#     else:
#         print(f"Congratulations! You've guessed the number {number} in {attepts} attempts.")
#         break


# List_numbers = [10,70,40,50,100]
# print(List_numbers)
# List_numbers.sort()
# print(List_numbers)
# List_numbers.sort(reverse=True)
# print(List_numbers)

# sorted_no =sorted(List_numbers)
# print(sorted_no)

# List_numbers.append(120)
# print(List_numbers)
# List_numbers.insert(2,45)
# print(List_numbers)

# List_numbers.remove(45)
# print(List_numbers)

# import random
# words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']
# random_word = random.choice(words)
# scrambled_word = ''.join(random.sample(random_word, len(random_word)))
# print(scrambled_word)
# attempts=0

# while True:
#     guess = input("Enter your guess: ")
#     attempts = attempts+1

#     if guess != random_word:
#         print("Please try again")
#     else:
#         print(f"Congrats, You got the correct word {random_word} in {attempts} attempts")
#         break

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# union_set = set1| set2  # Union of two sets
# print(union_set)

# intersection_set = set1 & set2  # Intersection of two sets
# print(intersection_set)

# difference_set = set2 - set1  # Difference of two sets
# print(difference_set)

# sym_diff_set = set1 ^ set2  # Symmetric difference of two sets
# print(sym_diff_set)

# set1.discard(20)
# print(set1)
# set1 = {1, 2, 3}
# set4 ={40,50,50}
# set5 ={50,70,60}
# set4.add(80)
# set6 = set1|set4
# set7 = set6 & set5
# print(set6)
# print(set7)

# import random
# options = ["rock", "paper", "scissors"]

# while True:
#     user_choice = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
#     if user_choice == 'exit':
#         print("Thanks for playing!")
#         break
    
#     if user_choice not in options:
#         print("Invalid choice. Please try again.")
#         continue
    
#     computer_choice = random.choice(options)
#     print(f"Computer chose: {computer_choice}")

#     result = (options.index(user_choice) - options.index(computer_choice)) % 3

#     if result == 0:
#         print("It's a tie!")
#     elif result == 1:
#         print("You win!")
#     else:
#         print("Computer Win!")

def my_function():
  print("Hello from a function")
my_function()

