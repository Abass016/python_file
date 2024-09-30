# print("this project is for the user to guess a number correctly from the range of 1-10")

# import random
# print("Enter your name")
# name = input()

# print("you are asked to guess a number corectly from the range of 1-10")

# secret_key = random.randint(1, 10)

# print("guess the number")
# for trial in range(1, 6):
    
#     guess = int(input())
#     if guess > secret_key:
#         print("Your guess is high")
#     elif guess < secret_key:
#         print("your guess is low")
#     else:
#         print("Welldon, you have guessed the number correctly at " + str(int(trial)) + " times") 

# if secret_key == guess :
#     print("You have guess correctly")  
# else:
#     print("you have guess wrongly " + name + " the correct number is " + str(int(secret_key)))             


 

def General():
    return [
        {
            "Question": "The fattest animal on land is?",
            "options": ["A. Leopard", "B. Lion", "C. Tiger", "D. Elephant"],
            "Answer": "D"
        },
        {
            "Question": "The founder of Starlink is?",
            "options": ["A. Julius Berger", "B. Elon Musk", "C. Aliko Dangote", "D. Bill Gates"],
            "Answer": "B"
        },
        {
            "Question": "The highest goal scorer in the history of Football is who?",
            "options": ["A. L. Messi", "B. C. Ronaldo", "C. Pele", "D. Maradona"],
            "Answer": "B"
        },
        {
            "Question": "What is the capital of France?",
            "options": ["A. Paris", "B. Mumbai", "C. Ontario", "D. Francia"],
            "Answer": "A"
        }
    ]

def Mathematics():
    return [
        {
            "Question": "The multiplication of 4 by 4 is?",
            "options": ["A. 13", "B. 18", "C. 16", "D. 20"],
            "Answer": "C"
        },
        {
            "Question": "The multiplication of 4 by 5 is?",
            "options": ["A. 13", "B. 18", "C. 20", "D. 16"],
            "Answer": "C"
        }
    ]

def Examination1(exam):
    score = 0
    for objective in exam:
        print(objective["Question"])
        for opt in objective["options"]:
            print(opt)
        answer = input("Choose an option between (A, B, C, and D): ").upper()
        if answer == objective["Answer"]:
            print("Hooray!")
            score += 1
        else:
            print(f"Wrong answer. The correct answer was {objective['Answer']}.")
    print(f"You have scored {score} out of {len(exam)}")

def main():
    while True:
        print("\nYou are about to start your exam. Kindly choose the paper you are starting with:")
        print("1. General")
        print("2. Mathematics")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if choice == 1:
                exam = General()
            elif choice == 2:
                exam = Mathematics()
            elif choice == 3:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
                continue
            
            Examination1(exam)

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
