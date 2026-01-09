#TASK 4
import random
u_score = 0
c_score = 0
print("=== Rock Paper Scissors Game ===")
print("Instructions:")
print("rock beats scissors\nscissors beats paper\npaper beats rock")
while True:
    u_choice = input("\nChoose rock, paper, or scissors: ").lower()
    if u_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue
    c_choice = random.choice(["rock", "paper", "scissors"])
    print("Your choice:", u_choice)
    print("Computer choice:", c_choice)
    if u_choice == c_choice:
        print("Result: It's a tie!")
    elif (u_choice == "rock" and c_choice == "scissors") or \
         (u_choice == "scissors" and c_choice == "paper") or \
         (u_choice == "paper" and c_choice == "rock"):
        print("Result: You win!")
        u_score += 1
    else:
        print("Result: You lose!")
        c_score += 1
    print("Score → You:", u_score, "| Computer:", c_score)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nGame Over!")
        print("Final Score → You:", u_score, "| Computer:", c_score)
        break