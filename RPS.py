#TASK 4
import random
ur_score = 0
com_score = 0
print("=== Rock Paper Scissors Game ===")
print("Instructions:")
print("rock beats scissors\nscissors beats paper\npaper beats rock")
while True:
    ur_choice = input("\nChoose rock, paper or scissors: ").lower()
    if ur_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue
    com_choice = random.choice(["rock", "paper", "scissors"])
    print("Your choice:", ur_choice)
    print("Computer choice:", com_choice)
    if ur_choice == com_choice:
        print("Result: It's a tie!")
    elif (ur_choice == "rock" and com_choice == "scissors") or \
         (ur_choice == "scissors" and com_choice == "paper") or \
         (ur_choice == "paper" and com_choice == "rock"):
        print("Result: You win!")
        ur_score += 1
    else:
        print("Result: You lose!")
        com_score += 1
    print("Score → You:", ur_score, "| Computer:", com_score)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nGame Over!")
        print("Final Score → You:", ur_score, "| Computer:", com_score)
        if ur_score > com_score:
             print("Overall Winner: You !")
        elif com_score > ur_score:
             print("Overall Winner: Computer ! ")
        else:
            print("Overall Result: It's a Tie !")
        break